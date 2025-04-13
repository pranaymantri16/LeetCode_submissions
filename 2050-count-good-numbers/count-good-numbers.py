class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def mod_pow(base, exp, mod):
            result = 1
            base %= mod
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        return (mod_pow(5, even_positions, MOD) * mod_pow(4, odd_positions, MOD)) % MOD
