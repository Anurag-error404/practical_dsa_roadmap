"""Content-addressable storage (hash -> content)."""


class BlobStore:
    def __init__(self):
        raise NotImplementedError

    def put(self, content: str) -> str:
        """Store content under its content hash and return the hash (identical content reuses the blob)."""
        raise NotImplementedError

    def get(self, blob_hash: str) -> str:
        raise NotImplementedError

    def __contains__(self, blob_hash: str) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
