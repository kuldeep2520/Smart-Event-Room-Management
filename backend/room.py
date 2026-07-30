class Room:

    def __init__(self, room_id, status, end_time):
        self.room_id = room_id
        self.status = status
        self.end_time = end_time
    def display_room(self):
        print(f"Room ID : {self.room_id}")
        print(f"Status : {self.status}")
        print(f"End Time : {self.end_time}")
        print()