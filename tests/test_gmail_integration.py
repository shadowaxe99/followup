```python
import unittest
from unittest.mock import patch
from src import gmail_integration

class TestGmailIntegration(unittest.TestCase):

    @patch('src.gmail_integration.login')
    def test_login(self, mock_login):
        mock_login.return_value = True
        result = gmail_integration.login('test@gmail.com', 'password')
        self.assertTrue(result)

    @patch('src.gmail_integration.send_email')
    def test_send_email(self, mock_send_email):
        mock_send_email.return_value = True
        result = gmail_integration.send_email('test@gmail.com', 'receiver@gmail.com', 'subject', 'message')
        self.assertTrue(result)

    @patch('src.gmail_integration.read_email')
    def test_read_email(self, mock_read_email):
        mock_read_email.return_value = 'Test email content'
        result = gmail_integration.read_email('test@gmail.com', 'password')
        self.assertEqual(result, 'Test email content')

    @patch('src.gmail_integration.logout')
    def test_logout(self, mock_logout):
        mock_logout.return_value = True
        result = gmail_integration.logout('test@gmail.com')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```