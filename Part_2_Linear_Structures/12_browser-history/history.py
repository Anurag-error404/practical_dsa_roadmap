"""Two stacks: back_stack, forward_stack."""


class BrowserHistory:
    def __init__(self, homepage: str):
        raise NotImplementedError

    @property
    def current(self) -> str:
        raise NotImplementedError

    def visit(self, url: str) -> None:
        """Navigate to url. Clears forward history."""
        raise NotImplementedError

    def back(self) -> str:
        """Go back one page and return the current page. Nothing before: no-op."""
        raise NotImplementedError

    def forward(self) -> str:
        """Go forward one page and return the current page. Nothing ahead: no-op."""
        raise NotImplementedError
