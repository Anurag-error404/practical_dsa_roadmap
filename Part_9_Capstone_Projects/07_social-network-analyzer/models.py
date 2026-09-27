"""Friend graph shared by BFS, union-find, and top-K. Storage only."""
from collections.abc import Hashable
from dataclasses import dataclass, field

UserId = Hashable


@dataclass
class FriendGraph:
    adj: dict[UserId, set[UserId]] = field(default_factory=dict)

    def add_user(self, u: UserId) -> None:
        self.adj.setdefault(u, set())

    def add_friendship(self, a: UserId, b: UserId) -> None:
        self.add_user(a)
        self.add_user(b)
        self.adj[a].add(b)
        self.adj[b].add(a)

    def users(self) -> list[UserId]:
        return list(self.adj)

    def friends(self, u: UserId) -> set[UserId]:
        return self.adj[u]
