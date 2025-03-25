class Solution(object):
    def checkValidCuts(self, n, rectangles):
        return self.isValidCut(rectangles, 0, 0, 2) or self.isValidCut(rectangles, 1, 1, 3)
    def isValidCut(self, rectangles, sort_index, start, end):
        rectangles.sort(key=lambda x: x[sort_index])
        A = rectangles[0][start]
        B = rectangles[0][end]
        i = 0
        for rect in rectangles:
            if rect[start] < B:
                B = max(rect[end], B)
            else:
                i += 1
                A = rect[start]
                B = rect[end]
        i += 1
        return i > 2