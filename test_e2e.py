import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestMaxAreaContainerApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://127.0.0.1:5000/")

    def test_valid_input(self):
        driver = self.driver
        heights_input = driver.find_element(By.ID, "heights")
        heights_input.send_keys("1,8,6,2,5,4,8,3,7")
        heights_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Allow time for page to load
        result = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("Result: 49", result)

    def test_min_constraints(self):
        driver = self.driver
        heights_input = driver.find_element(By.ID, "heights")
        heights_input.send_keys("1,2")
        heights_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Allow time for page to load
        result = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("Result: 1", result)

    def test_max_constraints(self):
        driver = self.driver
        heights_input = driver.find_element(By.ID, "heights")
        heights_input.send_keys(",".join(["10000"] * 100000))
        heights_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Allow time for page to load
        result = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("Result: 999990000", result)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
