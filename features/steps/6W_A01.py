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


#ドライバのインストール
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver = susa.getDriver() 

"""
AW01新規ウィジェットを作成する Create a new widget
https://jaqool.atlassian.net/browse/GPT-770

kenta+b230109-admin@kotozna.com
developer+kenta-lamondo@kotozna.com
"""


# Scenario: [A11-01]ウィジェット設定画面を開く Open the widget setting screen
# https://jaqool.atlassian.net/browse/GPT-328
@given('基本設定の画面が表示されている2 The basic setting screen is displayed')
def chinsara_G(chinsara):
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

#
@when('左のメニューバーから「ウィジェット設定」をクリックする Click "Widget Settings" from the left menu bar')
def chinsara_W(chinsara):
    cur_url = driver.current_url
    if 'https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/basicConfiguration' in cur_url:
        #ウィジェット設定へ移動
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()

    time.sleep(5)

#
@then('現在登録されているウィジェット一覧が表示されるA list of currently registered widgets is displayed.')
def chinsara_T(chinsara):
    result_a11_01 = "" 
    checkp1 = 0
    checkp2 = 0
    checkp3 = 0
    widget_setting = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]')  # dev要素をCSSセレクタで見つける場合
    widget = widget_setting.text
    if '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]' == widget:
        #ウィジェット設定へ移動
        checkp1 = 1
    agopoyo = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[1]/td[1]/span")    
    jidoukayou = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[1]/span")
    assert (agopoyo.text == "あごぽよクリーニング香椎本店") & (jidoukayou.text == "自動化用")
#
@then('GPTと連携しているウィジェットのGPTステータスにはcheckが入っている')
def chinsara_T(chinsara):
    #And GPTと連携しているウィジェットのGPTステータスには✓が入っている
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[7]/td[2]/div/template/div/i')
    check = element.get_attribute('class')
    #
    if 'mdi-check-all mdi v-icon notranslate v-theme--light v-icon--size-default text-green' in check:
        checkp2 = 1
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[12]/td[2]/div/template/div/i')
    #
    notcheck = element.get_attribute('class')
    #if 'mdi-minus mdi v-icon notranslate v-theme--light v-icon--size-default' in notcheck:
    #    checkp3 = 1
    #一覧が表示され、ステータスが変わっているか
    assert 'mdi-minus mdi v-icon notranslate v-theme--light v-icon--size-default' in notcheck

# Scenario: [A11-02]新規ウィジェット作成画面に進む Go to the new widget creation screen
# https://jaqool.atlassian.net/browse/GPT-329
@given('現在登録されているウィジェット一覧が表示されているA list of currently registered widgets is displayed.')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('右上の追加ボタンをクリックするClick the add button in the upper right')
def chinsara_W(chinsara):
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').click()
    time.sleep(5)
    
#
@then('「1担当グループ」から「8スニペット」までの登録面に遷移するTransition to the registration side from "1charge group" to "7 snippet"')
def chinsara_T(chinsara):
    cur_url = driver.current_url
    assert 'https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/newWidgetSetting' in cur_url