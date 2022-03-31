from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # map to keep track of visited nodes
        visited = {i: False for i in range(n)}

        # since nodes are bidirectional, create bidirectional adjacency list
        adj_list = {}
        for i in range(len(edges)):
            v1, v2 = edges[i]
            if v1 not in adj_list:
                adj_list[v1] = []
            if v2 not in adj_list:
                adj_list[v2] = []

            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        # use dfs to find if there is a path from source to destination
        # time complexity: O(V + E) where V is the number of vertices and E is the number of edges
        # space complexity: O(V)
        def dfs(node, d):
            visited[node] = True
            # if destination is found, return True
            if node == d:
                return True
            # otherwise iterate through all adjacent nodes
            for ch in adj_list[node]:
                if not visited[ch]:
                    v = dfs(ch, d)
                    if v:
                        return True

        if dfs(source, destination):
            return True
        return False
