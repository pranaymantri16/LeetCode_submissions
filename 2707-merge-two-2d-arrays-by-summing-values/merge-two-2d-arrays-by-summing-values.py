class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        M = {}
        for id1, val1 in nums1:
            M[id1] = M.get(id1, 0) + val1
        for id2, val2 in nums2:
            M[id2] = M.get(id2, 0) + val2
        return [[id, val] for id, val in sorted(M.items())]