from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # if all courses can finish,course order should follow topological order
        # create adj list and calculate in-degrees for all nodes
        indegrees = {}
        adj_list = {}
        for i in range(numCourses):
            indegrees[i] = 0
            adj_list[i] = []
        # prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        # adj_list = {0:[1,2],1:[3],2:[3],3:[]}
        # in-degrees = {0:0,1:1,2:1,3:2}
        for course, pre in prerequisites:
            indegrees[course] += 1
            adj_list[pre].append(course)

        # if in-degree is 0,we can start by that course
        # while finishing course,decrease in-degree for nei node
        # if any nei node's in-degree is 0,we can start that course,so add to queue
        from collections import deque
        que = deque()
        for k, v in indegrees.items():
            if v == 0:
                que.append(k)
        order = []
        while que:
            cn = que.popleft()
            order.append(cn)
            for nei in adj_list[cn]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    que.append(nei)
        return order if len(order) == numCourses else []