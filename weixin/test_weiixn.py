from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import time


class TestDemo1:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "H8BUT20312003886 "
        caps["appPackage"] = "com.tencent.mm"
        caps["appActivity"] = ".ui.LauncherUI"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)



    def test_contact(self):
            # xpath
        contact_ele = self.driver.find_element(MobileBy.XPATH,
                                                   "//*[@text='我' and @resource-id ='com.tencent.mm:id/cns']")
        contact_ele.click()

        contact_ele2 = self.driver.find_element(MobileBy.XPATH,
                                                   "//*[@text='收藏' and @resource-id ='android:id/title']")
        contact_ele2.click()
        self.driver.implicitly_wait(20)
        contact_ele2 = self.driver.find_element(MobileBy.XPATH,
                                                    "//*[@text='新国都集团开年大吉-2021接力跑挑战赛' and @resource-id ='com.tencent.mm:id/bwa']")
        contact_ele2.click()

        time.sleep(5)
        action0 = TouchAction(self.driver).tap(x = 515, y =1419)
        action0.perform()
        self.driver.implicitly_wait(10)
        var = 1
        while var == 1:
            action1 = TouchAction(self.driver)
            action2 = TouchAction(self.driver)
            mul_action =MultiAction(self.driver)
            action2.tap(x=226, y=1677)
            action2.tap(x=824, y=1707)
            mul_action.add(action1,action2)
            mul_action.perform()




