# В файл test_items.py напишите тест, который проверяет,
# что страница товара на сайте содержит кнопку добавления в корзину.
# Например, можно проверять товар, доступный по
# http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.

import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

languages = {
    'es':'Añadir al carrito',
    'fr':'Ajouter au panier',
    'ru':'Добавить в корзину',
    'de':'In Warenkorb legen',
    'en-gb':'Add to basket'

}
 
def test_basket_button(browser):
    browser.get(link)
    # criteria 2
    # time.sleep(30)
    item = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    print(item)
    assert item, "button 'Add to basket' is not found"