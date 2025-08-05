class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        counter = defaultdict(int)
        max_fruits = 0

        for right in range(len(fruits)):
            counter[fruits[right]] += 1
            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
