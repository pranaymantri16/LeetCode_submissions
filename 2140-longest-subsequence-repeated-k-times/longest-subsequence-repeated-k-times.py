class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        from collections import Counter

        n = len(s)
        max_len = 0
        freq = Counter(s)
        has_char = set([c for c in freq if freq[c] >= k])
        if not has_char:
            return ""

        filtered_s = [c for c in s if c in has_char]
        n = len(filtered_s)
        max_len = n // k

        chars = sorted(list(has_char), reverse=True)
        ans = ""

        def can_repeat_k_times(subseq):
            m = len(subseq)
            count = 0
            j = 0
            for c in filtered_s:
                if c == subseq[j]:
                    j += 1
                    if j == m:
                        count += 1
                        j = 0
                if count == k:
                    return True
            return False

        def dfs(current_subseq):
            nonlocal ans
            if len(current_subseq) > max_len:
                return
            if len(current_subseq) > 0 and not can_repeat_k_times(current_subseq):
                return
            if len(current_subseq) > len(ans):
                ans = current_subseq
            for c in chars:
                dfs(current_subseq + c)

        dfs("")
        return ans
