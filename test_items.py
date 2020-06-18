import time

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"#.format(language)
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
    time.sleep(5)