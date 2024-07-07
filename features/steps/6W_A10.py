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
import calendar
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException


"""
ウィジェット一覧に戻る
https://jaqool.atlassian.net/browse/GPT-1057
kenta+b230109-admin@kotozna.com
developer+kenta-lamondo@kotozna.com
developer+kenta-lamondo+super@kotozna.com
"""

#ドライバのインストール
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

""" 
管理画面にログイン
"""
def loginAdmin():
    #ログイン
    driver.get('https://beta-tenant-admin.im.kotozna.chat/ja/login')
    time.sleep(5)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('developer+kenta-lamondo+super@kotozna.com')
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('000000')
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    # dev要素を見つけて、そのテキストを取得する
    time.sleep(10)
    cur_url = driver.current_url
    if 'https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/basicConfiguration' in cur_url:
        #ウィジェット設定へ移動
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()
    time.sleep(5)
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    #営業時間の設定を解除
    #パターン1：受付時間のプルダウンが表示されてない
    eigyo_type = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[3]/div/div/span').text 
    if '' == eigyo_type:
        #プルダウンをクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div').click()
        time.sleep(5)
    else :
    #パターン2：すでに受付時間のプルダウンが表示
        #最初のゴミ箱をクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]').click()
        try:
            #2番目のゴミ箱をクリック
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]').click()
        except NoSuchElementException:
            pass
        except ElementClickInterceptedException:
            pass
        #ばつボタンをクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[4]/i').click()
        time.sleep(5)
        #プルダウンをクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div').click()
        time.sleep(5)     
    # 自動化用のウィジェットの②営業時間にて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)   
    #営業時間外をクリックして、設定を解除する
    time.sleep(10)
    outofbusihour = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/input')
    #営業時間外のチェックボックスがクリックされている
    if outofbusihour.is_selected():
        #クリックを解除
        outofbusihour.click()    
    #不在時をクリック
    outoftime = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/input')
    #不在時のチェックボックスがクリックされている
    if outoftime.is_selected():
        #クリックを解除
        outoftime.click()

    # 自動化用のウィジェットの③不在時のメール受信設定にて”保存して閉じます”をクリックしてウィジェット設定へ移動
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
    time.sleep(10)
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    # 自動化用のウィジェットの②営業時間にて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    # 自動化用のウィジェットの③不在時のメール受信設定にて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    # 自動化用のウィジェットの④ゲストによる評価にて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    # 自動化用のウィジェットの⑤システムメッセージにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)    
    # 自動化用のウィジェットの⑥デザイン設定にて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)   
    

# [AW10-01]新規ウィジェット作成後一覧に戻る Return to Widget List
# https://jaqool.atlassian.net/browse/GPT-347
# 

# 
@given('❼スニペット」画面が表示されている Snippet screen screen is displayed')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('右下の一覧に戻るボタンをクリックする Select "Return to the List" in the bottom right hand corner')
def chinsara_W(chinsara):
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div/button').click()
    time.sleep(5)

#
@then('現在登録されているウィジェット一覧が表示されているA list of currently registered widgets is displayed.')
def chinsara_T(chinsara):
    #ウィジェット設定画面に戻る
    cur_url = driver.current_url
    assert 'https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/widgetSetting' in cur_url