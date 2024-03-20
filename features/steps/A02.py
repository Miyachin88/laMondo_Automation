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
from func import susa

#ドライバのインストール
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver = susa.installD()

"""
A02基本設定をする Set Basic Settings
https://jaqool.atlassian.net/browse/GPT-759
"""

#@BDDTEST-GPT-760
#Scenario: [A02-01]ウィジェットを表示する Show widget
#https://jaqool.atlassian.net/browse/BBS-65

#
@given('ゲスト画面にウィジェットが表示されていない / The widget is not displayed on the guest screen')
def chinsara_G(chinsara):
    time.sleep(5)    
    #基本設定へ移動
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]').click()
    #基本設定のタブに移動
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[3]/div/div/button').click()
    time.sleep(5)
    #日本語を選択
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/div/div').click()
    time.sleep(5)  
#
@when('「すべてのウィジェットを有効にする。」のトグルをONにする / Turn on the toggle for "Enable all widgets."')
def chinsara_W(chinsara):
    #ウィジェットをON
    toggle_button = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div')))
    #一度OFF
    toggle_button.click()
    #再度ON
    time.sleep(10)
    toggle_button.click()
    print('A02-1OK')
    #ウィジェット設定へ移動
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()
    time.sleep(10)
    #infoボタンをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[1]/td[6]/div/div/button').click()
    driver.switch_to.window
    time.sleep(15)
    #ウィジェットを開く
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div[2]').click()
    time.sleep(10)   # 'toggle-button-id'はトグルボタンのID
#
@then('ゲスト画面で該当のウィジェットが表示されている / The corresponding widget is displayed on the guest screen')
def chinsara_T(chinsara):
    tab_handles = driver.window_handles
    # 2番目のタブに切り替える
    second_tab_handle = tab_handles[1]
    driver.switch_to.window(second_tab_handle)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(30)
    print(driver.current_url)
    #element = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    #driver.execute_script('arguments[0].click();', element)
    toggle_button = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/div/div[1]/div/main/div/div/div[2]/div/div/div[1]/div/div[2]')))
    element = toggle_button.text
    print(element)
    assert ('あごぽよクリーニング香椎本店のチャットボットへようこそ！チャットサービスはlaMondoを搭載しています。' == element) is True
    
@then('ゲスト画面を開くと、通常フローでGPT・スタッフに問い合わせが送信できる')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH,'/html/body/span/div/div[1]/div/main/div/div/div[2]/div/div/div[6]/div/button')
    driver.execute_script('arguments[0].click();', element)
    hellomsg = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/div/div[1]/div/main/div/div/div[2]/div[1]/div/div[8]/div/div[2]')))
    element = hellomsg.text
    assert ('こんにちは！laMondoがなんでもお答えします！From あごぽよ' == element) is True    


#@BDDTEST-GPT-761
#Scenario: [A02-02]ウィジェットを非表示にする Hide widget
#https://jaqool.atlassian.net/browse/BBS-65

#
@given('ゲスト画面にウィジェットが表示されている / The widget is displayed on the guest screen')
def chinsara_G(chinsara):
    #現在のURLがhttps://beta-tenant-admin.im.kotozna.chat/ja/laMondo/widgetSetting
    print(chinsara)
#
@when('「すべてのウィジェットを有効にする。」のトグルをOFFにする / Turn off the toggle for "Enable all widgets."')
def chinsara_W(chinsara):
    toggle_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/thead/tr/th[3]/div/div/div/div[1]/div/div/div[2]/input')))  # 'toggle-button-id'はトグルボタンのID
# トグルボタンをクリックしてONにする
    if not toggle_button.is_selected():
        toggle_button.click()
#
@then('ゲスト画面で該当のウィジェットが表示されていない / The widget is not displayed on the guest screen')
def chinsara_T(chinsara):
    print(chinsara)

#
@then('ゲスト画面を開くと、「チャット機能は現在ご利用できません」が表示される')
def chinsara_T(chinsara):
    print(chinsara)


