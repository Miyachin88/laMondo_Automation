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
エスカレーション機能の設定
https://jaqool.atlassian.net/browse/GPT-831
kenta+b230109-admin@kotozna.com
developer+kenta-lamondo@kotozna.com
developer+kenta-lamondo+super@kotozna.com
"""

#ドライバのインストール
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


"""
ウィジェット(自動化用)を開く
"""
def openW():
    #infoボタンをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[6]/div/div/button').click()
    driver.switch_to.window
    time.sleep(10)
    #ウィジェットを開く
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div[2]').click()
    time.sleep(30) 
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 2番目のタブに切り替える
    second_tab_handle = tab_handles[1]
    driver.switch_to.window(second_tab_handle)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(5)
    # スタートボタンを押下
    element = driver.find_element(By.XPATH,'/html/body/span/div/div[1]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('こんにちは')
    # メッセージを送信
    driver.find_element(By.XPATH,'/html/body/span/div/div[1]/div/main/div/div/div[2]/div[2]/div/button[2]').click()
    time.sleep(30)
    # メッセージボタンを押下
    driver.find_element(By.XPATH,'/html/body/span/div/div[1]/div/main/div/div/div[2]/div[3]/div/button[1]').click()
    time.sleep(10)


""" 
管理画面にログイン
"""
def loginAdmin():
    #ログイン
    driver.get('https://beta-tenant-admin.im.kotozna.chat/ja/login')
    time.sleep(5)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('developer+kenta-lamondo+super@kotozna.com')
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('000000')
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    # dev要素を見つけて、そのテキストを取得する
    time.sleep(10)
        
# [AW21-01]ウィジェット設定画面を開く
# https://jaqool.atlassian.net/browse/GPT-832
# 

# 
@given('基本設定の画面が表示されている The basic setting screen is displayed')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('左のメニューバーから「ウィジェット設定」をクリックする2 Click "Widget Settings" from the left menu bar')
def chinsara_W(chinsara):
    cur_url = driver.current_url
    if 'https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/basicConfiguration' in cur_url:
        #ウィジェット設定へ移動
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()
    time.sleep(5)

#
@then('現在登録されているウィジェット一覧が表示される2 A list of currently registered widgets is displayed.')
def chinsara_T(chinsara):
    #ウィジェット設定画面に戻る
    cur_url = driver.current_url
    assert 'https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/widgetSetting' in cur_url

#
@then('エスカレーションスイッチが全てオフになっている')
def chinsara_T(chinsara):
    #自動化用のトグルを確認する
    jidoukatoggle = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[3]/div/div[1]/div/div/div[2]/input')
    #①ONの場合は
    if jidoukatoggle.is_selected():
        #トグルをクリックしてOFFにする
        jidoukatoggle.click()
        assert not jidoukatoggle.is_selected()
    #②OFFの場合は
    else :
        assert not jidoukatoggle.is_selected()


# [AW21-02]エスカレーション機能をONにする
# https://jaqool.atlassian.net/browse/GPT-833
# 

# 
@given('エスカレーションスイッチが全てオフになっている')
def chinsara_G(chinsara):
    #自動化用のトグルを確認する
    jidoukatoggle = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[3]/div/div[1]/div/div/div[2]/input')
    #①ONの場合は
    if jidoukatoggle.is_selected():
        #トグルをクリックしてOFFにする
        jidoukatoggle.click()
    else :
        print('chinsara')
#
@when('GPTステータスに✓が入っている任意のウィジェットのスイッチをオンにする')
def chinsara_W(chinsara):
    #自動化用のトグルを確認する
    jidoukatoggle = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[3]/div/div[1]/div/div/div[2]/input')
    #①ONの場合は
    if not jidoukatoggle.is_selected():
        #トグルをクリックしてOFFにする
        jidoukatoggle.click()
    else :
        print('chinsara')

#
@then('スイッチがピンク色に切り替わり、"レコードは正常に編集されました。"と表示される')
def chinsara_T(chinsara):
    jidoukatoggle = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[3]/div/div[1]/div/div/div[2]/input')
    assert jidoukatoggle.is_selected()

#
@then('ゲスト画面のメッセージ入力欄にはエスカレーションボタンが表示される')
def chinsara_T(chinsara):
    openW()
    messagebutton = driver.find_element(By.XPATH, '/html/body/span/div/div[1]/div/main/div/div/div[2]/div[3]/div/button[1]')
    assert messagebutton.is_enabled()

# [AW21-03]エスカレーション機能をOFFにする
# https://jaqool.atlassian.net/browse/GPT-834
# 

# 
@given('エスカレーションスイッチ（GPTステータスの右隣）がオンになっているウィジェットがある')
def chinsara_G(chinsara):
    print('susara')

#
@when('スイッチをオフにする')
def chinsara_W(chinsara):
    print('susara')

#
@then('スイッチがグレーに切り替わり、"レコードは正常に編集されました。"と表示される')
def chinsara_T(chinsara):
    print('susara')

#
@then('ゲスト画面のメッセージ入力欄からエスカレーションボタンが非表示になる')
def chinsara_T(chinsara):
    print('susara')