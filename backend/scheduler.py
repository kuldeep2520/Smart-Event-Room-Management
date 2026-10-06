from room import Room
from max_heap import MaxHeap
from min_heap import MinHeap


class Scheduler:

    def __init__(self):
        self.event_heap = MaxHeap()
        self.rooms = []
        self.waiting_list = []
        self.schedule = []

        room_data = [
            ("R001", "Conference Hall", 100),
            ("R002", "Seminar Hall", 80),
            ("R003", "Meeting Room A", 30),
            ("R004", "Meeting Room B", 30),
            ("R005", "Training Room", 50),
            ("R006", "Computer Lab", 40),
            ("R007", "Workshop Room", 60),
            ("R008", "Board Room", 20),
            ("R009", "Lecture Hall A", 70),
            ("R010", "Lecture Hall B", 70),
            ("R011", "Innovation Room", 35),
            ("R012", "Discussion Room A", 25),
            ("R013", "Discussion Room B", 25),
            ("R014", "Presentation Room", 45),
            ("R015", "Auditorium", 150),
            ("R016", "Faculty Meeting Room", 20),
            ("R017", "Interview Room A", 10),
            ("R018", "Interview Room B", 10),
            ("R019", "Small Meeting Room", 15),
            ("R020", "Multipurpose Hall", 120)
        ]

        for room_id, name, capacity in room_data:
            self.rooms.append(Room(room_id, name, capacity))

    def add_event(self, event):
        self.event_heap.insert(event)

    def time_to_minutes(self, t):
        try:
            h, m = map(int, t.strip().split(":"))
        except (ValueError, AttributeError):
            raise ValueError("Time must be in HH:MM format.")

        if h < 0 or h > 23 or m < 0 or m > 59:
            raise ValueError("Time must be in 00:00 to 23:59 format.")

        return h * 60 + m

    def _find_room(self, event_start, event_end, participants):
        """Use Min Heap + Greedy selection to find the best free room."""
        room_heap = MinHeap()

        for room in self.rooms:
            if (
                room.capacity >= participants
                and room.available_from <= event_start
            ):
                room_heap.insert(room)

        if room_heap.is_empty():
            return None

        return room_heap.remove_min()

    def allocate_rooms(self):
        """Allocate highest-priority events without room time conflicts."""
        while not self.event_heap.is_empty():
            event = self.event_heap.remove_max()

            event_start = self.time_to_minutes(event.start_time)
            event_end = self.time_to_minutes(event.end_time)

            if event_end <= event_start:
                self.waiting_list.append(event)
                print("\nEvent Added to Waiting List")
                print("---------------------------")
                print("Event ID    :", event.event_id)
                print("Event Name  :", event.event_name)
                print("Reason      : End time must be after start time")
                continue

            if event.participants <= 0:
                self.waiting_list.append(event)
                print("\nEvent Added to Waiting List")
                print("---------------------------")
                print("Event ID    :", event.event_id)
                print("Event Name  :", event.event_name)
                print("Reason      : Participants must be greater than 0")
                continue

            room = self._find_room(
                event_start,
                event_end,
                event.participants
            )

            if room is None:
                self.waiting_list.append(event)
                print("\nEvent Added to Waiting List")
                print("---------------------------")
                print("Event ID    :", event.event_id)
                print("Event Name  :", event.event_name)
                print("Priority    :", event.priority)
                print("Participants:", event.participants)
                print("Reason      : No suitable room available for this time")
                continue

            room.status = "Occupied"
            room.event = event.event_name
            room.available_from = event_end

            self.schedule.append((event, room))

            print("\nEvent Allocated Successfully")
            print("----------------------------")
            print("Event ID    :", event.event_id)
            print("Event Name  :", event.event_name)
            print("Priority    :", event.priority)
            print("Participants:", event.participants)
            print("Room ID     :", room.room_id)
            print("Room Name   :", room.name)
            print("Capacity    :", room.capacity)
            print("Time        :", event.start_time, "-", event.end_time)

        self._try_waiting_events()

    def _try_waiting_events(self):
        """Retry waiting events in priority order after allocations."""
        if not self.waiting_list:
            return

        remaining = sorted(
            self.waiting_list,
            key=lambda event: (-event.priority, event.event_id)
        )
        self.waiting_list = []

        changed = True
        while remaining and changed:
            changed = False
            still_waiting = []

            for event in remaining:
                start = self.time_to_minutes(event.start_time)
                end = self.time_to_minutes(event.end_time)

                room = self._find_room(start, end, event.participants)

                if room is None:
                    still_waiting.append(event)
                    continue

                room.status = "Occupied"
                room.event = event.event_name
                room.available_from = end
                self.schedule.append((event, room))
                changed = True

                print("\nWaiting Event Allocated")
                print("-----------------------")
                print("Event ID    :", event.event_id)
                print("Event Name  :", event.event_name)
                print("Priority    :", event.priority)
                print("Participants:", event.participants)
                print("Room ID     :", room.room_id)
                print("Room Name   :", room.name)
                print("Capacity    :", room.capacity)
                print("Time        :", event.start_time, "-", event.end_time)

            remaining = still_waiting

        self.waiting_list.extend(remaining)

    def display_rooms(self):
        print("\n========== ROOM DETAILS ==========")

        for room in self.rooms:
            available_time = f"{room.available_from // 60:02d}:{room.available_from % 60:02d}"

            print(
                f"{room.room_id} | "
                f"{room.name} | "
                f"Capacity: {room.capacity} | "
                f"Status: {room.status} | "
                f"Event: {room.event} | "
                f"Available From: {available_time}"
            )

    def display_waiting_list(self):
        print("\n========== WAITING LIST ==========")

        if not self.waiting_list:
            print("No events in waiting list.")
            return

        for event in sorted(
            self.waiting_list,
            key=lambda e: (-e.priority, e.event_id)
        ):
            print(
                f"Event ID: {event.event_id} | "
                f"Event: {event.event_name} | "
                f"Participants: {event.participants} | "
                f"Priority: {event.priority}"
            )

    def display_schedule(self):
        print("\n========== SCHEDULE ==========")

        if not self.schedule:
            print("No events scheduled.")
            return

        for event, room in sorted(
            self.schedule,
            key=lambda item: self.time_to_minutes(item[0].start_time)
        ):
            print(
                f"Event: {event.event_name} | "
                f"Room: {room.room_id} - {room.name} | "
                f"Capacity: {room.capacity} | "
                f"Participants: {event.participants} | "
                f"Priority: {event.priority} | "
                f"Time: {event.start_time}-{event.end_time}"
            )
