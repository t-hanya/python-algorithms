"""
Unittest for union_find module
"""


from alg.union_find import UnionFind


class TestUnionFind:

    def test(self):
        uf = UnionFind(10)
        uf.unite(1, 3)
        uf.unite(3, 5)
        uf.unite(3, 7)
        assert uf.find(1) == uf.find(7)
        assert uf.find(1) != uf.find(2)

