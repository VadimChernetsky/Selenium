from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


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
# options.add_argument("--headless")
# Фоновый режим 2 способ
# options.headless = True


driver = webdriver.Chrome(service=s,
                          options=options
                          )

try:
    driver.get("https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty")
    time.sleep(10)
    # print(driver.window_handles)
    # Распечатать текущий URL адрес
    print(f"Currently URL is: {driver.current_url}")

    # items = driver.find_elements(By.XPATH, '//div[@class="iva-item-slider-pYwHo"]')
    items = driver.find_elements(By.XPATH, '//a[@class="iva-item-sliderLink-uLz1v"]')
    # items = driver.find_element(By.CLASS_NAME, 'iva-item-sliderLink-uLz1v')
    items[0].click()
    time.sleep(10)
    # print(driver.window_handles)

    # Перемещение по вкладкам браузера
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    print(f"Currently URL is: {driver.current_url}")

    # Получаем имя продовца
    username = driver.find_element(By.CLASS_NAME, "seller-info-name")
    print(f"User name is: {username.text}")
    time.sleep(5)

    # Закрыть вкладку
    driver.close()

    # Отпровляем браузер на основную вкладку
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)
    print(f"Currently URL is: {driver.current_url}")

    items[1].click()
    time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    print(f"Currently URL is: {driver.current_url}")

    # Еще раз узнаем имя продовца по XPATH
    username1 = driver.find_element(By.XPATH, "//div[@data-marker='seller-info/name']")
    print(f"User name is: {username1.text}")

    # Узнаем дату публикации
    ad_date = driver.find_element_by(By.CLASS_NAME, "title-info-metadata-item-redesign")
    print(f"An ad date is: {ad_date.text}")

    # Получаем дату регистрации пользователя, классов несколько, а нужная информация находится во втором
    joined_date = driver.find_elements(By.CLASS_NAME, "seller-info-value")[1]
    print(f"User since: {joined_date.text}")
    time.sleep(5)
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()