#@BDDTEST-GPT-762
#[A02-03]ゲストによる回答評価の利用を有にする（Survey）Make use of guest response evaluation (Survey)
#https://jaqool.atlassian.net/browse/BBS-65

#
@given('"チャット終了後の「ゲスト評価」を利用する。"トグルがOFFになっている "Use the guest evaluation after the chat. " is OFF')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('ステップ④ゲストによる評価の「ゲストによる評価を利用する」がOFFになっている')
def chinsara_W(chinsara):
    time.sleep(3)
#
@then('"チャット終了後の「ゲスト評価」を利用する。"のトグルをONにする Turn on the "Use the guest evaluation after the chat."')
def chinsara_T(chinsara):
    print(chinsara)
#
@then('ステップ④ゲストによる評価の「ゲストによる評価を利用する」がONになる')
def chinsara_T(chinsara):
    print(chinsara)


#@BDDTEST-GPT-763
#[A02-04]ゲストによる回答評価の利用を無にする（Survey）Eliminate the use of guest response ratings (Survey)
#https://jaqool.atlassian.net/browse/BBS-65

#
@given('"チャット終了後の「ゲスト評価」を利用する。"トグルがONになっている""Use the" guest evaluation "after the chat. " is ON"')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('「チャット終了後の「ゲスト評価」を利用する。」のトグルをOFFにする"Use the" guest evaluation "after the chat. Toggle off"')
def chinsara_W(chinsara):
    time.sleep(3)
#
@then('ゲスト画面で、チャット終了後に回答評価が表示されなくなる On the guest screen, the answer rating is no longer displayed after the chat ends')
def chinsara_T(chinsara):
    print(chinsara)


#@BDDTEST-GPT-764
#[A02-05]WorkCodeを追加する Add work code
#https://jaqool.atlassian.net/browse/BBS-65

#
@given('基本設定画面のワークコードマスタに、現在登録されているワークコード一覧が表示されている / A list of work codes currently registered in the work code master is displayed.')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('「＋」ボタンを押し、ワークコード名を入力して保存する / Press the "+" button, enter a name and save')
def chinsara_W(chinsara):
    time.sleep(3)
#
@then('ワークコード一覧に数字→アルファベット→ひらがな→漢字の順に新たなワークコードが追加され、スタッフ画面にも同様に表示される / A new work code is added to the work code list in the order of numbers → alphabet → hiragana → kanji, and the same is displayed on the staff screen.')
def chinsara_T(chinsara):
    print(chinsara)


#@BDDTEST-GPT-765
#[A02-06]WorkCodeを削除する Delete workcode
#https://jaqool.atlassian.net/browse/BBS-65

#
@given('ワークコードマスタに現在登録されているワークコード一覧が表示されている / A list of work codes currently registered in the work code master is displayed.')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('削除したいワークコードに✅をし、ごみ箱ボタンをクリックする  /✅  on the work code you want to delete and click the Recycle Bin button')
def chinsara_W(chinsara):
    time.sleep(3)
#
@then('ワークコード一覧から削除され、スタッフ画面にも反映されている / It has been deleted from the work code list and reflected on the staff screen.')
def chinsara_T(chinsara):
    print(chinsara)


#@BDDTEST-GPT-766
#[A02-07]WorkCodeを編集する Edit workcode
#https://jaqool.atlassian.net/browse/BBS-65

#
@given('ワークコードマスタに現在登録されているワークコード一覧が表示されている2 / A list of work codes currently registered in the work code master is displayed.')
def chinsara_G(chinsara):
    print(chinsara)
#
@when('編集したいワークコードのペンシルマークをクリックし、名前を編集する / Click the pencil mark of the work code you want to edit, and edit name')
def chinsara_W(chinsara):
    time.sleep(3)
#
@then('どこかをクリックすると保存され、スタッフ画面にも反映されている / Click anywhere to save it and reflect it on the staff screen')
def chinsara_T(chinsara):
    print(chinsara)

