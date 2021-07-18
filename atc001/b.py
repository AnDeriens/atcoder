n, q = list(map(int, input().split()))

class UnionFind:
    def __init__(self, n):
        # 子をキー、親を値に持つ辞書
        self.parents = {i: -1 for i in range(n)}
        # 木の深さ。根の項のみ正しい値が保証される
        self.siz = {i: 1 for i in range(n)}

    # ノードxを含むグループの代表元を返す
    # ノードxに対応する根を返す
    def root(self, x):
        if self.parents[x] == -1:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    # ２つの値が同じグループに属するか
    # ２つの値の根が同じかどうかを判定
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unit(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.siz[x] < self.siz[y]:
            x, y = y, x

        # サイズが小さい方に大きい方の木をつける
        self.parents[y] = x
        self.siz[x] = self.siz[y]

    def size(self, x):
        return self.siz[self.root(x)]


uf = UnionFind(n)

for i in range(q):
    p, a, b = list(map(int, input().split()))
    if p == 0:
        uf.unit(a, b)
    else:
        if uf.issame(a, b):
            print('Yes')
        else:
            print('No')
