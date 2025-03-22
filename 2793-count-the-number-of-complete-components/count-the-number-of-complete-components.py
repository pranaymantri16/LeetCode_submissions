class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        visited = set()
        complete_components = 0

        def dfs(node, component):
            stack = [node]
            visited.add(node)
            while stack:
                curr = stack.pop()
                component.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        for node in range(n):
            if node not in visited:
                component = set()
                dfs(node, component)
                size = len(component)
                edge_count = sum(len(graph[v]) for v in component) // 2
                if edge_count == (size * (size - 1)) // 2:
                    complete_components += 1

        return complete_components
