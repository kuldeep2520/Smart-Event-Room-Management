from scheduler import Scheduler
from event import Event


def get_time(prompt):
    while True:
        value = input(prompt).strip()
        try:
            h, m = map(int, value.split(":"))
            if 0 <= h <= 23 and 0 <= m <= 59:
                return f"{h:02d}:{m:02d}"
            print("Invalid time. Use 00:00 to 23:59.")
        except ValueError:
            print("Invalid time. Please use HH:MM format.")


def get_priority():
    while True:
        try:
            value = int(input("Priority (1-10): "))
            if 1 <= value <= 10:
                return value
            print("Priority must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Value must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    scheduler = Scheduler()

    print("========================================")
    print("   SMART EVENT ROOM MANAGEMENT SYSTEM")
    print("========================================")

    n = get_positive_integer("Enter Number of Events: ")

    for i in range(n):
        print(f"\nEvent {i + 1}")
        print("----------")

        name = input("Event Name: ").strip()
        while not name:
            print("Event name cannot be empty.")
            name = input("Event Name: ").strip()

        start = get_time("Start Time (HH:MM): ")
        end = get_time("End Time (HH:MM): ")

        start_minutes = scheduler.time_to_minutes(start)
        end_minutes = scheduler.time_to_minutes(end)

        if end_minutes <= start_minutes:
            print("End time must be after start time. Please enter the event again.")
            end = get_time("End Time (HH:MM): ")
            while scheduler.time_to_minutes(end) <= start_minutes:
                print("End time must be after start time.")
                end = get_time("End Time (HH:MM): ")

        priority = get_priority()
        participants = get_positive_integer("Number of Participants: ")

        event = Event(
            f"E{i + 1:03}",
            name,
            start,
            end,
            priority,
            participants
        )

        scheduler.add_event(event)

    scheduler.allocate_rooms()

    scheduler.display_schedule()
    scheduler.display_rooms()
    scheduler.display_waiting_list()


if __name__ == "__main__":
    main()
