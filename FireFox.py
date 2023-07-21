import pytest
import time
from faker import Faker

fake = Faker()
import selenium
from selenium.webdriver.common.by import By

browser = selenium.webdriver.Firefox()
browser.get('https://webtucre.ru/testovaya-stranicza-2/')
time.sleep(1)

randomName = fake.name()
randomEmail = fake.email()
randomMessage = fake.text()

fieldName = browser.find_element(By.NAME, "form_fields[name]")
fieldEmail = browser.find_element(By.NAME, "form_fields[email]")
fieldMessage = browser.find_element(By.NAME, "form_fields[message]")
button = browser.find_element(By.XPATH,
                              "/html/body/div/div[2]/div/div[1]/main/article/div/div/div/section[2]/div/div/div/section/div/div[2]/div/div/div/form/div/div[4]/button")

fieldName.send_keys(randomName)
time.sleep(1)
fieldEmail.send_keys(randomEmail)
time.sleep(1)
fieldMessage.send_keys(randomMessage)
time.sleep(1)
button.click()
time.sleep(3)

response = browser.find_element(By.CLASS_NAME, 'elementor-message')


def test():
    assert response == browser.find_element(By.CLASS_NAME, 'elementor-message-success')


if __name__ == '__main__':
    pytest.main()