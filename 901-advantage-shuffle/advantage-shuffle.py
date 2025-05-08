from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        A = sorted([(val, i) for i, val in enumerate(nums2)], reverse=True)

        R = [0] * len(nums1)
        l, h = 0, len(nums1) - 1

        for val, i in A:
            if nums1[h] > val:
                R[i] = nums1[h]
                h -= 1
            else:
                R[i] = nums1[l]
                l += 1
        return R
