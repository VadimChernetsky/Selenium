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

# Для новых версий браузера от 79.0.3945.16 включительно
options.add_argument("--disable-blink-features=AutomationControlled")

# Фоновый режим 1 способ
options.add_argument("--headless")
# Фоновый режим 2 способ
options.headless = True


driver = webdriver.Chrome(service=s,
                          options=options
                          )

try:
    driver.get("https://vk.com/")
    time.sleep(5)

    print('Проходим аутентификацию...')
    email_input = driver.find_element(By.ID, "index_email")
    email_input.clear()
    email_input.send_keys(vk_phone)
    time.sleep(3)

    login_button = driver.find_element(By.XPATH, '//button[@class="FlatButton FlatButton--primary FlatButton--size-l '
                                                 'FlatButton--wide VkIdForm__button VkIdForm__signInButton"]')
    login_button.click()
    time.sleep(3)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(vk_password)
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

    print('Переходим на страницу профайла...')
    profile_link = driver.find_element(By.ID, "l_pr").click()
    time.sleep(10)

    print('Начинаем просмотр видео...')
    video_block = driver.find_element(By.CLASS_NAME, "post_video_views_count").click()
    time.sleep(15)
    print('Финиш')

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
