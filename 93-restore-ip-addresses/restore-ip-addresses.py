class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        R = []
        def backtrack(start: int, path: List[str]):
            if len(path) == 4:
                if start == len(s):
                    R.append('.'.join(path))
                return
            for length in range(1, 4):
                if start + length > len(s):
                    break
                S = s[start:start+length]
                if (S.startswith('0') and len(S) > 1) or int(S) > 255:
                    continue
                backtrack(start + length, path + [S])
        backtrack(0, [])
        return R
