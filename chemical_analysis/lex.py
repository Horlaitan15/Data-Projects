class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def solution(str, pairs):
    n = len(str)
    uf = UnionFind(n)

    for pair in pairs:
        uf.union(pair[0] - 1, pair[1] - 1)

    components = {}
    for i in range(n):
        root = uf.find(i)
        if root not in components:
            components[root] = []
        components[root].append(str[i])

    for key in components:
        components[key].sort(reverse=True)

    result = [''] * n
    for i in range(n):
        root = uf.find(i)
        result[i] = components[root].pop(0)

    return ''.join(result)

# Example usage
str_val = "abdc"
pairs_val = [[1, 4], [3, 4]]
output = solution(str_val, pairs_val)
print(output)  # Output: "dbca"
