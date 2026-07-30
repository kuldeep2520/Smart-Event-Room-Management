from room import Room
from max_heap import MaxHeap
class Scheduler:
    def __init__(self):
        self.event_heap = MaxHeap()
        self.rooms = []
        self.waiting_list = []
        self.schedule = []
        for i in range(1, 21):
            self.rooms.append(Room(f"R{i:03}", "Free", "-"))
    def add_event(self, event):
        self.event_heap.insert(event)

    def time_to_minutes(self, t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    def allocate_rooms(self):
        while not self.event_heap.is_empty():
            event = self.event_heap.remove_max()
            allocated = False
            event_start = self.time_to_minutes(event.start_time)
            for room in self.rooms:
                if room.status == "Free":
                    room.status = "Occupied"
                    room.end_time = event.end_time
                    self.schedule.append((event, room))
                    allocated = True
                    break
                if self.time_to_minutes(room.end_time) <= event_start:
                    room.end_time = event.end_time
                    self.schedule.append((event, room))
                    allocated = True
                    break
            if not allocated:
                self.waiting_list.append(event)
    def show_schedule(self):
        print("\n==========SCHEDULE==========")
        for event, room in self.schedule:
            print(
                f"{event.event_name} ({event.start_time}-{event.end_time}) --> {room.room_id}"
            )
    def show_waiting_list(self):
        print("\n==========WAITING LIST==========")
        if not self.waiting_list:
            print("Empty")
        else:
            for event in self.waiting_list:
                print(event.event_name)
    def show_rooms(self):
        print("\n==========ROOMS==========")
        for room in self.rooms:
            room.display_room()