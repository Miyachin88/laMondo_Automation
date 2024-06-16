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


#ドライバのインストール
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver = susa.getDriver() 

"""
AW03 Create New Widget Step ❷
https://jaqool.atlassian.net/browse/GPT-775

kenta+b230109-admin@kotozna.com
developer+kenta-lamondo@kotozna.com
"""

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
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('000000')
    time.sleep(5)
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
    # 自動化用のウィジェットの②営業時間にて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)    
    #営業時間外をクリック
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
    # 自動化用のウィジェットの②鋭意用グループにて”保存して次へ”をクリックしてウィジェット設定へ移動
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
    time.sleep(10)
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)        

"""
パラメータリスト
"""

# 現在の日時を取得
now = datetime.now()
# 曜日を取得
weekday = calendar.day_name[now.weekday()]
# 日付のフォーマットを指定
#date_format = now.strftime("%Y/%m/%d %a %H:%M")
#現在時刻
date_format = now.strftime("%H:%M")
#今日の日付
monthday_format = now.strftime("%m%d")

# Scenario: [AW03-01]チャットの営業可能時間を設定する（毎日） Set chat business hours (Daily)
# https://jaqool.atlassian.net/browse/GPT-776

@Given('営業時間の設定画面が表示されている1')
def step_impl(context):
    loginAdmin()

@When('タイプのプルダウンから"受付時間"を選択1')
def step_impl(context):
    ##営業時間の設定
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

@When('タイトル欄に任意のタイトルを入力1')
def step_impl(context):
    #受付時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-01 title')
    time.sleep(3)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #プルダウンを表示
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)

@When('対象のプルダウンから"毎日"を選択1')
def step_impl(context):
    #毎日を選択
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(5)

@When('開始/終了時間を設定1')
def step_impl(context):
    ####時刻を入力
    #時刻を変換
    #時間を設定
    settingh = str(date_format[:2])
    sethour = int(settingh)
    #分を設定
    settingm = str(date_format[-2:])
    setminute = int(settingm)
    
        #時間を設定
    #ケース1 : 23時台の時
    if (settingh == 23):
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(settingh - 1):
            businessh_1st.click()
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59):
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input')
        #保存して閉じますをクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10)  

    #ケース2 : 0-22時台の時
    else:
        #時計を操作(開始時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(sethour + 1):
            businessh_1st.click()
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(setminute + (60 - setminute)):
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input')

@When('"保存"を押下1')
def step_impl(context):
    #保存して閉じますをクリック
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
    time.sleep(10)  

@Then('このウィジェットから受付時間外にお問い合わせを送ると、受付可能時間メッセージ、またはメール送信用フォームが表示される（設定による）1')
def step_impl(context):
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
    assert notaccept.text[:13] == '受付時間は下記の通りです。'
    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)

    
# Scenario: [AW03-02]チャットの営業可能時間を設定する（曜日） Set chat business hours (day of the week)
# https://jaqool.atlassian.net/browse/GPT-777
@Given('営業時間の設定画面が表示されている2')
def step_given_business_hours_setting_displayed(context):
    #ウィジェットを閉じる必要あり
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)

@When('タイプのプルダウンから"受付時間"を選択2')
def step_when_select_business_hours_type(context):
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

    #受付時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()

@When('タイトル欄に任意のタイトルを入力2')
def step_when_set_title(context):
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-02 title')
    time.sleep(10)

@When('対象のプルダウンから"曜日（優先度中）"を選択1')
def step_when_select_specific_day_type(context):
    #対象をクリック 曜日を指定
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #対象をクリック
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div')))    
    element.click()
    time.sleep(10)
    #曜日を指定をクリック
    wait = WebDriverWait(driver, 300)
    businessdtw = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div')))    
    businessdtw.click()
    time.sleep(5)

@When('曜日のプルダウンから任意の曜日を選択1')
def step_when_select_specific_day(context):
    #曜日をクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div')))
    add_businessh.click()
    time.sleep(10)

@When('開始/終了時間を設定2')
def step_when_set_start_end_time(context):
    ##休日なら月曜日をクリックして、平日なら土曜日をクリックするプログラム
    #休日の場合
    if weekday == "Saturday" or weekday == "Sunday":
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[1]/div/div/div/input').click()
        time.sleep(5)
        #保存して閉じますをクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10) 
    #平日の場合
    else:
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[6]/div[1]/div/div/div/input').click()
        time.sleep(5)

