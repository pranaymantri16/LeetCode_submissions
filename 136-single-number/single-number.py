class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result