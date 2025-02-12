class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common_digits = set(nums1) & set(nums2)
        if common_digits:
            return min(common_digits)
        min1, min2 = min(nums1), min(nums2)
        return min(min1 * 10 + min2, min2 * 10 + min1)
