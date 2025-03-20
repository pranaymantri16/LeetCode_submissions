class Solution:
    def getRoot(self, node, roots):
        if roots[node] != node:
            roots[node] = self.getRoot(roots[node], roots)
        return roots[node]

    def minimumCost(self, n, edges, queries):
        roots = list(range(n))
        minAndCost = [-1] * n
        for u, v, weight in edges:
            rootU = self.getRoot(u, roots)
            rootV = self.getRoot(v, roots)
            minAndCost[rootU] = weight if minAndCost[rootU] == -1 else minAndCost[rootU] & weight
            minAndCost[rootV] = weight if minAndCost[rootV] == -1 else minAndCost[rootV] & weight

            if rootU != rootV:
                roots[rootU] = rootV  # Union operation
                minAndCost[rootV] &= minAndCost[rootU]
        results = []
        for src, dest in queries:
            if src == dest:
                results.append(0)
            elif self.getRoot(src, roots) != self.getRoot(dest, roots):
                results.append(-1)
            else:
                results.append(minAndCost[self.getRoot(src, roots)])

        return results
