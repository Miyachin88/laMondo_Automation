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
AW05Create New Widget Step ❹　ゲストによる評価設定
https://jaqool.atlassian.net/browse/GPT-791
kenta+b230109-admin@kotozna.com
developer+kenta-lamondo@kotozna.com
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
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('developer+kenta-lamondo@kotozna.com')
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    time.sleep(5)
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


# [AW05-01]メッセージ評価をONにする / Turn on Message Rating
# https://jaqool.atlassian.net/browse/GPT-335
# 

@given('Tenant Admin Panel Guest Rating setting is displayed/ ゲストによる評価設定画面を開いている')
def chinsara_G(chinsara):
    loginAdmin()
#
@when('Turn on "Message Rating"/ メッセージ評価を利用するのスイッチをONにする')
def chinsara_W(chinsara):
    time.sleep(3)
#
@then('In Guest Screen, each message from GPT has clickable "thumbs up/down"/ ゲスト画面では、GPTからの返信毎にいいね！ボタンが表示される')
def chinsara_T(chinsara):
    print(chinsara)


# [AW05-02]ゲストによる評価をONにする Turn "Guest Rating" option ON
# https://jaqool.atlassian.net/browse/GPT-336
# 

@given('❹ゲストによる評価画面で、「ゲストによる評価を利用する」トグルがオフになっている/❹Guest Rating screen is displayed with Guest rating automatically off')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('トグルをオンにする/Switch toggle to "ON"')
def chinsara_W(chinsara):
    time.sleep(3)
#
@then('ゲスト評価のデザイン選択肢が表示される/The four candidates of the design are displayed on the admin panel')
def chinsara_T(chinsara):
    print(chinsara)

# [AW05-03]「５アイコン」に設定する If ON, Set Guest Rating to "5 icons"
# https://jaqool.atlassian.net/browse/GPT-337
# 

@given('❹ゲストによる評価画面におり、トグルがオンになっている1/Guest Rating is turned on')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('「５アイコン」を選択する/Select "5 Icon"')
def chinsara_W(chinsara):
    time.sleep(3)
#
@then('管理画面ではサンプルが表示され、ゲスト画面で会話終了後に５段階評価のアイコンが表示される/Guest rating survey is set to rate chat between 5 icons, display sample of "5 Icon" is automatically displayed')
def chinsara_T(chinsara):
    print(chinsara)

# [AW05-04]「 星」に設定する If ON, Set Guest Rating to "Stars"
# https://jaqool.atlassian.net/browse/GPT-338
# 
    
@given('❹ゲストによる評価画面におり、トグルがオンになっている2/Guest Rating is turned on')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('「星」を選択する/Select "Emoji"')
def chinsara_W(chinsara):
    time.sleep(3)
#
@then('管理画面ではサンプルが表示され、ゲスト画面で会話終了後に星5段階評価のアイコンが表示されるGuest rating survey is set to rate chat between 5 icons, display sample of "Emoji" is automatically displayed')
def chinsara_T(chinsara):
    print(chinsara)
    
