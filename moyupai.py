import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('--disable-gpu')

chrome_driver_path = "/usr/local/bin/chromedriver" # GitHub Actions 中的 ChromeDriver 路径
username = '153526739' # 登录账号
password = 'feiquan' # 登录密码

def get_driver():
    driver = webdriver.Chrome(chrome_driver_path, options=options)
    driver.implicitly_wait(10)
    return driver

def login(driver):
    try:
        driver.get("https://720ccl88.emy163.cn/user/login.php")
        # 等待用户名和密码输入框出现
        wait = WebDriverWait(driver, 10)
        user_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='user']")))
        user_input.send_keys(username)
        pass_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='pass']")))
        pass_input.send_keys(password)
        submit_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='submit_login']")))
        submit_btn.click()
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    driver = get_driver()
    login(driver)
