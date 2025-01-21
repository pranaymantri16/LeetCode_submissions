class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        ps = self.countAndSay(n - 1)
        result = ""
        count = 1
        for i in range(1, len(ps)):
            if ps[i] == ps[i - 1]:
                count += 1
            else:
                result += str(count) + ps[i - 1]
                count = 1
        result += str(count) + ps[-1]
        return result
