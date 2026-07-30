class MaxHeap:
    def __init__(self):
        self.heap=[]
    def is_empty(self):
        return len(self.heap)==0
    def insert(self, event):
        self.heap.append(event)
        self._heapify_up(len(self.heap) - 1)
    def remove_max(self):
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_event = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_event
    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent].priority < self.heap[index].priority:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break
    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break