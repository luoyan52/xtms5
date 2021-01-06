from po.page.base_page import BasePage
from po.page.memaber_invite_menu_page import MemberInviteMenuPage


class AddresssListPage(BasePage):
    def click_addmember(self):
        """
        添加成员
        :return:
        """
        self.scroll_find_click("添加成员")
        print("点击添加成员")
        return MemberInviteMenuPage(self.driver)