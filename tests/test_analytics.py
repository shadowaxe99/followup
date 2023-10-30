```python
import unittest
from src import analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        self.user_email = "testuser@gmail.com"
        self.user_password = "testpassword"
        self.analytics = analytics.Analytics(self.user_email, self.user_password)

    def test_update_metrics(self):
        self.analytics.update_metrics()
        self.assertIsNotNone(self.analytics.performance_metrics)

    def test_get_open_rate(self):
        open_rate = self.analytics.get_open_rate()
        self.assertIsInstance(open_rate, float)

    def test_get_click_through_rate(self):
        click_through_rate = self.analytics.get_click_through_rate()
        self.assertIsInstance(click_through_rate, float)

if __name__ == '__main__':
    unittest.main()
```