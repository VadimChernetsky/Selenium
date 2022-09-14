# from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent
from auth import proxy_login, proxy_password

# url = "https://www.vk.com/"

user_agents_list = [
    "Saturn",
    "Mars",
    "Jupiter"
]

useragent = UserAgent()

# Создаем объект options
options = webdriver.ChromeOptions()

# options.add_argument("user-agent=HelloWorld")
# options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) "
#                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
# options.add_argument(f"user-agent={useragent.opera}")
options.add_argument(f"user-agent={useragent.random}")

# подключение proxy
# подключение без авторизации, либо с привязкой к IP
# options.add_argument("--proxy-server=138.128.91.65:8000")

# подключение proxy с авторизацией, и без привязки к своему IP
# {login}:{password} логин и пароль своего proxy
proxy_options = {
    "proxy": {
        "https": f"htpps://{proxy_login}:{proxy_password}@138.128.91.65:8000"
    }
}

s = Service("D:\\PROJECTI\\Selenium\\chromedriver.exe")
# r"D:\PROJECTI\Selenium\chromedriver.exe"

# driver = webdriver.Chrome(service=s,
#                           options=options
#                           )

driver = webdriver.Chrome(service=s,
                          seleniumwire_options=proxy_options
                          )

# for i in user_agents_list:
#     options.add_argument(f"user-agent={i}")
#     s = Service("D:\\PROJECTI\\Selenium\\chromedriver.exe")
#     driver = webdriver.Chrome(service=s,
#                               options=options
#                               )
#     try:
#         driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
#         time.sleep(5)
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()

try:
    # Сайт, который показывает user_agent
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    # driver.get(url=url)
    # time.sleep(5)
    # driver.get(url="https://www.instagram.com/")
    # time.sleep(5)

    # driver.refresh()
    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://www.vk.com/")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # time.sleep(2)

    # Узнать IP адрес
    driver.get(url="https://2ip.ru/")
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

