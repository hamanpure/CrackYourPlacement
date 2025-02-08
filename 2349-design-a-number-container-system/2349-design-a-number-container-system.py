from heapq import heapify, heappush, heappop
class NumberContainers:

    def __init__(self):
        self.container = {}
        self.c = defaultdict(list)

    def change(self, index: int, number: int) -> None:     
        if index in self.container:
            old_number = self.container[index]
            if old_number != number:
                heappush(self.c[number], index)  # Push new index into the correct heap
        else:
            heappush(self.c[number], index)  # Add index to heap for the number

        # Update the mapping
        self.container[index] = number

    def find(self, number: int) -> int:
        if number not in self.c:
            return -1
        while self.c[number] and self.container.get(self.c[number][0]) != number:
            heappop(self.c[number])

        return self.c[number][0] if self.c[number] else -1       


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)