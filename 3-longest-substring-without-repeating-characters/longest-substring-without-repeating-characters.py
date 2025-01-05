class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_start = 0
        max_length = 0
        char_index_map = {}

        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= substring_start:
                substring_start = char_index_map[char] + 1

            char_index_map[char] = i
            current_length = i - substring_start + 1
            max_length = max(max_length, current_length)

        return max_length