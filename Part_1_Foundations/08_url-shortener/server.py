"""HTTP routes (stdlib only): POST /shorten {"url": ...} -> short key; GET /<key> -> redirect."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from key_generator import generate_key
from store import TTLStore

class ShortenerHandler(BaseHTTPRequestHandler):
    store: TTLStore

    def do_POST(self) -> None:
        """/shorten: read JSON {"url"}, store under a fresh key, respond with the short key."""
        raise NotImplementedError

    def do_GET(self) -> None:
        """/<key>: redirect (or return the value). Unknown or expired key -> 404."""
        raise NotImplementedError


def run(host: str = "127.0.0.1", port: int = 8000) -> None:
    ShortenerHandler.store = TTLStore()
    ThreadingHTTPServer((host, port), ShortenerHandler).serve_forever()


if __name__ == "__main__":
    run()
