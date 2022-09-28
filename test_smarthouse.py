import time
from functions import get_names, is_light
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
link = "https://capsula.mail.ru/smart-home"
obj = driver.get(link)
def test_light_filter():
    item = driver.find_element(By.XPATH, '//*[contains(@class, "sh-filter__group-item-text")]')
    item.click()
    time.sleep(5)
    items = driver.find_element(By.XPATH, '//*[contains(@class,"sh-catalog__products")]')
    items_child = items.find_elements(By.CSS_SELECTOR, '*')
    names = get_names(items_child)
    is_lght = is_light(names)
    assert is_lght == True

