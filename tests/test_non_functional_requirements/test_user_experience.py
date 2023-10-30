```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestUserExperience(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_form_exists(self):
        self.driver.get("http://localhost:3000")
        assert self.driver.find_element(By.ID, 'login_form')

    def test_dashboard_exists(self):
        self.driver.get("http://localhost:3000/dashboard")
        assert self.driver.find_element(By.ID, 'dashboard')

    def test_trigger_form_exists(self):
        self.driver.get("http://localhost:3000/dashboard")
        assert self.driver.find_element(By.ID, 'trigger_form')

    def test_follow_up_form_exists(self):
        self.driver.get("http://localhost:3000/dashboard")
        assert self.driver.find_element(By.ID, 'follow_up_form')

    def test_metrics_display_exists(self):
        self.driver.get("http://localhost:3000/dashboard")
        assert self.driver.find_element(By.ID, 'metrics_display')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```