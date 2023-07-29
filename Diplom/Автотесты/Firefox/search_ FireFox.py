from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

link = "http://qa228.karpin74.beget.tech/"
browser = webdriver.Firefox()
browser.maximize_window()
browser.get(link)

search_string = browser.find_element(By.CSS_SELECTOR, "input[class*=header-search-input]")
search_string.send_keys("Шляпы")
knopka = browser.find_element(By.CSS_SELECTOR, "button[class*=header-search-button]").click()
proverka = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*=breadcrumb-heading]"))).text
print(proverka)
proverka1 = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#product-39 > div.summary.entry-summary > h1"))).text
print(proverka1)
assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
browser.quit()