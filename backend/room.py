class Room:
    def __init__(self, room_id, name, capacity, status="Free", event="-", available_from=0):
        self.room_id = room_id
        self.name = name
        self.capacity = capacity
        self.status = status
        self.event = event
        # Time (in minutes) from which the room is available again.
        self.available_from = available_from

    def __str__(self):
        return (
            f"{self.room_id} | "
            f"{self.name} | "
            f"Capacity: {self.capacity} | "
            f"Status: {self.status} | "
            f"Available From: {self.available_from}"
        )
