class MinHeap:

    def __init__(self):
        self.heap = []
    def is_empty(self):
        return len(self.heap) == 0
    def insert(self, room):
        self.heap.append(room)
        self._heapify_up(len(self.heap) - 1)
    def remove_min(self):
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_room = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_room
    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent].end_time > self.heap[index].end_time:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break
    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
            
            if left < size and self.heap[left].end_time < self.heap[smallest].end_time:
                smallest = left
            if right < size and self.heap[right].end_time < self.heap[smallest].end_time:
                smallest = right
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break