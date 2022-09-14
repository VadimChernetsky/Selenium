from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from multiprocessing import Pool
import random

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

# urls_list = ["https://vk.com", "https://instagram.com", "https://github.com"]

# def get_data(url):
#     try:
#         # Создаем объект браузера
#         driver = webdriver.Chrome(service=s,
#                                   options=options
#                                   )
#         # Отправляем его по url адресу
#         driver.get(url=url)
#         time.sleep(5)
#         #Скриншот страницы
#         driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
#
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#
# if __name__ == '__main__':
#     p = Pool(processes=3) #urls_list состоит из 3х url адресов
#     p.map(get_data, urls_list)
#
# if __name__ == '__main__':
#     p = Pool(processes=2) #одновременно откроются 2 сайта, а 3й процесс стартует, как только освобождается занятый
#     p.map(get_data, urls_list)

# Если нужно потестировать один единственный сайт в многопроцессорном режиме

def get_data(url):
    try:
        # Создаем объект браузера
        driver = webdriver.Chrome(service=s,
                                  options=options
                                  )
        # Отправляем его по url адресу
        driver.get(url=url)
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "tiktok-kd7foj-DivVideoWrapper e1bh0wg716")\
            .find_element(By.CLASS_NAME, "tiktok-yf3ohr-DivContainer e1yey0rl0").click()
        time.sleep(random.randrange(10, 20))

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    # Вводим желаемое кол-во процессов
    process_count = int(input("Enter the number of processes: "))
    # Ввод сайта от пользователя
    url = input("Enter the URL: ")
    # Создаем список из url адресов, кол-во которых должно быть равно кол-ву запускаемых процессов
    urls_list = [url] * process_count
    print(urls_list)
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)


















