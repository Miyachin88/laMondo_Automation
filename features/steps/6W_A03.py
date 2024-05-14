from contextlib import AsyncExitStack
from fileinput import filename
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import*
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import sys
from selenium.webdriver.common.keys import Keys


#ドライバのインストール
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver = susa.getDriver() 

"""
AW01新規ウィジェットを作成する Create a new widget
https://jaqool.atlassian.net/browse/GPT-770

kenta+b230109-admin@kotozna.com
developer+kenta-lamondo@kotozna.com
"""

def loginAdmin():
    #ログイン
    driver.get('https://beta-tenant-admin.im.kotozna.chat/ja/login')
    time.sleep(5)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('kenta+b230109-admin@kotozna.com')
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('000000')
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    # dev要素を見つけて、そのテキストを取得する
    time.sleep(10)



# Scenario: [AW02-01]ウィジェット名称を設定する Set the widget name
# https://jaqool.atlassian.net/browse/GPT-332
@Given('ウィジェット番号がデフォルトで設定されている Widget number is set by default')
def chinsara_G(chinsara):
    loginAdmin()
    

@When('ウィジェット名横のペンシルボタンから名称を変更し、✓ボタンを押す Change the name from the pencil button next to the widget name and press the ✓ button.')
def chinsara_G(chinsara):
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').click()
    time.sleep(5)

@Then('ウィジェット番号→指定した名前に変更されるWidget number → changed to the specified name. Name appears in chat header and initial messages.')
def chinsara_G(chinsara):
    #ワークコードテストの名称を編集
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div').click()
    #Then ウィジェット番号→指定した名前に変更されるWidget number → changed to the specified name. Name appears in chat header and initial messages.
    wait = WebDriverWait(driver, 300)
    wkcdname = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div[1]/form/div/div[1]/div/div[3]/input')))
    wkcdname.send_keys(Keys.COMMAND + "a" )
    wkcdname.send_keys( Keys.DELETE )
    wkcdname.send_keys('AW02-01 test')
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div[2]').click()
    widget_setting = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/h1')
    aw2_1 = widget_setting.text
    assert 'AW02-01 test' == aw2_1