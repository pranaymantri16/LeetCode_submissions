def count_distinct_prime_factors(num):
    count = 0
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            count += 1
            while num % factor == 0:
                num //= factor
        factor += 1
    if num > 1:
        count += 1
    return count

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MODULO = 10**9 + 7
        n = len(nums)
        
        elements = [(idx, count_distinct_prime_factors(num), num) for idx, num in enumerate(nums)]
        prev_greater = [-1] * n
        next_greater = [n] * n
        stack = []
        
        for i, prime_factor_count, num in elements:
            while stack and stack[-1][0] < prime_factor_count:
                stack.pop()
            if stack:
                prev_greater[i] = stack[-1][1]
            stack.append((prime_factor_count, i))
        
        stack.clear()
        
        for i, prime_factor_count, num in reversed(elements):
            while stack and stack[-1][0] <= prime_factor_count:
                stack.pop()
            if stack:
                next_greater[i] = stack[-1][1]
            stack.append((prime_factor_count, i))
        elements.sort(key=lambda x: -x[2])
        result = 1
        for index, prime_count, value in elements:
            left_range = index - prev_greater[index]
            right_range = next_greater[index] - index
            possible_selections = left_range * right_range
            
            if possible_selections <= k:
                result = (result * pow(value, possible_selections, MODULO)) % MODULO
                k -= possible_selections
            else:
                result = (result * pow(value, k, MODULO)) % MODULO
                break

        return result
