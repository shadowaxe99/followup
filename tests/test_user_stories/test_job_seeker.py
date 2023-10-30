```python
import unittest
from src.automated_followup import AutomatedFollowUp
from src.user_stories.job_seeker import JobSeeker

class TestJobSeeker(unittest.TestCase):
    def setUp(self):
        self.job_seeker = JobSeeker("jobseeker@gmail.com", "password123")
        self.follow_up = AutomatedFollowUp(self.job_seeker.user_email, self.job_seeker.user_password)

    def test_send_follow_up(self):
        self.follow_up.set_trigger({"days_after": 7})
        self.follow_up.set_follow_up("Thank you for considering my application. I am looking forward to hearing from you.")
        self.assertTrue(self.follow_up.send_follow_up())

    def test_personalization(self):
        self.follow_up.set_trigger({"days_after": 7})
        self.follow_up.set_follow_up("Thank you for considering my application. I am looking forward to hearing from you.")
        self.assertEqual(self.follow_up.follow_up_content, "Thank you for considering my application. I am looking forward to hearing from you.")

    def test_trigger_conditions(self):
        self.follow_up.set_trigger({"days_after": 7})
        self.assertEqual(self.follow_up.trigger_conditions, {"days_after": 7})

if __name__ == '__main__':
    unittest.main()
```