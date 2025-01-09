from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        top_element = self.queue.popleft()
        self.queue.append(top_element)
        return top_element

    def empty(self) -> bool:
        return not self.queue
