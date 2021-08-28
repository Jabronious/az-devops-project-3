# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

DRIVER = webdriver.Chrome()
# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    # options = ChromeOptions()
    # options.add_argument("--headless") 
    # DRIVER = webdriver.Chrome(options=options)
    print ('Browser started successfully. Navigating to the demo page to login.')
    DRIVER.get('https://www.saucedemo.com/')

    DRIVER.find_element_by_id('user-name').send_keys(user)
    DRIVER.find_element_by_id('password').send_keys(password)
    DRIVER.find_element_by_id('login-button').click()

    print ('Asserting PRODUCTS is the page title')
    # .upper ensures the case will be matched in the event that the website decides to change the title formatting
    assert 'PRODUCTS'.upper() in DRIVER.find_element_by_class_name('title').text.upper()
    print ('Assertion passed.')

def add_cart():
    print('adding back pack...')
    DRIVER.find_element_by_id('add-to-cart-sauce-labs-backpack').click()
    print ('Asserting back pack was added to cart')
    assert '1' in DRIVER.find_element_by_class_name('shopping_cart_badge').text
    print ('Assertion passed.')

def remove_cart():
    print('removing back pack...')
    DRIVER.find_element_by_id('remove-sauce-labs-backpack').click()
    print ('Asserting back pack was removed from cart')
    assert not len(DRIVER.find_elements_by_class_name('shopping_cart_badge'))
    print ('Assertion passed.')

login('standard_user', 'secret_sauce')
add_cart()
remove_cart()

DRIVER.quit()