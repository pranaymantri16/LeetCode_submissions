class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mri = float('inf')
        for i in range(len(blocks) - k + 1):
            w = blocks[i:i + k]
            wc = w.count('W')
            mri = min(mri, wc)
        return mri