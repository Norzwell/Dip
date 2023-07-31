from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from faker import Faker
fake = Faker(locale="ru_RU")

link = "http://qa228.karpin74.beget.tech/"
browser = webdriver.Edge()
browser.maximize_window()
browser.get(link)

randomName = fake.name()
a = randomName.split()
name = a[0]
last_name = a[1]

randomAddress = fake.address()
b = randomAddress.split()
home = b[2:6]
oblast = b[0:2]
index = b[-1]

phone = fake.phone_number()

randomMessage = fake.text()
randomEmail = fake.email()

mag = browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[2]/nav/div[1]/ul/li[1]/a").click() #Переход во вкладку "Магазин"
mag2 = browser.find_element(By.CSS_SELECTOR, "#st-primary-content > div.woocommerce.columns-4 > ul > li:nth-child(2) > a").click() #Выбор категории "Все товары"
mag3 = browser.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div/ul/li[1]/div/div/div[2]/div[1]/h3/a").click() #Выбор товара "Будильники"
quantity = browser.find_element(By.XPATH, "//div[@id='product-36']/div[2]/form/div/input").clear() # Очистка значения по умолчанию
quantity = browser.find_element(By.XPATH, "//div[@id='product-36']/div[2]/form/div/input").send_keys("5") # Указание количесва товаров
product = browser.find_element(By.XPATH, "//*[@id='product-36']/div[2]/form/button").click() # Клик на кнопку "В корзину"
product = browser.find_element(By.CSS_SELECTOR, "#main-header6 > div.navigation-wrapper > div.navigation-middle > div > div > div > div > div.main-menu-right.col-lg-4 > ul > li.cart-wrapper > div.cart-main > button").click() #Открытие модального окна корзины
time.sleep(2)
product = browser.find_element(By.XPATH, "/html/body/div/header/div[2]/div[1]/div/div/div/div/div[3]/ul/li[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]").click() #Переход по вкладке "Посомтреть корзину"

making = browser.find_element(By.CSS_SELECTOR, "#st-primary-content > div > div.cart-collaterals > div > div > a").click()

fieldName = browser.find_element(By.CSS_SELECTOR, "#billing_first_name")
fieldName.send_keys(name)

fieldLastName = browser.find_element(By.CSS_SELECTOR, "#billing_last_name")
fieldLastName.send_keys(last_name)

fielHome = browser.find_element(By.XPATH, "/html/body/div/div[3]/section/div/div/div/div/form[2]/div[1]/div[1]/div/div/p[5]/span/input")
fielHome.send_keys(home)

fielOblast = browser.find_element(By.XPATH, "/html/body/div/div[3]/section/div/div/div/div/form[2]/div[1]/div[1]/div/div/p[7]/span/input")
fielOblast.send_keys(oblast)

fielOblast1 = browser.find_element(By.XPATH, "/html/body/div/div[3]/section/div/div/div/div/form[2]/div[1]/div[1]/div/div/p[8]/span/input")
fielOblast1.send_keys(oblast)

fielIndex = browser.find_element(By.XPATH, "/html/body/div/div[3]/section/div/div/div/div/form[2]/div[1]/div[1]/div/div/p[9]/span/input")
fielIndex.send_keys(index)

fielPhone = browser.find_element(By.XPATH, "/html/body/div/div[3]/section/div/div/div/div/form[2]/div[1]/div[1]/div/div/p[10]/span/input")
fielPhone.send_keys(phone)

fieldEmail = browser.find_element(By.XPATH, "/html/body/div/div[3]/section/div/div/div/div/form[2]/div[1]/div[1]/div/div/p[11]/span/input")
fieldEmail.send_keys(randomEmail)

making_an_order = browser.find_element(By.CSS_SELECTOR, "#place_order").click()
