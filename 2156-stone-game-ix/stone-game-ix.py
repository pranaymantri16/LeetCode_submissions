import collections

class Solution:
    def stoneGameIX(self, stones):
        stone_count = collections.Counter(stone % 3 for stone in stones)
        count_0, count_1, count_2 = stone_count[0], stone_count[1], stone_count[2]
        if min(count_1, count_2) == 0:
            return max(count_1, count_2) > 2 and count_0 % 2 == 1
        return abs(count_1 - count_2) > 2 or count_0 % 2 == 0
