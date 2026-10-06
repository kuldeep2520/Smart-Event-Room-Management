class MinHeap:
    """Min Heap used to find the room that becomes available earliest."""

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

    def _is_smaller(self, room_a, room_b):
        # Greedy order: smallest suitable capacity first.
        # Availability and room ID provide deterministic tie-breakers.
        if room_a.capacity != room_b.capacity:
            return room_a.capacity < room_b.capacity
        if room_a.available_from != room_b.available_from:
            return room_a.available_from < room_b.available_from
        return room_a.room_id < room_b.room_id

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self._is_smaller(self.heap[index], self.heap[parent]):
                self.heap[parent], self.heap[index] = (
                    self.heap[index],
                    self.heap[parent]
                )
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self._is_smaller(
                self.heap[left], self.heap[smallest]
            ):
                smallest = left

            if right < size and self._is_smaller(
                self.heap[right], self.heap[smallest]
            ):
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index]
                )
                index = smallest
            else:
                break