@When('"保存"を押下2')
def step_when_press_save_button(context):
    #保存して閉じますをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
    time.sleep(10) 

@Then('このウィジェットから受付時間外にお問い合わせを送ると、受付可能時間メッセージ、またはメール送信用フォームが表示される（設定による）2')
def step_then_out_of_business_message_or_form_displayed(context):
    #ウィジェット設定に戻り自動化用のウィジェットを開く
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
    assert notaccept.text[:13] == '受付時間は下記の通りです。'
    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)



# Scenario: [AW03-03]チャットの営業可能時間を設定する（特定の日のみ）Set chat business hours (only on specific days)
# https://jaqool.atlassian.net/browse/GPT-778
@Given('営業時間の設定画面が表示されている3')
def step_display_business_hours_setting_screen(context):
    #ウィジェットを閉じる必要あり
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

@When('タイプのプルダウンから"受付時間"を選択3')
def step_select_business_hours_type(context):
    #受付時間をクリック
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div')))
    element.click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()

@When('タイトル欄に任意のタイトルを入力3')
def step_input_title_in_field(context):
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-03 title')
    time.sleep(10)

@When('対象のプルダウンから"日を指定（優先度高）"を選択1')
def step_select_specify_date_as_subject(context):
    #対象をクリック 曜日を指定
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)

@When('曜日のプルダウンから任意の日を選択1')
def step_select_any_date_from_day_dropdown(context):
    #日を指定をクリック
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div[2]/div')))
    element.click()
    time.sleep(5)
    #日をクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div[2]/div[2]/div/div/div/input')))
    add_businessh.click()
    time.sleep(10)

@When('開始/終了時間を設定3')
def step_set_start_and_end_time(context):
    print('chinchin')

@When('"保存"を押下3')
def step_press_save_button(context):
    for i in range(6):  # 配列の長さまたは6の少ない方をループ回数とする
        #週を探索および設置
        flag = False 
        hello1 = str(i + 1)
        setsearchweek = "/div[" + str(hello1) + "]"
        for j in range(7):  # i+1回数の少ない方をループ回数とする
            #曜日を探索および設置
            hello2 = str(j + 1)
            setsearchdayoftheweek = "/div[" + hello2 + "]"        
            setpath = "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]" + setsearchweek + setsearchdayoftheweek
            dateset = driver.find_element(By.XPATH,setpath)
            widget = dateset.text
            #文字の色を取得
            setpathcolor = "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]" + setsearchweek + setsearchdayoftheweek + "/div"        
            widgetcolor = driver.find_element(By.XPATH,setpathcolor)
            color = widgetcolor.value_of_css_property('color')
            #日付が1-9日の時とそうでない時の条件分岐
            if widget.__len__ == 1 :
                #日付が合致していたらクリックする
                if (widget == monthday_format[-1:]) & (color == 'rgba(33, 33, 33, 1)'):
                    wait = WebDriverWait(driver, 300)
                    element = wait.until(EC.visibility_of_element_located((By.XPATH,setpath)))
                    dateset.click()
                    time.sleep(3)
                    #選択ボタンをクリック
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    time.sleep(3)
                    #時計を操作(終了時間のみ)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
                    time.sleep(5)
                    wait = WebDriverWait(driver, 300)
                    businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
                    for _ in range(23): #23時に設定
                        businessh_1st.click() #受付時間の時間を入力
                    #分を設定
                    wait = WebDriverWait(driver, 300)
                    businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
                    #時刻を設定
                    for _ in range(59): #59分に設定
                        businessm_1st.click()
                    #選択をクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    #保存をクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[7]/div[2]/button').click()                                
                    #保存して閉じますをクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
                    time.sleep(10)
                    flag = True  # フラグをTrueに設定
                    break;
            #10日から31日の時
            else :
                #日付が合致しているかつ文字が黒の時はクリックする
                if (widget == monthday_format[-2:]) & (color == 'rgba(33, 33, 33, 1)'):
                    wait = WebDriverWait(driver, 300)
                    element = wait.until(EC.visibility_of_element_located((By.XPATH,setpath)))
                    dateset.click()
                    time.sleep(3)
                    #選択ボタンをクリック
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    time.sleep(3)
                    #時計を操作(終了時間のみ)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
                    time.sleep(5)
                    wait = WebDriverWait(driver, 300)
                    businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
                    for _ in range(23): #23時に設定
                        businessh_1st.click() #受付時間の時間を入力
                    #分を設定
                    wait = WebDriverWait(driver, 300)
                    businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
                    #時刻を設定
                    for _ in range(59): #59分に設定
                        businessm_1st.click()            
                    #選択をクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()                    
                    #保存をクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[7]/div[2]/button').click()    
                    
                    #保存して閉じますをクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
                    time.sleep(10)
                    flag = True  # フラグをTrueに設定
                    break;    
        if flag:  # フラグがTrueの場合、外側のループを抜ける
            break

