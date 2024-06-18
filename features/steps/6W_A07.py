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
    time.sleep(10)
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
    # 自動化用のウィジェットの⑤システムメッセージ設定にて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)    
    

# [AW07-01]ウィジェットロゴを設定する Set Widget Logo
# https://jaqool.atlassian.net/browse/GPT-341
# 

@given('「❻デザイン設定」画面が表示されている1 ❻Design Setting screen is displayed')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('ウィジェットロゴの「ロゴを変更」をクリックし、画像データをアップロードするSelect "Change Logo" and upload an image to be used')
def chinsara_W(chinsara):
    time.sleep(3)
#
@then('表示サンプルが選択したウィジェットロゴにて表示される。Preview displays selected widget logo, widget logo is set')
def chinsara_T(chinsara):
#最初に表示サンプルのロゴのリンクを取得
    firstsampleimage = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[6]/div[1]/div[1]/div[1]/img')
    image1 = firstsampleimage.get_attribute('currentSrc')
    print(image1)
    #画像を選択してアップ
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/input').send_keys('/Users/kentamiyachi/PythonPro/laMondo/other/pompom1.jpeg')
    time.sleep(15)
    secondsampleimage = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[6]/div[1]/div[1]/div[1]/img')
    image2 = secondsampleimage.get_attribute('currentSrc')
    print(image2)
    assert image1 != image2
    
# [AW07-02]チャットヘッダーの色を選択する Select Chat Header Color
# https://jaqool.atlassian.net/browse/GPT-342
# 

