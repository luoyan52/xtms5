from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


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
        contact_ele2 = self.driver.find_element(MobileBy.XPATH,
                                                    "//*[@text='新国都集团开年大吉-2021接力跑挑战赛' and @resource-id ='com.tencent.mm:id/bwa']")
        contact_ele2.click()

        self.driver.tap([330,1400])


