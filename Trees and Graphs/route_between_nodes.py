from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = {i: False for i in range(n)}
        adj_list = {}
        for i in range(len(edges)):
            v1, v2 = edges[i]
            if v1 not in adj_list:
                adj_list[v1] = []
            if v2 not in adj_list:
                adj_list[v2] = []

            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        def dfs(node, d):
            visited[node] = True
            if node == d:
                return True
            for ch in adj_list[node]:
                if not visited[ch]:
                    v = dfs(ch, d)
                    if v:
                        return True

        if dfs(source, destination):
            return True
        return False
