from collections import defaultdict
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        methods = defaultdict(list)

        for key, value in invocations:
            methods[key].append(value)
        
        visited = [False] * n

        def dfs(node):
            if visited[node] == True:
                return
            visited[node] = True
            for i in methods[node]:
                dfs(i)

        dfs(k)

        for key, value in invocations:
            if not visited[key] and visited[value]:
                return list(range(n))
        
        result = []

        for i in range(n):
            if not visited[i]:
                result.append(i)
        return result