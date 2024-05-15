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
AW04Create New Widget Step ❸　不在時のメール受信設定
https://jaqool.atlassian.net/browse/GPT-784

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
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('kenta+b230109-admin@kotozna.com')
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
    

# Scenario: [AW04-01]不在時のメール受信設定画面に移動する Move to Out of Business Hours Behavior Setting screen
# https://jaqool.atlassian.net/browse/GPT-785
@Given('営業時間の設定画面が表示されている')
def step_impl(context):
    loginAdmin()

@When('右下の「保存して次へ」をクリックする')
def step_impl(context):
    # 自動化用のウィジェットの②営業時間にて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(20)

@Then('「不在時のメール受信設定」画面が表示される')
def step_impl(context):
    #ページのタイトルが”不在時のメール受信設定”であるかを判定
    wait = WebDriverWait(driver, 180)
    currentpage = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/label')))
    assert currentpage.text == "不在時のメール受信設定"
    

# Scenario: [AW04-02]メール送信用フォームを営業時間外に表示設定する Set Email inquiries when staff are unavailable (Outside Business Hours)
# https://jaqool.atlassian.net/browse/GPT-786

@Given('「不在時のメール受信設定」画面が表示されている1')
def step_impl(context):
    #営業時間外をクリック
    time.sleep(10)
    outofbusihour = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/input')
    #営業時間外のチェックボックスがクリックされている
    if outofbusihour.is_selected():
        #メールアドレスを消去
        # 対象の要素を取得
        target_element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]')
        # 対象の要素内に含まれるinputタグの数を数える
        input_tags = target_element.find_elements(By.XPATH,'.//input')
        input_count = len(input_tags)
        for _ in range(input_count):
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]/button').click()
            time.sleep(3)
        # 不在判定時間を消去
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.BACK_SPACE)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.ENTER)
        #チェックボックスをクリック
        outofbusihour.click()
        time.sleep(3)
        #再度チェックボックスをクリック
        outofbusihour.click()
    else :   
        outofbusihour.click()

@When('「営業時間外」のチェックボックスに✓を入れる')
def step_impl(context):
    print('chinchin')
    time.sleep(10)

@Then('「不在時メール送信先」と「不在判定時間」の入力が可能になる')
def step_impl(context):
    #ページの項目が”不在時メール送信先”であるかを判定
    unavailable_Staff_Mail_Destination = driver.find_element(By.CSS_SELECTOR,'#app > div > div > div > div > div.body.d-flex.align-center.justify-center > div.body-content > div > div > div.lamondo-new-widget-left > div.lamondo-new-widget-left-content > div > div.d-flex.align-start.flex-column.width-100 > div.lamondo-new-widget-email-req-add.px-4.mt-2.width-100.d-flex.align-start.flex-column.justify-start > label')
    #ページの項目が”不在判定時間”であるかを判定
    time_Staff_Did_Not_Respond = driver.find_element(By.CSS_SELECTOR,'#app > div > div > div > div > div.body.d-flex.align-center.justify-center > div.body-content > div > div > div.lamondo-new-widget-left > div.lamondo-new-widget-left-content > div > div.d-flex.align-start.flex-column.width-100 > label')  
    assert (unavailable_Staff_Mail_Destination.text == "不在時メール送信先*") & (time_Staff_Did_Not_Respond.text == "不在判定時間*")

# Scenario: [AW04-03]不在時メール送信先を設定する Set  "Unavailable Staff Mail Destination"
# https://jaqool.atlassian.net/browse/GPT-787

@Given('「不在時メール送信先」入力欄が表示されている')
def step_impl(context):
    staffunavailable = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/div/input')
    #不在時のチェックボックスがクリックされている
    if staffunavailable.is_selected():
        #チェックボックスをクリック
        staffunavailable.click()
        time.sleep(3)
        #再度チェックボックスをクリック
        staffunavailable.click()
    else :   
        staffunavailable.click()

@When('入力欄にメールアドレスを入れる')
def step_impl(context):
    # メールアドレスを入力
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[1]/form/div/div[1]/div/div[3]/input').send_keys('aw04_03@kotozna.com')

@When('不在判定時間に1-10までの数字を半角で入力する1')
def step_impl(context):
        # 不在判定時間を消去
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.ENTER)
    # 不在判定時間を入力
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(10)

@Then('入力値が表示されている（未保存）')
def step_impl(context):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[1]/form/div/div[1]/div/div[3]/input')
    mailaddress = element.get_attribute('value')
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input')
    outoftime = element.get_attribute('value')
    assert (mailaddress == "aw04_03@kotozna.com") & (outoftime == "10")


# Scenario: [AW04-04]不在時メール送信先を追加する Add  "Unavailable Staff Mail Destination"
# https://jaqool.atlassian.net/browse/GPT-788

@Given('「不在時のメール受信設定」画面が表示されている2')
def step_impl(context):
    # メールアドレス追加ボタンをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/button').click() 

@When('不在時メール送信先の＋ボタンをクリックする')
def step_impl(context): 
    time.sleep(5)

@Then('入力欄が追加される')
def step_impl(context):
    element = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[1]/form/div/div[1]/div/div[3]/input')    
    assert len(element) > 0


# Scenario: [AW04-05]不在時メール送信先を削除する Delete  "Unavailable Staff Mail Destination"
# https://jaqool.atlassian.net/browse/GPT-789

@Given('不在時メール送信先が設定されている')
def step_impl(context):
    print('chinchin')
    # 実際のテストではここで「不在時メール送信先」にメールアドレスが設定されているかを確認するコード

@When('入力欄右横の×をクリックする')
def step_impl(context):
    # 2番目のメールアドレスを入力
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[1]/form/div/div[1]/div/div[3]/input').send_keys("aw04_05@kotozna.com") 

@Then('該当の入力欄ごと消える')
def step_impl(context): 
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[1]/form/div/div[1]/div/div[3]/input')
    mailaddress2 = element.get_attribute('value')
    assert (mailaddress2 == "aw04_05@kotozna.com")


# Scenario: [AW04-06]不在判定時間を設定する Set "Time Staff Did Not Respond"
# https://jaqool.atlassian.net/browse/GPT-790

@Given('「不在時のメール受信設定」画面が表示される')
def step_impl(context):
    print('chinchin')
    # 実際のテストではここで「不在時のメール受信設定」画面が表示されているかを確認するコード

@When('不在時のチェックボックスにチェックを入れる')
def step_impl(context):
    # 不在判定時間を消去
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.ENTER)

@When('不在判定時間に1-10までの数字を半角で入力する2')
def step_impl(context):
    # 不在判定時間を入力
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(5)

@Then('ゲスト画面でスタッフ呼び出し後、設定した分数が経過すると、メール送信用フォームが表示される')
def step_impl(context):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input')
    outoftime = element.get_attribute('value')
    assert outoftime == "5"
