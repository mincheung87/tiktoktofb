import time
import random
from helpers.tiktok_helper import TiktokHelper
from helpers.omini import Omni
from selenium.webdriver.common.by import By

def get_driver():
    config = []
    BROWSER_DETECT = Omni(config)
    driver = BROWSER_DETECT.get()
    return driver

driver = get_driver()
driver.get('https://facebook.com')
time.sleep(0.5)
driver.get('https://business.facebook.com/creatorstudio/home')
#
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div/div/div/span/div/div/div/span").click()
time.sleep(1)
fileupload = "E:\Tiktok\TiktokToReel\videotiktok\v12044gd0000ccef3n3c77u82otgdb4g.mp4 \n E:\Tiktok\TiktokToReel\videotiktok\v12044gd0000cceggfbc77u4e28k91i0.mp4"
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[3]/div/div/div[2]/div/a/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[3]/div/div/div[2]/div/a/div/input").send_keys("E:\Tiktok\TiktokToReel\videotiktok\v12044gd0000ccef3n3c77u82otgdb4g.mp4 \n E:\Tiktok\TiktokToReel\videotiktok\v12044gd0000cceggfbc77u4e28k91i0.mp4")