@Then('このウィジェットから受付時間外にお問い合わせを送ると、受付可能時間メッセージ、またはメール送信用フォームが表示される（設定による）3')
def step_verify_response_message_or_email_form(context):
    #ウィジェット設定に戻り自動化用のウィジェットを開く
    time.sleep(10)
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__title.pa-4')))
    assert notaccept.text[:13] == '利用規約'

    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)


# Scenario: [AW03-04]チャットの対応不可時間を設定する（毎日）Set chat unavailable hours (Daily)
# https://jaqool.atlassian.net/browse/GPT-779
@Given('営業時間の設定画面が表示されている4')
def step_display_business_hours_setting_screen(context):
    #ウィジェットを閉じる必要あり
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
        ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

@When('タイプのプルダウンから"受付不可時間"を選択1')
def step_select_out_of_business_hours_type(context):
    #受付不可時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()

@When('タイトル欄に任意のタイトルを入力4')
def step_input_title_in_field(context):
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-04 title')
    time.sleep(3)

@When('対象のプルダウンから"毎日"を選択2')
def step_select_daily_as_subject(context):
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #プルダウンを表示
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)
    #毎日を選択
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(5)

@When('開始/終了時間を設定4')
def step_set_start_and_end_time(context):
    print('chinchin')

@When('"保存"を押下4')
def step_press_save_button(context):
    ####時刻を入力
    #時刻を変換
    #時間を設定
    settingh = str(date_format[:2])
    sethour = int(settingh)
    #分を設定
    settingm = str(date_format[-2:])
    setminute = int(settingm)
    #時間を設定
    #ケース1 : 23時台の時
    if (settingh == 23):
        #時計を操作(開始時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(sethour - 1): #22時に設定
            businessh_1st.click()
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(setminute + (60 - setminute)): #59分に設定
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input')
        #保存して閉じますをクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10) 

    #ケース2 : 0-22時台の時
    else:
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(sethour + 1): #23時に設定
            businessh_1st.click() #受付時間の時間を入力
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59): #59分に設定
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input')
        #保存して閉じますをクリックdiv/div/div[2]').click()
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10)  

@Then('このウィジェットから受付時間外にお問い合わせを送ると、受付可能時間メッセージ、またはメール送信用フォームが表示される（設定による）4')
def step_verify_response_message_or_email_form(context):
    #ウィジェット設定に戻り自動化用のウィジェットを開く
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
    assert notaccept.text[:23] == '以下は受付時間外となりますのでご了承ください。'
            
    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10) 

# Scenario: [AW03-05]チャットの対応不可時間を設定する（曜日）Set chat unavailable hours (day of the week)
# https://jaqool.atlassian.net/browse/GPT-780
@Given('営業時間の設定画面が表示されている5')
def step_given_display_business_hours_setting_screen(context):
    #ウィジェットを閉じる必要あり
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

@When('タイプのプルダウンから"受付不可時間"を選択2')
def step_when_select_out_of_business_hours_type(context):
    #受付不可時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()

@When('タイトル欄に任意のタイトルを入力5')
def step_when_input_title_in_field(context):
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-05 title')
    time.sleep(10)

@When('対象のプルダウンから"曜日（優先度中）"を選択2')
def step_when_select_specify_day_of_week_as_subject(context):
    #対象をクリック 曜日を指定
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)

@When('曜日のプルダウンから任意の曜日を選択2')
def step_when_select_any_day_from_day_dropdown(context):

    #曜日を指定をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div').click()
    time.sleep(5)

@When('開始/終了時間を設定5')
def step_when_set_start_and_end_time(context):
    print('chinchin')

@When('"保存"を押下5')
def step_when_press_save_button(context):
    #曜日をクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div')))
    add_businessh.click()
    time.sleep(10)
    ##休日なら土日をクリックして、平日なら月ー金曜日をクリックするプログラム
    #休日の場合
    if weekday == "Saturday" or weekday == "Sunday":
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[6]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[7]/div[1]/div/div/div/input').click()
        time.sleep(5)
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(23): #23時に設定
            businessh_1st.click() #受付時間の時間を入力
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59): #59分に設定
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        #保存して閉じますをクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10) 
    #平日の場合
    else:
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[4]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[5]/div[1]/div/div/div/input').click()
        time.sleep(5)
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(23): #23時に設定
            businessh_1st.click() #受付時間の時間を入力
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59): #59分に設定
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        #保存して閉じますをクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10) 

