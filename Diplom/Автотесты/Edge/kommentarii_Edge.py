from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import random
from faker import Faker
import pytest

fake = Faker(locale="ru_RU")

link = "http://qa228.karpin74.beget.tech/"
browser = webdriver.Edge()
browser.maximize_window()
browser.get(link)

randomMessage = fake.text()
randomName = fake.name()
randomEmail = fake.email()

mag = browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[2]/nav/div[1]/ul/li[1]/a").click() #Переход во вкладку "Магазин"
mag2 = browser.find_element(By.CSS_SELECTOR, "#st-primary-content > div.woocommerce.columns-4 > ul > li:nth-child(2) > a").click() #Выбор категории "Все товары"
mag3 = browser.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div/ul/li[1]/div/div/div[2]/div[1]/h3/a").click() #Выбор товара "Будильники"
reviews = browser.find_element(By.CSS_SELECTOR, "[class*=reviews_tab]").click() #Переключение на вкладку отзывы
star = browser.find_element(By.CSS_SELECTOR, "a[class*=star-5]").click()
feedback_field = browser.find_element(By.CSS_SELECTOR, "#comment")
feedback_field.send_keys(randomMessage)
fieldName = browser.find_element(By.CSS_SELECTOR, "#author")
fieldName.send_keys(randomName)
fieldEmail = browser.find_element(By.CSS_SELECTOR, "#email")
fieldEmail.send_keys(randomEmail)
button = browser.find_element(By.CSS_SELECTOR, "#submit").click()
time.sleep(10)