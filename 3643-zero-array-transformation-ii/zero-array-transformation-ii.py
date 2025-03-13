class Solution(object):
    def minZeroArray(self, nums, queries):
        n = len(nums)
        sv = 0
        qc = 0
        Da = [0] * (n + 1)
        for i in range(n):
            while sv + Da[i] < nums[i]:
                qc += 1
                if qc > len(queries):
                    return -1
                left, right, value = queries[qc - 1]
                if right >= i:
                    Da[max(left, i)] += value
                    if right + 1 < len(Da):
                        Da[right + 1] -= value
            sv += Da[i]
        return qc