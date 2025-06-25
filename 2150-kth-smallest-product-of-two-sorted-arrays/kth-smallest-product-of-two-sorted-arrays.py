class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def split_neg_pos(arr):
            neg = []
            pos = []
            for val in arr:
                if val < 0:
                    neg.append(-val)
                else:
                    pos.append(val)
            neg.reverse()
            return neg, pos

        def count_pairs_leq_x(arr1, arr2, x):
            count = 0
            j = len(arr2) - 1
            for val in arr1:
                while j >= 0 and val * arr2[j] > x:
                    j -= 1
                count += j + 1
            return count

        nums1_neg, nums1_pos = split_neg_pos(nums1)
        nums2_neg, nums2_pos = split_neg_pos(nums2)

        total_negative_products = len(nums1_neg) * len(nums2_pos) + len(nums1_pos) * len(nums2_neg)
        sign = 1

        if k > total_negative_products:
            k -= total_negative_products
        else:
            k = total_negative_products - k + 1
            sign = -1
            nums2_neg, nums2_pos = nums2_pos, nums2_neg

        left, right = 0, int(1e10)

        while left < right:
            mid = (left + right) // 2
            count = count_pairs_leq_x(nums1_neg, nums2_neg, mid) + count_pairs_leq_x(nums1_pos, nums2_pos, mid)
            if count >= k:
                right = mid
            else:
                left = mid + 1

        return sign * left