@Then('このウィジェットから受付時間外にお問い合わせを送ると、受付可能時間メッセージ、またはメール送信用フォームが表示される（設定による）5')
def step_then_verify_response_message_or_email_form(context):
    #ウィジェット設定に戻り自動化用のウィジェットを開く
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
    assert notaccept.text[:23] == '以下は受付時間外となりますのでご了承ください。'

    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10) 


# Scenario: [AW03-06]チャットの対応不可時間を設定する（特定の日のみ）Set chat unavailable hours (only on specific days)
# https://jaqool.atlassian.net/browse/GPT-781
@Given('営業時間の設定画面が表示されている6')
def step_given_display_business_hours_setting_screen(context):
    #ウィジェットを閉じる必要あり
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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


@When('タイプのプルダウンから"受付不可時間"を選択3')
def step_when_select_out_of_business_hours_type(context):
    #受付不可時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]').click()
    time.sleep(10)

@When('タイトル欄に任意のタイトルを入力6')
def step_when_input_title_in_field(context):
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-06 title')
    time.sleep(10)

@When('対象のプルダウンから"日を指定（優先度高）"を選択2')
def step_when_select_specify_day_of_week_as_subject(context):
    #対象をクリック 日を指定
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)
    #日を指定をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div[2]/div').click()
    time.sleep(5)

@When('曜日のプルダウンから任意の日を選択2')
def step_when_select_any_day_from_day_dropdown(context):
    #日をクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div[2]/div[2]/div/div/div/input')))
    add_businessh.click()
    time.sleep(10)

@When('開始/終了時間を設定6')
def step_when_set_start_and_end_time(context):
    print('chinchin')

@When('"保存"を押下6')
def step_when_press_save_button(context):
    for i in range(6):  # 配列の長さまたは6の少ない方をループ回数とする
        #週を探索および設置
        flag = False 
        hello1 = str(i + 1)
        setsearchweek = "/div[" + str(hello1) + "]"
        for j in range(7):  # i+1回数の少ない方をループ回数とする
            #曜日を探索および設置
            hello2 = str(j + 1)
            setsearchdayoftheweek = "/div[" + hello2 + "]"        
            setpath = "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]" + setsearchweek + setsearchdayoftheweek
            dateset = driver.find_element(By.XPATH,setpath)
            widget = dateset.text
            #文字の色を取得
            setpathcolor = "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]" + setsearchweek + setsearchdayoftheweek + "/div"        
            widgetcolor = driver.find_element(By.XPATH,setpathcolor)
            color = widgetcolor.value_of_css_property('color')
            #日付が1-9日の時とそうでない時の条件分岐
            if widget.__len__ == 1 :
                #日付が合致していたらクリックする
                if (widget == monthday_format[-1:]) & (color == 'rgba(33, 33, 33, 1)'):
                    dateset.click()
                    #選択ボタンをクリック
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    time.sleep(3)
                    #時計を操作(終了時間のみ)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
                    time.sleep(5)
                    wait = WebDriverWait(driver, 300)
                    businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
                    for _ in range(23): #23時に設定
                        businessh_1st.click() #受付時間の時間を入力
                    #分を設定
                    wait = WebDriverWait(driver, 300)
                    businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
                    #時刻を設定
                    for _ in range(59): #59分に設定
                        businessm_1st.click()
                    #選択をクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()               
                    #保存して閉じますをクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
                    time.sleep(10)
                    flag = True  # フラグをTrueに設定
                    break;                   
            #10日から31日の時
            else :
                #日付が合致しているかつ文字が黒の時はクリックする
                if (widget == monthday_format[-2:]) & (color == 'rgba(33, 33, 33, 1)'): 
                    dateset.click()
                    #選択ボタンをクリック
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    time.sleep(3)
                    #時計を操作(終了時間のみ)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
                    time.sleep(5)
                    wait = WebDriverWait(driver, 300)
                    businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
                    for _ in range(23): #23時に設定
                        businessh_1st.click() #受付時間の時間を入力
                    #分を設定
                    wait = WebDriverWait(driver, 300)
                    businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
                    #時刻を設定
                    for _ in range(59): #59分に設定
                        businessm_1st.click()
                    #選択をクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()               
                    #保存して閉じますをクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
                    time.sleep(10)
                    flag = True  # フラグをTrueに設定
                #else :
        if flag:  # フラグがTrueの場合、外側のループを抜ける
            break

