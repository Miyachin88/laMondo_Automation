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
    element = driver.find_element(By.XPATH,'/html/body/span/div/div[1]/div/main/div/div/div[2]/div/div/div[7]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(15)    
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('こんにちは')
    time.sleep(10)
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
        
# [AW22-01]バリエーション設定画面を開く
# https://jaqool.atlassian.net/browse/GPT-717
# 

# 
@given('ウィジェット設定が開かれていて、登録済みのウィジェットがある')
def chinsara_G(chinsara):
    loginAdmin()
    cur_url = driver.current_url
    if 'https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/basicConfiguration' in cur_url:
        #ウィジェット設定へ移動
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()

    time.sleep(5)

#
@when('ウィジェット右側のロケーションアイコンを押下')
def chinsara_W(chinsara):
    #自動化用のウィジェットのロケーションアイコンをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[5]/div/div/button').click()
    time.sleep(5)
#
@then('バリエーション設定画面が表示される')
def chinsara_T(chinsara):
    cur_url = driver.current_url
    assert "https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/widgetSetting/widgetLocations" == cur_url
    
# [AW22-02]バリエーション追加ボタンを押す
# https://jaqool.atlassian.net/browse/GPT-718
# 

# 
@given('バリエーション設定画面が表示されている')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('右上のバリエーション追加ボタンを押下')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('バリエーションを追加するポップアップが表示される')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"
    
# [AW22-03] バリエーションの名前を入力する
# https://jaqool.atlassian.net/browse/GPT-719
# 

# 
@given('バリエーションを追加するポップアップが表示されていて名前欄が入力されていない')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('名前にValiation Name Aを入力する(例 Chanel)')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('名前欄にValiation Name Aが入力できる')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"
    
# [AW22-04] バリエーションを入力する
# https://jaqool.atlassian.net/browse/GPT-720
# 

# 
@given('バリエーションを追加するポップアップが表示されている')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('バリエーション欄にValiation Aを入力する(説明欄を参照)')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('バリエーション欄にValiation Aが入力できる')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"
    
# [AW22-05] バリエーションを保存する
# https://jaqool.atlassian.net/browse/GPT-721
# 

# 
@given('バリエーションを追加するの名前欄とバリエーション欄が入力されている')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('右下の"保存"ボタンを押下')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('バリエーション設定画面に、名前、バリエーション、スニペット、ゲスト画面URL、QRコードが生成され、追加される　＊画像参照')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"
    
# [AW22-11] スニペットのコピー＆ペースト
# https://jaqool.atlassian.net/browse/GPT-722
# 

# 
@given('バリエーション設定のスニペットの項目にスニペットとコピーボタンが表示されている(Snippet A)')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('Snippet Aの右のコピーボタンを押下し、テスト用サイトにペースト')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('Snippet Aがペーストできる')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"
    
# [AW22-12] スニペットのウィジェットの実行
# https://jaqool.atlassian.net/browse/GPT-723
# 

# 
@given('テスト用サイトにSnippet Aがペーストされていて、ウィジェットが表示されている')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('ウィジェットを押下し、スタートを押下')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('laMondoを実行できる')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"
    
# [AW22-13] ゲスト画面URLを別タブで開く
# https://jaqool.atlassian.net/browse/GPT-724
# 

# 
@given('バリエーション設定のスニペットの項目にゲスト画面URLと、コピーボタン、別タブで開くボタンが表示されている')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('別タブで開くボタンを押下')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('ゲスト画面が開き、laMondoスタート画面が表示される')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"


# [AW22-14] 二次元バーコードのコピー＆ペースト
# https://jaqool.atlassian.net/browse/GPT-725
# 

# 
@given('バリエーション設定のスニペットの項目に二次元バーコードが表示されている(2D-code A)')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('二次元バーコードをクリックしてリンクをコピーし、別タブを開いてペースト')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('二次元バーコードが表示される')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"
    
# [AW22-15] 二次元バーコードの読み取り
# https://jaqool.atlassian.net/browse/GPT-726
# 

# 
@given('二次元バーコードが表示されている')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('スマートフォンで読み取り実行')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('laMondoのスタート画面が表示される')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"
    
# [AW22-21] バリエーションの編集画面を表示する
# https://jaqool.atlassian.net/browse/GPT-727
# 

# 
@given('バリエーション設定のバリエーション(Vali-A)の右端に鉛筆ボタンが表示されている')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('鉛筆ボタンを押下')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('バリエーションを編集するポップアップが表示され、Vali-Aの情報が表示される')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"
    
# [AW22-22] バリエーションを編集する
# https://jaqool.atlassian.net/browse/GPT-728
# 

# 
@given('バリエーションを編集するポップアップが表示され、Vali-Aの情報が表示されている')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('名前欄、バリエーション欄を編集し、保存を押下')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('バリエーション設定画面に戻り、Vali-Aの名前、バリエーションが変更されている')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"
    
# [AW22-23] バリエーションの削除確認を表示する
# https://jaqool.atlassian.net/browse/GPT-729
# 

# 
@given('バリエーション設定のバリエーション(Vali-A)の右端にゴミ箱ボタンが表示されている　＊デフォルトのバリエーションは削除ボタンが押せなくなっている')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('ゴミ箱ボタンを押下')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('削除確認のポップアップが表示される')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"
    
# [AW22-24] バリエーションの削除の実行
# https://jaqool.atlassian.net/browse/GPT-730
# 

# 
@given('削除確認のポップアップが表示されている')
def chinsara_G(chinsara):
    loginAdmin()

#
@when('削除ボタンを押下')
def chinsara_W(chinsara):
    time.sleep(5)

#
@then('Vali-Aがバリエーション設定画面から非表示になる')
def chinsara_T(chinsara):
    assert 'susara' in "chinsara"
