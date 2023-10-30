```python
import json
from src.utils import login, set_trigger, set_follow_up, send_follow_up, update_metrics, get_suggestions

class UserDashboard:
    def __init__(self, user_email, user_password):
        self.user_email = user_email
        self.user_password = user_password
        self.trigger_conditions = {}
        self.follow_up_content = {}
        self.performance_metrics = {}

    def display_dashboard(self):
        print(f"Welcome, {self.user_email}")
        print("1. Set Trigger")
        print("2. Set Follow Up")
        print("3. Send Follow Up")
        print("4. View Performance Metrics")
        print("5. Get AI-Powered Suggestions")
        print("6. Logout")

    def handle_option(self, option):
        if option == 1:
            self.set_trigger()
        elif option == 2:
            self.set_follow_up()
        elif option == 3:
            self.send_follow_up()
        elif option == 4:
            self.view_performance_metrics()
        elif option == 5:
            self.get_ai_powered_suggestions()
        elif option == 6:
            self.logout()
        else:
            print("Invalid option. Please try again.")

    def set_trigger(self):
        trigger_conditions = input("Enter trigger conditions (in JSON format): ")
        self.trigger_conditions = json.loads(trigger_conditions)
        set_trigger(self.trigger_conditions)
        print("Trigger set successfully.")

    def set_follow_up(self):
        follow_up_content = input("Enter follow-up content (in JSON format): ")
        self.follow_up_content = json.loads(follow_up_content)
        set_follow_up(self.follow_up_content)
        print("Follow-up set successfully.")

    def send_follow_up(self):
        send_follow_up(self.user_email, self.user_password, self.trigger_conditions, self.follow_up_content)
        print("Follow-up sent successfully.")

    def view_performance_metrics(self):
        self.performance_metrics = update_metrics(self.user_email, self.user_password)
        print(json.dumps(self.performance_metrics, indent=4))

    def get_ai_powered_suggestions(self):
        suggestions = get_suggestions(self.user_email, self.user_password)
        print(json.dumps(suggestions, indent=4))

    def logout(self):
        print("You have been logged out. Thank you for using our service.")

    def run(self):
        while True:
            self.display_dashboard()
            option = int(input("Enter your option: "))
            self.handle_option(option)
            if option == 6:
                break
```