#
@given('「❻デザイン設定」画面が表示されている2Design Setting screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('チャットヘッダーの色を既存の色から選択する。Select chat header color from existing colors')
def chinsara_W(chinsara):
    element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[1]/div[1]')
    # 要素のクラス属性を取得
    class_attribute = element.get_attribute("class")
    #赤の時は緑に、それ以外は赤に変更
    if class_attribute == "mx-2 lamondo-new-widget-design-color-selected":
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[1]/div[4]').click()
    else :
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[1]/div[1]').click()
#
@then('表示サンプルのチャットヘッダーとウィジェットアイコンが選択した色にて表示される1。Preview displays selected chat color, chat color is set')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[1]/div[1]')
    # 要素のクラス属性を取得
    class_attribute = element.get_attribute("class")
    backcolor = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[6]/div[1]/div[1]')
    header_color = backcolor.value_of_css_property("background")
    colorjudge = header_color[:16]
    #赤の時
    if class_attribute == "mx-2 lamondo-new-widget-design-color-selected":
        assert colorjudge == "rgb(234, 84, 50)"
    else :
        assert colorjudge == "rgb(0, 215, 167)"




# [AW07-03]チャットヘッダーの色をカスタム設定する Create Custom Chat Header Color
# https://jaqool.atlassian.net/browse/GPT-343
# 

#
@given('「❻デザイン設定」画面が表示されている3 Design Setting screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('"カスタム"の横の入力欄に、6桁のHEXコードを入力する、またはカラーシートから選択するSelect input box next to custom and input 6 digit color HEX code, or select color box next to "Custom"and set')
def chinsara_W(chinsara):
    input_text = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[1]/input[2]')
    input_text.send_keys(Keys.COMMAND + "a" )
    input_text.send_keys( Keys.DELETE )
    input_text.send_keys("#222222")
    time.sleep(5)
#
@then('表示サンプルのチャットヘッダーとウィジェットアイコンが選択した色にて表示される2。Preview displays set chat color, chat color is set')
def chinsara_T(chinsara):
    backcolor = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[6]/div[1]/div[1]')
    header_color = backcolor.value_of_css_property("background")
    colorjudge = header_color[:15]
    #赤の時
    assert colorjudge == "rgb(34, 34, 34)"
    

# [AW07-04]チャットアイコンを設定する Set Chat Icon Image Setting
# https://jaqool.atlassian.net/browse/GPT-344
# 

#
@given('「❻デザイン設定」画面が表示されている4Design Setting screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('「アイコン設定」の「アイコンを変更」から画像をアップロードするSelect "Change Icon" and upload an image to be used')
def chinsara_W(chinsara):
    time.sleep(3)
#
@then('表示サンプルが選択したアイコンにて表示される1。Preview displays selected icon, icon is set')
def chinsara_T(chinsara):
    #アイコン設定のリンクを取得
    firstsampleimage = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[6]/div[1]/div[2]/div[1]/img')
    image1 = firstsampleimage.get_attribute('currentSrc')
    print(image1)
    #画像を選択してアップ
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[3]/input').send_keys('/Users/kentamiyachi/PythonPro/laMondo/other/pompom1.jpeg')
    time.sleep(15)
    secondsampleimage = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[6]/div[1]/div[2]/div[1]/img')
    image2 = secondsampleimage.get_attribute('currentSrc')
    print(image2)
    assert image1 != image2
    
# [AW07-05]ウィジェットアイコンを設定する Set Widget Icon Image Setting
# https://jaqool.atlassian.net/browse/GPT-907
# 

#
#
@given('「❻デザイン設定」画面が表示されている5 ❻Design Setting screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('ウィジェットが閉じている時のアイコンの「アイコンを変更」をクリックし、画像データをアップロードするSelect ""Change Icon"" and upload an image to be used')
def chinsara_W(chinsara):
    print('chinsara')
#
@then('表示サンプルが選択したアイコンにて表示される2。Preview displays selected widget icon, widget icon is set')
def chinsara_T(chinsara):
    #アイコン設定のリンクを取得
    firstsampleimage = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[6]/div[2]/div[2]/img')
    image1 = firstsampleimage.get_attribute('currentSrc')
    print(image1)
    #画像を選択してアップ
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[1]/div[2]/input').send_keys('/Users/kentamiyachi/PythonPro/laMondo/other/pompom1.jpeg')
    time.sleep(15)
    secondsampleimage = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[6]/div[2]/div[2]/img')
    image2 = secondsampleimage.get_attribute('currentSrc')
    print(image2)
    assert image1 != image2
    
# [AW07-06]ウィジェットアイコンのサイズを大きくする
# https://jaqool.atlassian.net/browse/GPT-908
# 

#
#
@given('「❻デザイン設定」画面が表示されている6 Design Setting screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('アイコンサイズ(px)の＋を押下1 Press "+" of Icon size(px)')
def chinsara_W(chinsara):
    #アイコンサイズが120px以外であったときに、120pxになるようにボタンを押下
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[2]/div[2]/input')    
    chinsara = element.get_attribute('value')

    if chinsara != "120":
        for _ in range(95):
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[2]/div[2]/button[2]').click()
    time.sleep(3)        
#
@then('表示サンプルのウィジェットアイコンサイズが変わる1 Preview displays changed size, widget icon on Web page is set')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[6]/div[2]/div[2]/img')   
    image_width = element.value_of_css_property("width")
    assert image_width == "120px"
    
# [AW07-07]ウィジェットアイコンのサイズを小さくする
# https://jaqool.atlassian.net/browse/GPT-909
# 

#
#
@given('「❻デザイン設定」画面が表示されている7 Design Setting screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('アイコンサイズ(px)の "-" を押下2 Press "-" of Icon size(px)')
def chinsara_W(chinsara):
    #アイコンサイズが25px以外であったときに、25pxになるようにボタンを押下
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[2]/div[2]/input')    
    chinsara = element.get_attribute('value')

    if chinsara != "25":
        for _ in range(95):
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[2]/div[2]/button[1]').click()
    time.sleep(3)  
#
@then('表示サンプルのウィジェットアイコンサイズが変わる2 Preview displays changed size, widget icon on Web page is set')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[6]/div[2]/div[2]/img')  
    image_width = element.value_of_css_property("width")
    assert image_width == "25px"
    
# [AW07-08]ウィジェットアイコンのフォントサイズを大きくする
# https://jaqool.atlassian.net/browse/GPT-910
# 

#
#
@given('「❻デザイン設定」画面が表示されている8 Design Setting screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('フォントサイズ(px)の"＋"を押下1 Press "+" of Icon size(px)')
def chinsara_W(chinsara):
    #フォントサイズが26px以外であったときに、26になるようにボタンを押下
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[3]/div[2]/input')    
    chinsara = element.get_attribute('value')

    if chinsara != "26":
        for _ in range(16):
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[3]/div[2]/button[2]').click()
    time.sleep(3)          

    
#
@then('表示サンプルのウィジェット上「チャットする」のフォントサイズが変わる1 Preview displays changed size, widget icon on Web page is set')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[6]/div[2]/div[1]/span')   
    font_size = element.value_of_css_property("font-size")
    assert font_size == "26px"
    
# [AW07-09]ウィジェットアイコンのフォントサイズを小さくする
# https://jaqool.atlassian.net/browse/GPT-911
# 

#
#
@given('「❻デザイン設定」画面が表示されている9 Design Setting screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('フォントサイズ(px)の "-" を押下2 Press "-" of Icon size(px)')
def chinsara_W(chinsara):
    #フォントサイズが10px以外であったときに、26になるようにボタンを押下
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[3]/div[2]/input')    
    chinsara = element.get_attribute('value')

    if chinsara != "10":
        for _ in range(16):
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[3]/div[2]/button[1]').click()
    time.sleep(3)        
#
@then('表示サンプルのウィジェット上「チャットする」のフォントサイズが変わる2 Preview displays changed size, widget icon on Web page is set')
def chinsara_T(chinsara):
    element = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div > div > div.body.d-flex.align-center.justify-center > div.body-content > div > div > div.lamondo-new-widget-left > div.lamondo-new-widget-left-content > div > div.d-flex.align-start.flex-column.justify-start.mt-4.width-100 > div.d-flex.align-start.justify-start > div.lamondo-new-widget-icon-preview > div.lamondo-new-widget-icon-preview-tip.pa-4.mb-2 > span')   
    font_size = element.value_of_css_property("font-size")
    assert font_size == "10px"


# [AW07-10]ウィジェットメッセージを変更する Change the Widget Message
# https://jaqool.atlassian.net/browse/GPT-1237
# 

#
#
@given('「「❻デザイン設定」画面が表示されている10 ❻Design Setting screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)
    
@given('ウィジェットメッセージ欄に「チャットする」と表示されている')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('ウィジェットメッセージ欄の文言を（テナント言語で）変更する　Change the text in the "Widget Message" input field in tenant language')
def chinsara_W(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[4]/div[2]/div/form/div/div[1]/div/div[3]/input').text
    if element != 'W07-10のテスト':
        input_text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[4]/div[2]/div/form/div/div[1]/div/div[3]/input')
        input_text.send_keys(Keys.COMMAND + "a" )
        input_text.send_keys( Keys.DELETE )
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[4]/div[2]/div/form/div/div[1]/div/div[3]/input').send_keys('W07-10のテスト')
        time.sleep(10)
#
@then('変更値が表示サンプルに表示されている（未保存)　Changed text is displayed (not saved yet)')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[3]/div[1]/form/div[2]/div[1]/div/div[3]/input')
    chinsara = element.get_attribute('value')
    assert chinsara == "W07-10のテスト"

# [AW07-11]ウィジェットアイコンのフォントサイズを小さくする
# https://jaqool.atlassian.net/browse/GPT-911
# 

#
#
@given('ウィジェットメッセージ欄に変更済みの文言が表示されている　Changed text is displayed in the "Widget Message" input field (not saved yet)')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('ウィジェットメッセージ入力欄横の"保存"を押下　Press "Save" next to the input field')
def chinsara_W(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[4]/div[2]/div/form/div/div[1]/div/div[3]/input').text
    if element != 'W07-11のテスト':
        input_text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[4]/div[2]/div/form/div/div[1]/div/div[3]/input')
        input_text.send_keys(Keys.COMMAND + "a" )
        input_text.send_keys( Keys.DELETE )
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[4]/div[4]/div[2]/div/form/div/div[1]/div/div[3]/input').send_keys('W07-11のテスト')
        #どこか適当にクリック(この場合は色のボタン)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[1]/div[4]').click()
#
@then('表示サンプルのウィジェットメッセージが書き換わる　Preview displays the changed text')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[6]/div[6]/div[2]/div[1]/span')
    chinsara = element.text
    assert chinsara == "W07-11のテスト"