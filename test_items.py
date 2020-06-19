from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # Проверка локатора кнопки "Add to basket"
    try:
        browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
        bt = True
    except:
        bt = False
    assert bt, 'Button "Add to basket" not found!'

    # Простое решение проверки локатора кнопки "Add to basket", падает при плохом селекторе.
    # button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary btn-add-to-basket"]')))
    # assert button, 'Button "Add to basket" not found!'
