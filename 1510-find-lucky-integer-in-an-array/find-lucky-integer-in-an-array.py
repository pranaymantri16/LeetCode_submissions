class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        result = -1
        for num, freq in count.items():
            if num == freq:
                result = max(result, num)
        return result
