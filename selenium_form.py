from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from auth import vk_password

# Создаем объект options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Apple Safari 5.1 (Win 8 x64): Mozilla/5.0 (Windows NT 6.2; WOW64) "
                     "AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2")

s = Service("D:\\PROJECTI\\Selenium\\chromedriver.exe")
# r"D:\PROJECTI\Selenium\chromedriver.exe"

driver = webdriver.Chrome(service=s,
                          options=options
                          )

try:
    driver.get("https://vk.com/")
    time.sleep(5)

    email_input = driver.find_element(By.ID, "index_email")
    email_input.clear()
    email_input.send_keys("375256530494")
    time.sleep(5)

    password_input = driver.find_element(By.ID, "index_pass")
    password_input.clear()
    password_input.send_keys(vk_password)
    time.sleep(3)
    # 1 способ авторизации, находясь в окне ввода пароля, стимулируем нажатие клавиши ENTER
    password_input.send_keys(Keys.ENTER)

    # 2 способ авторизации, нажимаем на саму кнопку
    # login_button = driver.find_element(By.ID, "index_login_button").click()
    time.sleep(10)

    # news_link = driver.find_element(By.ID, "l_nwst").click()
    # time.sleep(5)

    profile_page = driver.find_element_by_id("l_pr").click()
    time.sleep(5)

    # Оставить комент под видео
    comment_icon = driver.find_element_by(By.CLASS_NAME, "_comment").find_element_by(By.CLASS_NAME,
                                                                                     "like_button_icon").click()
    time.sleep(5)

    driver.find_elements_by(By.CLASS_NAME, "submit_post_field")[1].send_keys("Hey! I was here! (.)(.)" + Keys.ENTER)
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()