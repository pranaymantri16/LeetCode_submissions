class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        R = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                d1 = int(num1[i])
                d2 = int(num2[j])
                p = d1 * d2
                R[i + j] += p
                R[i + j + 1] += R[i + j] // 10
                R[i + j] %= 10
        while len(R) > 1 and R[-1] == 0:
            R.pop()
        return ''.join(map(str, R[::-1]))
