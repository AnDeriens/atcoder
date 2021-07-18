
class UnionFind:
    def __init__(self, n):
        self.parents = { i: -1 for i in range(1, n + 1) }
        self.siz = {i: 1 for i in range(1, n + 1) }

    def root(self, x):
        if self.parents[x] == -1:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.siz[x] < self.siz[y]:
            x, y = y, x

        self.parents[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x):
        return self.siz[self.root(x)]


uf = UnionFind(7)
uf.unite(2, 3)
uf.unite(3, 4)
uf.unite(6, 7)
uf.unite(2, 7)

print(uf.parents)
print(uf.siz)
