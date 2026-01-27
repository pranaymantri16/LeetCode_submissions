class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))
        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue
            for v, w in graph[u]:
                if cost + w < dist[v]:
                    dist[v] = cost + w
                    heapq.heappush(pq, (cost + w, v))
        return -1 if dist[n - 1] == INF else dist[n - 1]