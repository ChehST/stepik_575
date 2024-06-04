# В файл test_items.py напишите тест, который проверяет,
# что страница товара на сайте содержит кнопку добавления в корзину.
# Например, можно проверять товар, доступный по
# http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.

import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
 
def test_basket_button_on_page(browser):
    browser.get(link)
    # criteria 2 need to visual checking the button text
    time.sleep(30)
    item = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert item, f"button '{item.text}' is not found"