from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

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

driver.quit()
