from scheduler import Scheduler
from event import Event

scheduler = Scheduler()

n = int(input("Enter Number of Events: "))

for i in range(n):
    print(f"\nEvent {i+1}")
    name = input("Event Name: ")
    start = input("Start Time (HH:MM): ")
    end = input("End Time (HH:MM): ")
    priority = int(input("Priority: "))
    scheduler.add_event(
        Event(f"E{i+1:03}", name, start, end, priority)
    )
scheduler.allocate_rooms()
scheduler.show_schedule()
scheduler.show_rooms()
scheduler.show_waiting_list()