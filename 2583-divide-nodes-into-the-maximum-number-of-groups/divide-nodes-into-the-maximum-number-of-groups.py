class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        color = {}
        def is_bipartite(start):
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
            return True
        def bfs_max_depth(start):
            queue = deque([start])
            visited = {start}
            depth = 0
            
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                depth += 1
            
            return depth

        visited_global = set()
        total_groups = 0

        for node in range(1, n + 1):
            if node not in visited_global:
                if not is_bipartite(node):
                    return -1
                component = set()
                queue = deque([node])
                visited_global.add(node)
                while queue:
                    curr = queue.popleft()
                    component.add(curr)
                    for neighbor in graph[curr]:
                        if neighbor not in visited_global:
                            visited_global.add(neighbor)
                            queue.append(neighbor)
                max_groups = 0
                for c_node in component:
                    max_groups = max(max_groups, bfs_max_depth(c_node))
                total_groups += max_groups
        return total_groups
