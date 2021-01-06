from appium.webdriver.common.mobileby import MobileBy

from po.page.base_page import BasePage
from po.page.contact_add_page import ContactAdd


class MemberInviteMenuPage(BasePage):
    """
     添加成员 po
    """
    def add_member_menual(self):
        """
        手动添加成员信息
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return ContactAdd(self.driver)