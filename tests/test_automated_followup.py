```python
import unittest
from src.automated_followup import AutomatedFollowUp

class TestAutomatedFollowUp(unittest.TestCase):

    def setUp(self):
        self.follow_up = AutomatedFollowUp()

    def test_set_trigger(self):
        trigger_conditions = {"days": 2, "event": "initial_outreach"}
        self.follow_up.set_trigger(trigger_conditions)
        self.assertEqual(self.follow_up.trigger_conditions, trigger_conditions)

    def test_set_follow_up(self):
        follow_up_content = "This is a follow-up email."
        self.follow_up.set_follow_up(follow_up_content)
        self.assertEqual(self.follow_up.follow_up_content, follow_up_content)

    def test_send_follow_up(self):
        user_email = "test@example.com"
        user_password = "password"
        self.follow_up.send_follow_up(user_email, user_password)
        self.assertTrue(self.follow_up.sent)

    def test_update_metrics(self):
        performance_metrics = {"open_rate": 0.5, "click_through_rate": 0.2}
        self.follow_up.update_metrics(performance_metrics)
        self.assertEqual(self.follow_up.performance_metrics, performance_metrics)

if __name__ == '__main__':
    unittest.main()
```