from collections import deque, defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        in_degree = [0] * n
        for src in range(n):
            for dest in graph[src]:
                reverse_graph[dest].append(src)
                in_degree[src] += 1
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        safe_nodes = []
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return sorted(safe_nodes)