@Then('このウィジェットから受付時間外にお問い合わせを送ると、受付可能時間メッセージ、またはメール送信用フォームが表示される（設定による）6')
def step_then_verify_response_message_or_email_form(context):
    #ウィジェット設定に戻り自動化用のウィジェットを開く
    time.sleep(10)
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
    assert notaccept.text[:23] == '以下は受付時間外となりますのでご了承ください。'

    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)


# Scenario: [AW03-07]営業不可時間を複数設定する Set multiple Out of Business Hours
# https://jaqool.atlassian.net/browse/GPT-782

@Given('営業時間の設定画面が表示されている7')
def step_impl(context):
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)

    ##営業時間の設定
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

@Given('設定タイプが"営業不可時間"になっている')
def step_impl(context):
    # 曜日を設定
    # 
    #受付不可時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-07 title1')
    time.sleep(10)

@When('「曜日」と「特定の日」を設定する(優先度：高)')
def step_impl(context):
    #対象をクリック 曜日を指定
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)

@When('特定日について、受付時間内に設定する 例）4/10(月) 11:00にアクセスする場合は4/10の10:00 - 20:00')
def step_impl(context):
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)
    #曜日を指定をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div').click()
    time.sleep(5)

@When('「曜日」と「特定の日」を設定する(優先度：中)')
def step_impl(context):
    #曜日をクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div')))
    add_businessh.click()
    time.sleep(10)
    ##休日なら土日をクリックして、平日なら月ー金曜日をクリックするプログラム
    #休日の場合
    if weekday == "Saturday" or weekday == "Sunday":
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[6]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[7]/div[1]/div/div/div/input').click()
        time.sleep(5)
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(23): #23時に設定
            businessh_1st.click() #受付時間の時間を入力
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59): #59分に設定
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        #保存して閉じますをクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10) 
    #平日の場合
    else:
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[4]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[5]/div[1]/div/div/div/input').click()
        time.sleep(5)
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(23): #23時に設定
            businessh_1st.click() #受付時間の時間を入力
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59): #59分に設定
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()

    #受付不可時間の2個目をクリック
    wait = WebDriverWait(driver, 300)
    add_dotw = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_dotw.click()
    # 
    #日時を設定       
    time.sleep(10) 
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-07 title2')
    time.sleep(10)
    
    #対象をクリック 日を指定
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/div/div[4]/div/div[2]/div[1]/div/div[4]').click()
    time.sleep(5)    
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/div/div[4]/div/div[2]/div[1]/div/div[5]').click()
    time.sleep(5)
    #日を指定(優先度高)をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div[2]/div').click()
    time.sleep(5)

