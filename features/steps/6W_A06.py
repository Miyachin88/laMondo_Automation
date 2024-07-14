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
# https://jaqool.atlassian.net/browse/GPT-1373
# 

@Given('Tenant Admin Panel System Message Setting is displayed1/ システムメッセージ設定画面を開いている')
def chinsara_G(chinsara):
    loginAdmin()
#
@When('Change text in "Chat Messages (When beginning a new chat)" / 初期メッセージ設定欄のメッセージを（テナント言語で）変更')
def chinsara_W(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[1]/div/div[3]/input').text
    if element != 'AW06-01のテスト':
        input_text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[1]/div/div[3]/input')     
        input_text.send_keys(Keys.COMMAND + "a" )
        input_text.send_keys( Keys.DELETE )
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[1]/div/div[3]/input').send_keys('W06-01のテスト')
#
@Then('Changed test is displayed1 (not saved yet)/ 変更値が表示されている（未保存）')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[1]/div/div[3]/input')
    chinsara = element.get_attribute('value')
    assert chinsara == "W06-01のテスト"
    
# [AW06-02]メッセージインプットプレースホルダーを変更する / Change Placeholder Message
# https://jaqool.atlassian.net/browse/GPT-1374
# 

@Given('Tenant Admin Panel System Message Setting is displayed2/ システムメッセージ設定画面を開いている')
def chinsara_G(chinsara):
    time.sleep(5)
#
@When('Change text in "Placeholder Message2" / メッセージインプットプレースホルダー設定欄のメッセージを（テナント言語で）変更する')
def chinsara_W(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[1]/form/div[2]/div[1]/div/div[3]/input').text
    if element != 'AW06-02のテスト':
        input_text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[1]/form/div[2]/div[1]/div/div[3]/input')
        input_text.send_keys(Keys.COMMAND + "a" )
        input_text.send_keys( Keys.DELETE )
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[1]/form/div[2]/div[1]/div/div[3]/input').send_keys('W06-02のテスト')
#
@Then('Changed test is displayed (not saved yet)/ 変更値が表示されている（未保存）')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[1]/form/div[2]/div[1]/div/div[3]/input')
    chinsara = element.get_attribute('value')
    assert chinsara == "W06-02のテスト"


# [AW06-03]サンプル質問をONにする Turn ON the Sample Questions
# https://jaqool.atlassian.net/browse/GPT-1375
# 

#
@Given('Tenant Admin Panel System Message Setting is displayed3/ システムメッセージ設定画面を開いている')
def chinsara_G(chinsara):
    print(chinsara)
#
@Given('Sample Questions switch is OFF/ サンプル質問のツイッチがオフになっている')
def chinsara_G(chinsara):
    toggle_switch = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div/div/div/div[2]/input')
    if toggle_switch.is_selected():    
        toggle_switch.click()
    else :
        time.sleep(3)
        
#
@When('Turn on "Sample Questions"/ サンプル質問のスイッチをONにする')
def chinsara_W(chinsara):
    toggle_switch = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div/div/div/div[2]/input')
    toggle_switch.click()
    time.sleep(10)
#
@Then('One input box and "+" button will appear/ サンプル質問の入力欄1つと"+"ボタンが表示される')
def chinsara_T(chinsara):
    wait = WebDriverWait(driver, 300)
    sample1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[4]/div[1]/form/div/div/div/div[3]/input')
    chinsara1 = sample1.get_attribute('placeholder')
    assert (chinsara1 == '例: 今日の天気はどうですか？')
    

# [AW06-04]サンプル質問を追加する Add Sample Questions
# https://jaqool.atlassian.net/browse/GPT-1236
# 

#サンプル質問の入力欄が1つ表示されている
@Given('One input box for custom questions for guest screen will appear/ サンプル質問の入力欄が1つ表示されている')
def chinsara_G(chinsara):
    print(chinsara)
    time.sleep(3)
#サンプル質問を（テナント言語で）入力する
@When('Input sample question in tenant language/ サンプル質問を（テナント言語で）入力する')
def chinsara_W(chinsara):
    sample1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[4]/div[1]/form/div/div/div/div[3]/input')
    sample1.send_keys(Keys.COMMAND + "a" )
    sample1.send_keys( Keys.DELETE )
    sample1.send_keys('W06-04のテスト1')
    time.sleep(3)
# 
@Then('"Save and Next" button becomes active/ "保存して次へ"ボタンがアクティブになっている')
def chinsara_T(chinsara):
    sample1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[4]/div[1]/form/div/div/div/div[3]/input')
    chinsara1 = sample1.get_attribute('value')
    assert (chinsara1 == "W06-04のテスト1")


# [AW06-05]サンプル質問を追加する Add Sample Questions
# https://jaqool.atlassian.net/browse/GPT-1325
# 

#サンプル質問がいくつか入力されている

@Given('Some sample questions are displayed1/ サンプル質問が入力されている')
def chinsara_G(chinsara):
    sample_toggle = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div/div/div/div[2]/input')
    if sample_toggle.is_selected():
        time.sleep(1)
#
@When('Press "+" to add an input field/ "+"を押下する')
def chinsara_G1(chinsara):
    for i in range(9):
        param1 = i + 5
        setparam = str(param1)
        addbutton = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[" + str(setparam) + "]/button"
        chinsara = driver.find_element(By.XPATH, addbutton)
        chinsara.click()
        time.sleep(1)    

#
@Then('Sample question input field is added up to 10 "+" button becomes gray out/ サンプル質問入力欄が10個まで追加でき、"+"ボタンはグレーアウトする')
def chinsara_T(chinsara):
    sample_toggle = driver.find_element(By.CSS_SELECTOR, '#lamondo-new-widget-initial-messages > div.lamondo-new-widget-initial-messages-content.mt-4 > div.app-button > button')
    assert not sample_toggle.is_selected()

# [AW06-06]追加したサンプル質問を入力する Input Sample Questions in added Sample Questions
# https://jaqool.atlassian.net/browse/GPT-1326
# 

#
@Given('Added sample question input fields are displayed and blank/ サンプル質問欄が追加され空欄である')
def chinsara_G(chinsara):
    print(chinsara)

#    
@When('Input sample question(s) in that input fields/ サンプル質問追加欄に質問を入力する')
def chinsara_W(chinsara):
    for i in range(9):
        param1 = i + 5
        setparam = str(param1)
        inputsampleq = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[" + str(setparam) + "]/div[1]/form/div/div/div/div[3]/input"
        chinsara = driver.find_element(By.XPATH, inputsampleq)
        tintin = i + 2
        tintinstr = str(tintin)        
        chinsara.send_keys('W06-06のテスト'+ tintinstr)
        time.sleep(1)
#
@Then('Added sample questions are displayed (not saved yet)/ 追加されたサンプル質問が表示されている')
def chinsara_T(chinsara):
    sample1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[13]/div[1]/form/div/div/div/div[3]/input')
    chinsara1 = sample1.get_attribute('value')
    assert (chinsara1 == "W06-06のテスト10")
#
@Then('"Save and Next" button becomes active2/ "保存して次へ"ボタンがアクティブになっている')
def chinsara_T(chinsara):
    sample_toggle = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button')
    assert sample_toggle.is_enabled()


# [AW06-07]サンプル質問表示中もメッセージ入力欄を表示する
# https://jaqool.atlassian.net/browse/GPT-1379
# 

#
@Given('Toggle of Display message input field when displaying sample questions is "OFF"  / ウィジェット設定にてサンプル質問表示中もメッセージ入力欄を表示するのトグルがOFF')
def chinsara_G(chinsara):
    # サンプル質問表示中もメッセージ入力欄を表示するのトグルをOFFにする
    toggle_switch = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div/div/div[2]/input')
    if toggle_switch.is_selected():    
        toggle_switch.click()

#
@When('Change toggle of Display message input field when displaying sample questions is "ON"/ サンプル質問表示中もメッセージ入力欄を表示するのトグルをONにする')
def chinsara_W(chinsara):
    # サンプル質問表示中もメッセージ入力欄を表示するのトグルをONにする
    toggle_switch = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div/div/div[2]/input') 
    toggle_switch.click()
    # 自動化用のウィジェットの③不在時のメール受信設定にて”保存して閉じます”をクリックしてウィジェット設定へ移動
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
    time.sleep(10)
    
    # ウィジェットを開く
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
    time.sleep(10)
    # スタートボタンを押下
    element = driver.find_element(By.XPATH,'/html/body/span/div/div[1]/div/main/div/div/div[2]/div/div/div[7]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(15)
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]')
    element.send_keys('W06-07のテスト')
#
@Then('Sample message and message input box are displayed if you open guest screen / ゲスト画面を開くとサンプルメッセージおよびメッセージのテキストボックスが表示されている')
def chinsara_T(chinsara):
    sample1 = driver.find_element(By.XPATH, '/html/body/span/div/div[1]/div/main/div/div/div[2]/div[2]/div/textarea')
    chinsara1 = sample1.get_attribute('value')
    assert (chinsara1 == "W06-07のテスト")


# [AW06-08]サンプル質問表示中もメッセージ入力欄を表示しない
# https://jaqool.atlassian.net/browse/GPT-1380
# 

#
@Given('Toggle of Display message input field when displaying sample questions is "ON"  / ウィジェット設定にてサンプル質問表示中もメッセージ入力欄を表示するのトグルが"ON"')
def chinsara_G(chinsara):
    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    second_tab_handle = tab_handles[0]
    driver.switch_to.window(second_tab_handle)
    #戻るを押下
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[4]/div[2]/button').click()
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
    
#
@When('Change toggle of Display message input field when displaying sample questions is "OFF"/ サンプル質問表示中もメッセージ入力欄を表示するのトグルを"OFF"にする')
def chinsara_W(chinsara):
    # サンプル質問表示中もメッセージ入力欄を表示するのトグルをOFFにする
    toggle_switch = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div/div/div[2]/input')
    if toggle_switch.is_selected():    
        toggle_switch.click()
#
@Then('Message input box is NOT displayed if you open guest screen / ゲスト画面を開くとメッセージのテキストボックスが表示されない')
def chinsara_T(chinsara):
    # 自動化用のウィジェットの③不在時のメール受信設定にて”保存して閉じます”をクリックしてウィジェット設定へ移動
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
    time.sleep(10)
    
    # ウィジェットを開く
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
    element = driver.find_element(By.XPATH,'/html/body/span/div/div[1]/div/main/div/div/div[2]/div/div/div[7]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(15)
    judge = "true"
    try:
        # 指定したDiv要素を検索
        driver.find_element(By.ID, "inputMessage").send_keys('W06-08のテスト')
    except NoSuchElementException:
        judge = "false"
    
    assert judge == "false"
    
    #最後にタブを閉じて初期化する
    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    second_tab_handle = tab_handles[0]
    driver.switch_to.window(second_tab_handle)
    #戻るを押下
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[4]/div[2]/button').click()
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
    
    # サンプル質問を全て削除する
    for _ in range(10):
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[4]/div[2]/button').click()
        time.sleep(3)
    
    # サンプル質問表示中もメッセージ入力欄を表示するのトグルをOFFにする
    toggle_switch = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div/div/div[2]/input')
    if not toggle_switch.is_selected():    
        toggle_switch.click()
    
    # 自動化用のウィジェットの③不在時のメール受信設定にて”保存して閉じます”をクリックしてウィジェット設定へ移動
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
    time.sleep(5)
    
# [AW06-09]システムメッセージ設定の保存
# https://jaqool.atlassian.net/browse/GPT-1381
# 

#
@Given('Tenant Admin Panel System Message Setting is displayed4/ システムメッセージ設定画面を開いている')
def chinsara_G(chinsara):
    print(chinsara)
#
@Given('Texts are displayed in "Chat Messages (When beginning a new chat)", "Placeholder Message" field and "Sample Questions" field/ 初期メッセージ、メッセージインプットプレースホルダー、サンプル質問設定欄に文章が入力されている')
def chinsara_G(chinsara):
    print(chinsara)
#
@When('Press "SAVE AND NEXT" / "保存して次へ"を押下')
def chinsara_W(chinsara):
    time.sleep(3)
#
@Then('Design Setting screen is displayed/ デザイン設定画面に遷移する')
def chinsara_T(chinsara):
    print(chinsara)
#
@Then('System Messages of all widgets in this tenant are changed/ 管理画面上でシステムメッセージが変更されている＊同テナント全てのウィジェット')
def chinsara_T(chinsara):
    print(chinsara)
#
@Then('Sample Questions are displayed/ 管理画面上でサンプル質問が表示されている＊該当ウィジェットのみ')
def chinsara_T(chinsara):
    print(chinsara)
#
@Then('On the guest screen, "Chat Messages (When beginning a new chat)" and "Placeholder Message" are changed/ ゲスト画面で初期メッセージとメッセージ入力欄のメッセージが変更されている')
def chinsara_T(chinsara):
    print(chinsara)

#
@Then('On the guest screen,  "Chat Messages (When beginning a new chat)" and "Placeholder Message" are translated in the guest device language/ ゲスト画面で初期メッセージとメッセージ入力欄のメッセージが端末言語に機械翻訳されている')
def chinsara_T(chinsara):
    print(chinsara)
