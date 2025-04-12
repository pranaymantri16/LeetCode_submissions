class Solution:
    def countGoodIntegers(self, digit_length: int, k: int) -> int:
        unique_digit_signatures = set()

        def get_digit_signature(counter):
            return tuple(counter.get(str(d), 0) for d in range(10))

        def build_palindrome_sequence(first_half, center_digit=""):
            return "".join(first_half) + center_digit + "".join(reversed(first_half))

        if digit_length == 1:
            for d in range(1, 10):
                if d % k == 0:
                    unique_digit_signatures.add(get_digit_signature(Counter(str(d))))
        else:
            half_size = digit_length // 2
            all_possible_digits = '0123456789'
            half_permutations = product(all_possible_digits, repeat=half_size)

            if digit_length % 2 == 0:
                for half in half_permutations:
                    if half[0] == '0':
                        continue
                    full_palindrome = build_palindrome_sequence(half)
                    if int(full_palindrome) % k == 0:
                        digit_freq_signature = get_digit_signature(Counter(full_palindrome))
                        unique_digit_signatures.add(digit_freq_signature)
            else:
                for half in half_permutations:
                    if half[0] == '0':
                        continue
                    for mid in all_possible_digits:
                        full_palindrome = build_palindrome_sequence(half, mid)
                        if int(full_palindrome) % k == 0:
                            digit_freq_signature = get_digit_signature(Counter(full_palindrome))
                            unique_digit_signatures.add(digit_freq_signature)

        total_good_counts = 0
        for digit_signature in unique_digit_signatures:
            digit_freqs = list(digit_signature)

            total_arrangements = factorial(digit_length)
            for count in digit_freqs:
                total_arrangements //= factorial(count)

            leading_zero_cases = 0
            if digit_freqs[0] > 0:
                reduced_freqs = digit_freqs.copy()
                reduced_freqs[0] -= 1
                leading_zero_cases = factorial(digit_length - 1)
                for count in reduced_freqs:
                    leading_zero_cases //= factorial(count)

            valid_arrangements = total_arrangements - leading_zero_cases
            total_good_counts += valid_arrangements

        return total_good_counts
