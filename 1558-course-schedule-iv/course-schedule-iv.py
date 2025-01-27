class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            isPrerequisite[u][v] = True
        for k in range(numCourses):  # Intermediate node
            for i in range(numCourses):  # Start node
                for j in range(numCourses):  # End node
                    if isPrerequisite[i][k] and isPrerequisite[k][j]:
                        isPrerequisite[i][j] = True
        result = []
        for u, v in queries:
            result.append(isPrerequisite[u][v])
        return result