@When('曜日について、受付時間内に設定する 例）4/10(月) 11:00にアクセスする場合は火〜日の10:00 - 20:00')
def step_impl(context):    
    #日をクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[2]/div/div/div/input')))
    add_businessh.click()
    time.sleep(10)

    for i in range(6):  # 配列の長さまたは6の少ない方をループ回数とする
        #週を探索および設置
        flag = False 
        hello1 = str(i + 1)
        setsearchweek = "/div[" + str(hello1) + "]"
        for j in range(7):  # i+1回数の少ない方をループ回数とする
            #曜日を探索および設置
            hello2 = str(j + 1)
            setsearchdayoftheweek = "/div[" + hello2 + "]"        
            setpath = "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]" + setsearchweek + setsearchdayoftheweek
            dateset = driver.find_element(By.XPATH,setpath)
            widget = dateset.text
            #文字の色を取得
            setpathcolor = "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]" + setsearchweek + setsearchdayoftheweek + "/div"        
            widgetcolor = driver.find_element(By.XPATH,setpathcolor)
            color = widgetcolor.value_of_css_property('color')
            #日付が1-9日の時とそうでない時の条件分岐
            if widget.__len__ == 1 :
                #日付が合致していたらクリックする
                if (widget == monthday_format[-1:]) & (color == 'rgba(33, 33, 33, 1)'):
                    dateset.click()
                    #選択ボタンをクリック
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    time.sleep(3)
                    #時計を操作(終了時間のみ)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
                    time.sleep(5)
                    wait = WebDriverWait(driver, 300)
                    businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
                    for _ in range(23): #23時に設定
                        businessh_1st.click() #受付時間の時間を入力
                    #分を設定
                    wait = WebDriverWait(driver, 300)
                    businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
                    #時刻を設定
                    for _ in range(59): #59分に設定
                        businessm_1st.click()
                    #選択をクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()               
                    #保存して閉じますをクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
                    time.sleep(10)
                    flag = True  # フラグをTrueに設定
                    break;                   
            #10日から31日の時
            else :
                #日付が合致しているかつ文字が黒の時はクリックする
                if (widget == monthday_format[-2:]) & (color == 'rgba(33, 33, 33, 1)'): 
                    dateset.click()
                    #選択ボタンをクリック
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    time.sleep(3)
                    #時計を操作(終了時間のみ)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
                    time.sleep(5)
                    wait = WebDriverWait(driver, 300)
                    businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
                    for _ in range(23): #23時に設定
                        businessh_1st.click() #受付時間の時間を入力
                    #分を設定
                    wait = WebDriverWait(driver, 300)
                    businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
                    #時刻を設定
                    for _ in range(59): #59分に設定
                        businessm_1st.click()
                    #選択をクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()              
                    #保存して閉じますをクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
                    time.sleep(10)
                    flag = True  # フラグをTrueに設定
                #else :
        if flag:  # フラグがTrueの場合、外側のループを抜ける
            break

    
@Then('このウィジェットから受付時間外にお問い合わせを送ると、受付時間外メッセージが表示される(添付画像参照)7')
def step_impl(context):
    #ウィジェット設定に戻り自動化用のウィジェットを開く
    time.sleep(10)
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
    assert notaccept.text == '以下は受付時間外となりますのでご了承ください。 00:00 - 23:59'

    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)   



# Scenario: [AW03-08]営業可能時間を複数設定する
# https://jaqool.atlassian.net/browse/GPT-783

@Given('営業時間の設定画面が表示されている8')
def step_display_business_hours_setting_screen(context):
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)

    ##営業時間の設定
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

@When('営業可能時間を1日の中で複数設定する。営業可能時間を設定 例）4/10(月) 13:00にアクセスする場合は毎日の10:00 - 13:00')
def step_set_multiple_business_hours(context):
    #受付時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-08 title')
    time.sleep(3)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #プルダウンを表示
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)
    #毎日を選択
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(5)
    #2つ目の時間設定ボタンをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[6]/button').click()
    time.sleep(5)

@When('営業可能時間を1日の中で複数設定する。営業外時間を設定 例）4/10(月) 13:00にアクセスする場合はの毎日の14:00 - 20:00')
def step_set_multiple_out_of_business_hours(context):
    #時間を設定
    ####時刻を入力
    #時刻を変換
    #時間を設定
    # 現在の日時を取得
    now = datetime.now()
    # 曜日を取得
    weekday2 = calendar.day_name[now.weekday()]
    # 日付のフォーマットを指定
    #date_format = now.strftime("%Y/%m/%d %a %H:%M")
    #現在時刻
    date_format2 = now.strftime("%H:%M")
    #今日の日付
    monthday_format2 = now.strftime("%m%d")
    
    settingh = str(date_format2[:2])
    sethour = int(settingh)
    #分を設定
    settingm = str(date_format[-2:])
    setminute = int(settingm)
    
    #ケース1 : 23時台の時
    if (settingh == 23) or (settingh == 0):
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(settingh - 1):
            businessh_1st.click()
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59):
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input')
        #保存して閉じますをクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10)  

    #ケース2 : 1-22時台の時
    else:
        #1番目の時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(sethour - 1):
            businessh_1st.click()
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59):
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)

        #2番目の時計を操作(開始時間)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr[2]/td[1]/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(sethour + 1):
            businessh_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input')
        
        #2番目の時計を操作(終了時間)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr[2]/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(23): #23時に設定
            businessh_1st.click() #受付時間の時間を入力
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59): #59分に設定
            businessm_1st.click()  
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()

        #保存して閉じますをクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10)
        flag = True

@Then('このウィジェットから受付時間外にお問い合わせを送ると、受付時間外メッセージが表示される8')
def step_verify_out_of_business_hour_message_displayed(context):
    #ウィジェット設定に戻り自動化用のウィジェットを開く
    time.sleep(10)
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
    assert len(notaccept.text) == 42
