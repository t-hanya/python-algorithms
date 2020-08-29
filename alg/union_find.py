"""
Implement an union find data structure.
"""


class UnionFind:
    """An union find data structure.

    Args:
        n (int): Number of items in the union find object.
    """

    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, i: int) -> None:
        """Find the set identifier for the item `i`."""
        if self.parent[i] == i:
            return i
        else:
            return self.find(self.parent[i])

    def unite(self, i: int, j: int) -> None:
        """Unite sets containing i and j into a single set."""
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1

