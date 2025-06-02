class Solution(object):
    def distributeCandies(self, total_candies, max_candies_per_child):
        total_ways = (total_candies + 2) * (total_candies + 1) // 2
        for count_exceeding in range(1, 4):
            remaining = total_candies - count_exceeding * (max_candies_per_child + 1)
            if remaining < 0:
                break
            combinations = (remaining + 2) * (remaining + 1) // 2
            multiplier = 3 if count_exceeding < 3 else 1
            if count_exceeding % 2 == 1:
                total_ways -= multiplier * combinations
            else:
                total_ways += multiplier * combinations
        return total_ways
