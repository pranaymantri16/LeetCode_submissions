class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        ALPHABET_SIZE = 26

        # Build transformation matrix based on nums
        def build_transformation_matrix() -> List[List[int]]:
            matrix = [[0] * ALPHABET_SIZE for _ in range(ALPHABET_SIZE)]
            for src in range(ALPHABET_SIZE):
                steps = nums[src]
                for offset in range(1, steps + 1):
                    dst = (src + offset) % ALPHABET_SIZE
                    matrix[src][dst] += 1
            return matrix

        # Multiply two matrices modulo MOD
        def multiply_matrices(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            result = [[0] * ALPHABET_SIZE for _ in range(ALPHABET_SIZE)]
            for i in range(ALPHABET_SIZE):
                for k in range(ALPHABET_SIZE):
                    if a[i][k] == 0:
                        continue
                    for j in range(ALPHABET_SIZE):
                        result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % MOD
            return result

        # Raise a matrix to the power of `t` using binary exponentiation
        def exponentiate_matrix(base: List[List[int]], exp: int) -> List[List[int]]:
            identity = [[int(i == j) for j in range(ALPHABET_SIZE)] for i in range(ALPHABET_SIZE)]
            while exp > 0:
                if exp % 2 == 1:
                    identity = multiply_matrices(identity, base)
                base = multiply_matrices(base, base)
                exp //= 2
            return identity

        # Step 1: Construct transformation matrix
        transformation_matrix = build_transformation_matrix()

        # Step 2: Raise the transformation matrix to power `t`
        final_matrix = exponentiate_matrix(transformation_matrix, t)

        # Step 3: Create initial frequency vector for input string
        initial_frequencies = [0] * ALPHABET_SIZE
        for ch in s:
            initial_frequencies[ord(ch) - ord('a')] += 1

        # Step 4: Apply final transformation matrix to the frequency vector
        final_frequencies = [0] * ALPHABET_SIZE
        for src in range(ALPHABET_SIZE):
            for dst in range(ALPHABET_SIZE):
                final_frequencies[dst] = (final_frequencies[dst] + initial_frequencies[src] * final_matrix[src][dst]) % MOD

        # Step 5: Sum all values to get total length
        return sum(final_frequencies) % MOD
