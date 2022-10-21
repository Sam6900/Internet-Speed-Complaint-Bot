from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

TWITTER_EMAIL = os.environ["EMAIL"]
TWITTER_PSWD = os.environ["PSWD]
TWITTER_USERNAME = os.environ["USERNAME"]
min_down_speed, min_upload_speed = 100, 40
chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.speedtest.net/")
time.sleep(2)
accept_cookies = driver.find_element("id", "onetrust-accept-btn-handler")
accept_cookies.click()
go_btn = driver.find_element("class name", "start-text")
go_btn.click()
time.sleep(40)

download_speed = driver.find_element("class name", "download-speed")
upload_speed = driver.find_element("class name", "upload-speed")
if download_speed.text == "--" or upload_speed.text == "--":
    time.sleep(20)
    download_speed = driver.find_element("class name", "download-speed")
    upload_speed = driver.find_element("class name", "upload-speed")

download_speed, upload_speed = download_speed.text, upload_speed.text

# Twitter Login
if float(download_speed) < min_down_speed or float(upload_speed) < min_upload_speed:
    driver.switch_to.new_window()
    driver.get("https://twitter.com/")
    time.sleep(6)
    signin_btn = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
    signin_btn.click()
    time.sleep(3)
    enter_mail = driver.find_element("tag name", "input")
    enter_mail.send_keys(TWITTER_EMAIL)
    next_btn = driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
    next_btn.click()
    time.sleep(3)

    enter_username = driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    enter_username.send_keys(TWITTER_USERNAME)
    usercheck_next_btn = driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
    usercheck_next_btn.click()
    time.sleep(3)

    enter_pswd = driver.find_element("xpath",  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    enter_pswd.send_keys(TWITTER_PSWD)
    login_btn = driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
    login_btn.click()
    time.sleep(5)
                          
driver.quit()
