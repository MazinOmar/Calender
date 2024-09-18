import datetime

class Event:
    def __init__(self, title, date_time):
        self.title = title
        self.date_time = date_time

    def __str__(self):
        return f"{self.title} on {self.date_time.strftime('%Y-%m-%d %H:%M')}"

class CalendarApp:
    def __init__(self):
        self.events = []

    def add_event(self):
        title = input("Enter event title: ")
        date_input = input("Enter event date and time (YYYY-MM-DD HH:MM): ")
        try:
            date_time = datetime.datetime.strptime(date_input, '%Y-%m-%d %H:%M')
            event = Event(title, date_time)
            self.events.append(event)
            print("Event added successfully!")
        except ValueError:
            print("Invalid date format. Please try again.")

    def view_events(self):
        if not self.events:
            print("No events scheduled.")
        else:
            print("Scheduled Events:")
            for event in self.events:
                print(event)

    def run(self):
        while True:
            print("\nCalendar Application")
            print("1. Add Event")
            print("2. View Events")
            print("3. Exit")
            choice = input("Select an option: ")
            if choice == '1':
                self.add_event()
            elif choice == '2':
                self.view_events()
            elif choice == '3':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = CalendarApp()
    app.run()
