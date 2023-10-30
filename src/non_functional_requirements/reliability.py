```python
import time
from src.utils import send_follow_up

class Reliability:
    def __init__(self):
        self.start_time = time.time()
        self.total_downtime = 0

    def check_uptime(self):
        current_time = time.time()
        uptime = current_time - self.start_time - self.total_downtime
        uptime_percentage = (uptime / (current_time - self.start_time)) * 100
        return uptime_percentage >= 99.9

    def record_downtime(self, downtime):
        self.total_downtime += downtime

    def handle_downtime(self, downtime):
        self.record_downtime(downtime)
        if not self.check_uptime():
            print("Warning: System uptime has fallen below 99.9%")

    def retry_on_failure(self, function, args, max_retries=3):
        for i in range(max_retries):
            try:
                function(*args)
                break
            except Exception as e:
                if i < max_retries - 1:  # i is zero indexed
                    time.sleep(2)  # wait for 2 seconds before trying again
                else:
                    raise e

reliability = Reliability()

# Example usage:
# reliability.retry_on_failure(send_follow_up, [user_email, follow_up_content])
```