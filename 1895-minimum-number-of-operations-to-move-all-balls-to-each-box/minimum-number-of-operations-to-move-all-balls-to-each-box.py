class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        left_sum = 0
        right_sum = 0
        left_cost = 0
        right_cost = 0
        for i in range(n):
            if boxes[i] == '1':
                right_sum += 1
                right_cost += i
        for i in range(n):
            answer[i] = left_cost + right_cost
            if boxes[i] == '1':
                left_sum += 1
                right_sum -= 1
            left_cost += left_sum
            right_cost -= right_sum

        return answer