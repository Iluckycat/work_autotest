import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import webdriver_manager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
link="https://capsula.mail.ru/smart-home"
obj = driver.get(link)

def get_attributes(driver, element) -> dict:
    return driver.execute_script(
        """
        let attr = arguments[0].attributes;
        let items = {}; 
        for (let i = 0; i < attr.length; i++) {
            items[attr[i].name] = attr[i].value;
        }
        return items;
        """,
        element
    )


item = driver.find_element(By.XPATH, '//*[contains(@class, "sh-filter__group-item-text")]')
item.click()
time.sleep(5)
items = driver.find_element(By.XPATH, '//*[contains(@class,"sh-catalog__products")]')
items_child = items.find_elements(By.CSS_SELECTOR, '*')
for child in items_child:
    name = child.text
    if child.get_attribute('class') == 'sh-product__name' :
        print(name)
time.sleep(10)
