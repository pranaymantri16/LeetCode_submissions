class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(num_str: str, target: int, index: int, current_sum: int) -> bool:
            if index == len(num_str):
                return current_sum == target
            for i in range(index, len(num_str)):
                part = int(num_str[index:i + 1])
                if current_sum + part <= target and can_partition(num_str, target, i + 1, current_sum+part):
                    return True
            return False
        total = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i, 0, 0):
                total += i * i
        return total
