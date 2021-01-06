from po.page.app import App
from po.page.main_page import MainPage


def test_add_member():
    app = App()
    app.start()
    result= app.goto_address().click_addmember().add_member_menual().add_contact()
    assert result