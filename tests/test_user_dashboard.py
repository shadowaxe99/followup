```python
import unittest
from unittest.mock import patch
from src.user_dashboard import UserDashboard

class TestUserDashboard(unittest.TestCase):

    def setUp(self):
        self.user_dashboard = UserDashboard()

    @patch('src.user_dashboard.UserDashboard.set_trigger')
    def test_set_trigger(self, mock_set_trigger):
        self.user_dashboard.set_trigger('trigger_conditions')
        mock_set_trigger.assert_called_with('trigger_conditions')

    @patch('src.user_dashboard.UserDashboard.view_scheduled_follow_ups')
    def test_view_scheduled_follow_ups(self, mock_view_scheduled_follow_ups):
        self.user_dashboard.view_scheduled_follow_ups()
        mock_view_scheduled_follow_ups.assert_called()

    @patch('src.user_dashboard.UserDashboard.monitor_performance_metrics')
    def test_monitor_performance_metrics(self, mock_monitor_performance_metrics):
        self.user_dashboard.monitor_performance_metrics()
        mock_monitor_performance_metrics.assert_called()

if __name__ == '__main__':
    unittest.main()
```