from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from auth import vk_password, vk_phone
import pickle

# Создаем объект options
options = webdriver.ChromeOptions()

# options.add_argument("user-agent=Apple Safari 5.1 (Win 8 x64): Mozilla/5.0 (Windows NT 6.2; WOW64) "
#                      "AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2")

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

s = Service("D:\\PROJECTI\\Selenium\\chromedriver.exe")
# r"D:\PROJECTI\Selenium\chromedriver.exe"

driver = webdriver.Chrome(service=s,
                          options=options
                          )

try:
    # driver.get("https://vk.com/")
    # time.sleep(5)

    # email_input = driver.find_element(By.ID, "index_email")
    # email_input.clear()
    # email_input.send_keys(vk_phone)
    # time.sleep(3)

    # login_button = driver.find_element(By.XPATH, '//button[@class="FlatButton FlatButton--primary FlatButton--size-l '
    #                                              'FlatButton--wide VkIdForm__button VkIdForm__signInButton"]')
    # login_button.click()
    # time.sleep(3)

    # password_input = driver.find_element(By.ID, "index_pass")
    # password_input.clear()
    # password_input = driver.find_element(By.NAME, "password")
    # password_input.clear()

    # password_input.send_keys(vk_password)
    # time.sleep(3)
    # 1 способ авторизации, находясь в окне ввода пароля, стимулируем нажатие клавиши ENTER
    # password_input.send_keys(Keys.ENTER)
    # time.sleep(5)
    # 2 способ авторизации, нажимаем на саму кнопку
    # login_button = driver.find_element(By.ID, "index_login_button").click()
    # time.sleep(10)

    # news_link = driver.find_element(By.ID, "l_nwst").click()
    # news_link = driver.find_element(By.ID, "l_gr").click()
    # time.sleep(10)

    # coocies
    # with open(f"{vk_phone}_cookies", "wb") as f:
    #     pickle.dump(driver.get_cookies(), f)
    # driver.quit()
    # pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    # browser = webdriver.Chrome()
    # browser.get("https://vk.com/")
    # browser.delete_all_cookies()

    # pickle.dump(driver.get_cookies(), open(f"{vk_phone}.cookies", "wb"))

    driver.get("https://vk.com/")
    time.sleep(5)

    for cookie in pickle.load(open(f"{vk_phone}.cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()