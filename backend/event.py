class Event:
    def __init__(self,event_id,event_name,start_time,end_time,priority,participants):
        self.event_id = event_id
        self.event_name = event_name
        self.start_time = start_time
        self.end_time = end_time
        self.priority = priority 
        self.participants = participants   
    def display_event(self):
        print("Event ID :",self.event_id)
        print("Event Name :",self.event_name)
        print("Start Time :",self.start_time)
        print("End Time :",self.end_time)
        print("Priority :",self.priority)
        print("participants :",self.participants)