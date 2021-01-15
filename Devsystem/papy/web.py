
from selenium  import  webdriver

def star(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(3)
    self.driver.maximize_window()
    return LoginPage(self.driver)