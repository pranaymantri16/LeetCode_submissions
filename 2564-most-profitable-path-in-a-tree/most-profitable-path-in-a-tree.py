class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        n = len(amount)
        bob_time = [-1] * n
        def dfs_bob(node, parent, time):
            bob_time[node] = time
            if node == 0:
                return True
            for neighbor in graph[node]:
                if neighbor != parent and dfs_bob(neighbor, node, time + 1):
                    return True
            bob_time[node] = -1
            return False
        dfs_bob(bob, -1, 0)
        def dfs_alice(node, parent, time):
            income = 0
            if bob_time[node] == -1 or time < bob_time[node]:
                income += amount[node]
            elif time == bob_time[node]:
                income += amount[node] // 2
            if len(graph[node]) == 1 and node != 0:
                return income
            max_child_income = float('-inf')
            for neighbor in graph[node]:
                if neighbor != parent:
                    max_child_income = max(max_child_income, dfs_alice(neighbor, node, time + 1))
            return income + (max_child_income if max_child_income != float('-inf') else 0)
        return dfs_alice(0, -1, 0)
