class NumberContainers:
    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = {}
    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.number_to_indices:
                heapq.heappush(self.number_to_indices[old_number], index)
        self.index_to_number[index] = number
        if number not in self.number_to_indices:
            self.number_to_indices[number] = []
        heapq.heappush(self.number_to_indices[number], index)
    def find(self, number: int) -> int:
        if number not in self.number_to_indices or not self.number_to_indices[number]:
            return -1
        while self.number_to_indices[number]:
            smallest_index = self.number_to_indices[number][0]
            if self.index_to_number.get(smallest_index) == number:
                return smallest_index
            heapq.heappop(self.number_to_indices[number])
        return -1