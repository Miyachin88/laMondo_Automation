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
Create New Widget Step ❺　システムメッセージ設定
https://jaqool.atlassian.net/browse/GPT-1056
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
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('kenta+gpt-adminoshima-3096@kotozna.com')
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

# [AW06-01]初期メッセージを変更する / Change Chat Messages
# https://jaqool.atlassian.net/browse/GPT-339
# 

@given('Tenant Admin Panel System Message Setting is displayed1/ システムメッセージ設定画面を開いている')
def chinsara_G(chinsara):
    loginAdmin()
#
@when('Change text in "Chat Messages (When beginning a new chat)" / 初期メッセージ設定欄のメッセージを（テナント言語で）変更')
def chinsara_W(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[1]/div/div[3]/input').text
    if element != 'AW06-01のテスト':
        input_text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[1]/div/div[3]/input')     
        input_text.send_keys(Keys.COMMAND + "a" )
        input_text.send_keys( Keys.DELETE )
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[1]/div/div[3]/input').send_keys('W06-01のテスト')
#
@then('Changed test is displayed1 (not saved yet)/ 変更値が表示されている（未保存）')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[1]/div/div[3]/input')
    chinsara = element.get_attribute('value')
    assert chinsara == "W06-01のテスト"
    
# [AW06-02]メッセージインプットプレースホルダーを変更する / Change Placeholder Message
# https://jaqool.atlassian.net/browse/GPT-340
# 

@given('Tenant Admin Panel System Message Setting is displayed2/ システムメッセージ設定画面を開いている')
def chinsara_G(chinsara):
    time.sleep(5)
#
@when('Change text in "Placeholder Message2" / メッセージインプットプレースホルダー設定欄のメッセージを（テナント言語で）変更する')
def chinsara_W(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[1]/form/div[2]/div[1]/div/div[3]/input').text
    if element != 'AW06-02のテスト':
        input_text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[1]/form/div[2]/div[1]/div/div[3]/input')
        input_text.send_keys(Keys.COMMAND + "a" )
        input_text.send_keys( Keys.DELETE )
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[1]/form/div[2]/div[1]/div/div[3]/input').send_keys('W06-02のテスト')
#
@then('Changed test is displayed (not saved yet)/ 変更値が表示されている（未保存）')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[1]/form/div[2]/div[1]/div/div[3]/input')
    chinsara = element.get_attribute('value')
    assert chinsara == "W06-02のテスト"




# [AW06-03]サンプル質問をONにする Turn ON the Sample Questions
# https://jaqool.atlassian.net/browse/GPT-1235
# 

#
@given('Tenant Admin Panel System Message Setting is displayed3/ システムメッセージ設定画面を開いている')
def chinsara_G(chinsara):
    print(chinsara)
#
@given('Sample Questions switch is OFF/ サンプル質問のツイッチがオフになっている')
def chinsara_G(chinsara):
    toggle_switch = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div/div/div[2]/input')
    if toggle_switch.is_selected():    
        toggle_switch.click()
        
#
@when('Turn on "Sample Questions"/ サンプル質問のスイッチをONにする')
def chinsara_W(chinsara):
    toggle_switch = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div/div/div[2]/input')
    toggle_switch.click()
    time.sleep(10)
#
@then('Three input boxes for custom questions for guest screen will appear/ サンプル質問の入力欄が3つ表示される')
def chinsara_T(chinsara):
    wait = WebDriverWait(driver, 300)
    sample1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[4]/form/div/div[1]/div/div[3]/input')
    chinsara1 = sample1.get_attribute('placeholder')
    sample2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[5]/form/div/div[1]/div/div[3]/input')
    chinsara2 = sample1.get_attribute('placeholder')
    sample2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[6]/form/div/div[1]/div/div[3]/input')
    chinsara3 = sample1.get_attribute('placeholder')
    assert (chinsara1 == '例: 今日の天気はどうですか？') & (chinsara2 == '例: 今日の天気はどうですか？') & (chinsara3 == "例: 今日の天気はどうですか？")
    

# [AW06-04]サンプル質問を追加する Add Sample Questions
# https://jaqool.atlassian.net/browse/GPT-1236
# 

@given('Three input boxes for custom questions for guest screen will appear/ サンプル質問の入力欄が3つ表示されている')
def chinsara_G(chinsara):
    print(chinsara)
    time.sleep(3)
#
@when('Input one or two sample question(s) in tenant language/ サンプル質問を1つまたは2つ（テナント言語で）入力する')
def chinsara_W(chinsara):
    sample1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[4]/form/div/div[1]/div/div[3]/input')
    sample1.send_keys(Keys.COMMAND + "a" )
    sample1.send_keys( Keys.DELETE )
    sample1.send_keys('W06-04のテスト1')
    sample2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[5]/form/div/div[1]/div/div[3]/input')
    sample2.send_keys(Keys.COMMAND + "a" )
    sample2.send_keys( Keys.DELETE )
    sample2.send_keys('W06-04のテスト2')
    sample3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[6]/form/div/div[1]/div/div[3]/input')
    sample3.send_keys(Keys.COMMAND + "a" )
    sample3.send_keys( Keys.DELETE )
    sample3.send_keys('W06-04のテスト3')
    time.sleep(3)
#
@then('"Save and Next" button becomes active/ "保存して次へ"ボタンがアクティブになっている')
def chinsara_T(chinsara):
    sample1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[4]/form/div/div[1]/div/div[3]/input')
    chinsara1 = sample1.get_attribute('value')
    sample2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[5]/form/div/div[1]/div/div[3]/input')
    chinsara2 = sample2.get_attribute('value')
    sample3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[6]/form/div/div[1]/div/div[3]/input')
    chinsara3 = sample3.get_attribute('value')
    assert (chinsara1 == "W06-04のテスト1") & (chinsara2 == "W06-04のテスト2") & (chinsara3 == "W06-04のテスト3")
    
# [AW06-05]システムメッセージ設定の保存
# https://jaqool.atlassian.net/browse/GPT-1055
# 

#
@given('Tenant Admin Panel System Message Setting is displayed4/ システムメッセージ設定画面を開いている')
def chinsara_G(chinsara):
    print(chinsara)
#
@given('Texts are displayed in "Chat Messages (When beginning a new chat)", "Placeholder Message" field and "Sample Questions" field/ 初期メッセージ、メッセージインプットプレースホルダー、サンプル質問設定欄に文章が入力されている')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('Press "SAVE AND NEXT" / "保存して次へ"を押下')
def chinsara_W(chinsara):
    time.sleep(3)
#
@then('Design Setting screen is displayed/ デザイン設定画面に遷移する')
def chinsara_T(chinsara):
    print(chinsara)
#
@then('On the guest screen, "Chat Messages (When beginning a new chat)" and "Placeholder Message" are changed/ ゲスト画面の初期メッセージとメッセージ入力欄のメッセージが変更されている')
def chinsara_T(chinsara):
    print(chinsara)
#
@then('System Messages of all widgets in this tenant are changed/ システムメッセージが変更されている＊同テナントのウィジェット全て')
def chinsara_T(chinsara):
    print(chinsara)
#
@then('Sample Questions are displayed/ サンプル質問が表示されている＊同テナントのウィジェット全て')
def chinsara_T(chinsara):
    print(chinsara)