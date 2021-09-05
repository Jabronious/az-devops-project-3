# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime

chrome_options = ChromeOptions()
chrome_options.add_argument("--headless")

DRIVER = webdriver.Chrome(options=chrome_options)
# Start the browser and login with standard_user
def login (user, password):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tStarting the browser...')
    DRIVER.get('https://www.saucedemo.com/')
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tBrowser started successfully. Navigating to the demo page to login.')

    DRIVER.find_element_by_id('user-name').send_keys(user)
    DRIVER.find_element_by_id('password').send_keys(password)
    DRIVER.find_element_by_id('login-button').click()

    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\t%s logged in' % user)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tAsserting PRODUCTS is the page title')
    # .upper ensures the case will be matched in the event that the website decides to change the title formatting
    assert 'PRODUCTS'.upper() in DRIVER.find_element_by_class_name('title').text.upper()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tAssertion passed.')

def add_cart():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tAsserting items were added to cart')
    assert str(click_btns()) in DRIVER.find_element_by_class_name('shopping_cart_badge').text
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tAssertion passed.')

def remove_cart():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tAsserting back pack was removed from cart')
    click_btns()
    assert not len(DRIVER.find_elements_by_class_name('shopping_cart_badge'))
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tAssertion passed.')

def click_btns():
    inventoryBtns = DRIVER.find_elements_by_class_name('btn_inventory')
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\tClicking all the buttons...')
    for btn in inventoryBtns:
        btn.click()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\t%d items clicked' % len(inventoryBtns))
    return len(inventoryBtns)

login('standard_user', 'secret_sauce')
add_cart()
remove_cart()

DRIVER.quit()