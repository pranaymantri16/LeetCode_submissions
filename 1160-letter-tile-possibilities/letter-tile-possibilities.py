class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            t = 0
            for tile in counter:
                if counter[tile] > 0:
                    counter[tile] -= 1
                    t += 1 + backtrack(counter)
                    counter[tile] += 1
            return t
        return backtrack(Counter(tiles))