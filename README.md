# Smart Event Room Management System

A Python-based event room scheduling system using **Max Heap, Min Heap, Greedy Algorithm, room capacity constraints, time-conflict checking, and a waiting list**.

## Features

- 20 predefined rooms (`R001` to `R020`)
- Room name and capacity for every room
- Event ID, name, start/end time, priority, and participants
- **Max Heap**: processes higher-priority events first
- **Min Heap**: selects the minimum-capacity suitable room
- **Greedy Algorithm**: chooses the smallest room that can accommodate all participants
- Prevents overlapping bookings in the same room
- Reuses a room after its previous event ends
- Waiting list when no suitable room is available
- Waiting-list retry after the main allocation pass
- Input validation for time, priority, and participant count
- Schedule, room status, and waiting-list reports

## Project Structure

```text
Smart-Event-Room-Management/
├── backend/
│   ├── event.py
│   ├── room.py
│   ├── max_heap.py
│   ├── min_heap.py
│   ├── scheduler.py
│   └── main.py
└── README.md
```

## Run

Open Terminal in the `backend` directory:

```bash
python3 main.py
```

Use time in 24-hour `HH:MM` format, for example `14:00`.

## Allocation Logic

```text
Event Input
    ↓
Max Heap (highest priority first)
    ↓
Check time + participant capacity
    ↓
Min Heap of suitable rooms
    ↓
Greedy: smallest suitable room
    ↓
Allocate room
    ↓
No suitable room → Waiting List
```

## Example

For an event with **45 participants**, the system can choose:

- Training Room — 50 seats
- Workshop Room — 60 seats
- Lecture Hall — 70 seats

The greedy rule chooses the **50-seat Training Room** because it is the smallest suitable room.

## Presentation Points

- **Max Heap:** priority-based event processing.
- **Min Heap:** efficient minimum-room selection.
- **Greedy:** avoid wasting large rooms on small events.
- **Time conflict detection:** a room is reusable only when its previous event has ended.
- **Waiting list:** handles events for which no suitable room is currently available.
