class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        left, right = 0, len(height) - 1
        lm, rm = 0, 0
        wt = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= lm:
                    lm = height[left]
                else:
                    wt += lm - height[left]
                left += 1
            else:
                if height[right] >= rm:
                    rm = height[right]
                else:
                    wt += rm - height[right]
                right -= 1
        return wt
