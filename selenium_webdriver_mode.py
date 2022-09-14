from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Создаем объект options
options = webdriver.ChromeOptions()

# options.add_argument("user-agent=Apple Safari 5.1 (Win 8 x64): Mozilla/5.0 (Windows NT 6.2; WOW64) "
#                      "AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2")

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

s = Service("D:\\PROJECTI\\Selenium\\chromedriver.exe")
# r"D:\PROJECTI\Selenium\chromedriver.exe"

# Отключить режим webdriver
# Для старых версий браузера, до 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# Для новых версий браузера от 79.0.3945.16 включительно
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=s,
                          options=options
                          )

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()