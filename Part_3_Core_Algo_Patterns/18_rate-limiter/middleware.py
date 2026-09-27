"""WSGI middleware: intercepts requests, consults the limiter, returns 429 when denied."""
import argparse
import time
from collections.abc import Callable
from wsgiref.simple_server import make_server

from sliding_window_limiter import SlidingWindowLimiter


class RateLimitMiddleware:
    def __init__(self, app: Callable, limiter: SlidingWindowLimiter,
                 client_id: Callable[[dict], str] = lambda environ: environ.get("REMOTE_ADDR", "?"),
                 clock: Callable[[], float] = time.time):
        self.app = app
        self.limiter = limiter
        self.client_id = client_id
        self.clock = clock

    def __call__(self, environ: dict, start_response: Callable):
        if self.limiter.allow(self.client_id(environ), self.clock()):
            return self.app(environ, start_response)
        start_response("429 Too Many Requests", [("Content-Type", "text/plain")])
        return [b"rate limit exceeded\n"]


def hello_app(environ: dict, start_response: Callable):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [b"ok\n"]


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description="Demo server behind the sliding-window rate limiter.")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--window", type=float, default=60.0, help="seconds")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args(argv)
    app = RateLimitMiddleware(hello_app, SlidingWindowLimiter(args.limit, args.window))
    print(f"serving on http://127.0.0.1:{args.port} ({args.limit} req / {args.window}s per client)")
    make_server("127.0.0.1", args.port, app).serve_forever()


if __name__ == "__main__":
    main()
