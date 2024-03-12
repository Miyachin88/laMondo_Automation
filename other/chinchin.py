import webbrowser
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import*
import time
import json


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def chinchin():
    # 
    print('chinchin')
    driver.get('https://kotozna.com/')
    time.sleep(10)
    driver.find_element(By.XPATH,'//*[@id="ktzn-tm-icon"]').click()
    time.sleep(20)
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    # iframeに切り替え
    driver.switch_to.frame(iframe)
    time.sleep(5)
    element = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('Kotozna test 製品の価格を教えて？')
    driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div[2]/div/button').click()
    time.sleep(20)