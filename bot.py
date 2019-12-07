#from pyvirtualdisplay import Display
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
import sys
import time
import os

gamepin = sys.argv[1]

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1024,728")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

driver.get('https://quizizz.com/join/')
time.sleep(2.8)
#driver.save_screenshot("screenshot.png")
inputElement = driver.find_element_by_class_name("check-room-input")
inputElement.send_keys(gamepin)
inputElement.send_keys(Keys.ENTER)
time.sleep(2.5)
#    invalidpinbox = driver.find_element_by_class_name("content right error")



invalidcode = driver.find_elements_by_xpath("//div[@class='content right error']")
errorcode = driver.find_elements_by_xpath("//div[@class='An error has occured. Please Try Again.']")

if invalidcode[0].is_displayed():
    driver.save_screenshot("notvalid.png")
    #print("Game PIN not valid!")
    subprocess.call('echo Game PIN not valid!',shell=True)
    sys.stdout.write("Game PIN not valid!")
    sys.stdout.flush()
    #sys.exit(" 1 ")
else:
    #print ("Game PIN is valid!")
    subprocess.call('echo Game PIN valid!',shell=True)
    sys.stdout.write("Game PIN valid!")
    sys.stdout.flush()
    #sys.exit(" valid9 ")


driver.close();
