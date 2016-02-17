from selenium import webdriver
import unittest
import sys
import HTMLTestRunner

class Grid2(unittest.TestCase):

    capabilities = None

    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities={
            "browserName": browser,
            "platform":platform,
            "node":port,
            "version":version
        })

    def test_google(self):
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def test_python(self):
        self.driver.get("https://www.python.org/")
        self.assertEqual("Welcome to Python.org", self.driver.title)

    def test_yahoo(self):
        self.driver.get("https://www.yahoo.com/")
        self.assertEqual("Mail", self.driver.find_element_by_link_text("Mail").text)

    def test_stackoverflow(self):
        self.driver.get("http://stackoverflow.com/")
        self.assertEqual("Stack Overflow", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    args = sys.argv
    port,platform,browser,version = args[1:]
    suite = unittest.makeSuite(Grid2)
    report_file = '../report/{0}_{1}_{2}.html'.format(platform,browser,version)
    fp = file(report_file, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="test result",
        description="test report"
    )
    runner.run(suite)


