class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        vowel_freq = {}
        consonant_count = 0
        left = 0
        extra_left = 0
        total_count = 0
        vowel_types = 0
        for right, char in enumerate(word):
            if char in vowel_set:
                vowel_freq[char] = vowel_freq.get(char, 0) + 1
                if vowel_freq[char] == 1:
                    vowel_types += 1
            else:
                consonant_count += 1
            while consonant_count > k:
                left_char = word[left]
                if left_char in vowel_set:
                    vowel_freq[left_char] -= 1
                    if vowel_freq[left_char] == 0:
                        vowel_types -= 1
                else:
                    consonant_count -= 1
                left += 1
                extra_left = 0
            while vowel_types == 5 and consonant_count == k and left < right and word[left] in vowel_set and vowel_freq[word[left]] > 1:
                extra_left += 1
                vowel_freq[word[left]] -= 1
                left += 1
            if vowel_types == 5 and consonant_count == k:
                total_count += (1 + extra_left)
        return total_count