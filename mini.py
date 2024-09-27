class VisitorExperience:
    def __init__(self):
        self.events = [
            {"name": "1. CSK vs RCB", "date": "2024-09-30", "time": "7:00 pm"},
            {"name": "2. SRH vs GT", "date": "2024-10-05", "time": "3:00 pm"},
            {"name": "3. MI vs KKR", "date": "2024-10-10", "time": "6:00 pm"},
            {"name": "4. RR vs DC", "date": "2024-10-17", "time": "7:00 pm"}
        ]
        self.feedback = []
        self.booked_ticket = None

    def display_events(self):
        print("Upcoming Events:")
        for event in self.events:
            print(f"{event['name']} on {event['date']} at {event['time']}")

    def book_ticket(self):
        print("Enter your details")
        name = input("Name: ")
        contact = input("Contact number: ")
        email = input("Email: ")
        
        self.display_events()
        event_choice = input("Enter event number (1-4): ")
        
        if event_choice in ['2', '3']:
            print("Ticket cost: ₹1499")
            opinion = input("Do you want to book? (Yes/No): ").strip().lower()
            if opinion == 'yes':
                self.booked_ticket = {"name": name, "contact": contact, "email": email, "event": self.events[int(event_choice) - 1]}
                print("Thank you for booking the ticket!")
                print("Enjoy the Event!!")
            else:
                print("Thank you for using the app.")
        elif event_choice == '1':
            print("Tickets are not available.")
        elif event_choice == '4':
            print("Your booking is pending.")
        else:
            print("Invalid input.")

    def view_ticket(self):
        if self.booked_ticket:
            print(f"Ticket booked in the name of {self.booked_ticket['name']} for the event {self.booked_ticket['event']['name']}.")
        else:
            print("No tickets booked yet.")

    def give_feedback(self):
        feedback = input("Please enter your feedback: ")
        self.feedback.append(feedback)
        print("Thank you for your feedback!")

    def ticket_cancellation(self):
        name = input("Enter your name to cancel the ticket: ")
        if self.booked_ticket and self.booked_ticket['name'] == name:
            self.booked_ticket = None
            print("Your ticket has been cancelled.")
        else:
            print("Invalid booking or no ticket booked.")

    def start(self):
        while True:
            print("\nWelcome to the Stadium Visitor Experience App!")
            print("1. View Upcoming Events")
            print("2. Book Ticket")
            print("3. View Booked Ticket")
            print("4. Leave Feedback")
            print("5. Ticket Cancellation")
            print("6. Exit")
            choice = input("Select an option (1-6): ")

            if choice == '1':
                self.display_events()
            elif choice == '2':
                self.book_ticket()
            elif choice == '3':
                self.view_ticket()
            elif choice == '4':
                self.give_feedback()
            elif choice == '5':
                self.ticket_cancellation()
            elif choice == '6':
                print("Thank you for using the app. Have a nice day!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = VisitorExperience()
    app.start()
