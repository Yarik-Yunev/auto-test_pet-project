from pages.base_page import BasePage
import time

def test(browser):
    page = BasePage(browser, 'google.com')
    page.open()
    time.sleep(3)