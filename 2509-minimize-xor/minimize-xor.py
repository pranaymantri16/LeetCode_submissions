class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num2_set_bits = bin(num2).count('1')
        result = 0
        num1_set_bits = bin(num1).count('1')
        for i in range(31, -1, -1):
            if num1 & (1 << i):
                if num2_set_bits > 0:
                    result |= (1 << i)
                    num2_set_bits -= 1
        for i in range(32):
            if num2_set_bits == 0:
                break
            if not (result & (1 << i)):
                result |= (1 << i)
                num2_set_bits -= 1
        return result
