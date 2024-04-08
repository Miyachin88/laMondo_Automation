from fileinput import filename
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import*
from bs4 import BeautifulSoup
from func import susa
import requests
import time

#ドライバのインストール
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#susa.chinchin()
driver = susa.getDriver()

"""
A01日本人が管理画面にログインする Japanese administrator tries to log in to the Admin Panel
https://jaqool.atlassian.net/browse/GPT-753

kenta+b230109-admin@kotozna.com
developer+kenta-lamondo@kotozna.com
"""


# [A01-01]メールアドレスを入力する Enter your email address on the login screen
# https://jaqool.atlassian.net/browse/GPT-754
@given('Open the lamondo admin panel')
def chinsara_G(chinsara):
    #driver.get('https://beta-tenant-admin.im.kotozna.chat/ja/login')
    susa.login(driver, 'https://beta-tenant-admin.im.kotozna.chat/ja/login')
    time.sleep(10)

@when('メールアドレスを入力する Input email address')
def chinsara_W(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('kenta+b230109-admin@kotozna.com')
    time.sleep(3)


@then('PINコード入力画面に遷移し、PINコードが送信される Transit to the PIN code input screen and send the PIN code')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input')
    chinsara = element.get_attribute('value')
    assert ('kenta+b230109-admin@kotozna.com' == chinsara) is True
    
# [A01-02]PINコードを入力する Enter your PIN code to complete login
# https://jaqool.atlassian.net/browse/GPT-755
#
@given('PINコード入力画面が表示されているThe PIN code entry screen is displayed')
def chinsara_G(chinsara):
    #ログインボタンを押下
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[3]/button').click()
    time.sleep(5)

#
@when('PINコードを入力して「ログイン」をクリックEnter your PIN code and click "Login"')
def chinsara_W(chinsara):
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('000000')
    time.sleep(10)

#
@then('管理画面にログイン完了する（＝基本設定のページが開く）Login to the management screen is completed (= the basic setting page opens)')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input')
    chinsara = element.get_attribute('value')   
    cur_url = driver.current_url
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    assert ('https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/basicConfiguration' == cur_url) is True

# [A01-03]使い方動画を閲覧する Watching how-to video
# https://jaqool.atlassian.net/browse/GPT-756
# 
@given('管理画面にログインしている1 / You are logged in to the admin panel')
def chinsara_G(chinsara):
    # dev要素を見つけて、そのテキストを取得する
    time.sleep(30)    
    cur_url = driver.current_url
    if 'https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/basicConfiguration' in cur_url:
        # 特定の文字列が含まれている場合の処理
        print("OK")
    else:
    # 特定の文字列が含まれていない場合の処理
        print("NG")
# 
@given('トップバーと基本設定画面が表示されている1 / The top bar and the basic settings are displayed')
def chinsara_G(chinsara):
    # dev要素を見つけて、そのテキストを取得する
    dev_element = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[2]')  # dev要素をCSSセレクタで見つける場合
    dev_text = dev_element.text
    if "基本設定" in dev_text:
        # 特定の文字列が含まれている場合の処理
        print("OK")
    else:
    # 特定の文字列が含まれていない場合の処理
        print("NG")

#
@when('トップバーの[使い方動画を見る]ボタンを押下 / Select the [Using laMondo] button on the top bar')
def chinsara_W(chinsara):
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[1]/button').click()
    time.sleep(10)

#
@then('ウィジェット1と記載されたウィンドウが開く / A window will open labeled Widget 1')
def chinsara_T(chinsara):
    driver.current_window_handle
    widget_title = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[1]').text
    assert ('あごぽよクリーニング香椎本店' == widget_title) is True
    
#
@then('使い方動画が再生できる / How-to video can be played')
def chinsara_T(chinsara):
    time.sleep(30)
    iframe = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[3]/div[1]/iframe')
    movsrc = iframe.get_attribute('src')
    assert ('https://www.youtube.com/embed/e23dN762YTg' == movsrc) is True
    
    
# [A01-04]ヘルプセンターにアクセスする Open the help center link
# https://jaqool.atlassian.net/browse/GPT-757
#
@given('管理画面にログインしている2 / You are logged in to the admin panel')
def chinsara_G(chinsara):
    #あごぽよクリーニングのウインドウを❌で閉じる
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/button').click()
    time.sleep(3)
#
@given('トップバーと基本設定画面が表示されている2 / The top bar and the basic settings are displayed')
def chinsara_G(chinsara):
    #ウインドウを現在の画面に戻す
    driver.current_window_handle
    
#
@when('？アイコンを押下 / Select "?" button')
def chinsara_W(chinsara):
    time.sleep(3)
    #?アイコンを押下
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/i').click()
    time.sleep(5)
    #別タブへ移動  
    driver.switch_to.window(driver.window_handles[1])    
    
#
@then('別タブにて、"Kotozna laMondoヘルプセンター"サイトが開く / "Kotozna laMondo Help Center" website will be opend in a new tab')
def chinsara_T(chinsara):
    cur_url = driver.current_url
    assert ('https://lamondo.manual.kotozna.com/ja/home' == cur_url) is True

#
@then('管理画面の表示言語が日本語の場合ヘルプセンターは日本語で表示され、管理画面の表示言語が日本語以外の場合ヘルプセンターは英語で表示される / If the admin panel display language is Japanese, the website will be displayed in Japanese, and if the admin panel display language is other than Japanese, the website will be displayed in English.')
def chinsara_T(chinsara):
    time.sleep(3)

    
# [A01-05]表示言語を変更する Changing display language
# https://jaqool.atlassian.net/browse/GPT-758
#
@given('管理画面にログインしている3 You are logged in to the admin panel')
def chinsara_G(chinsara):
    # ハンドルを戻す
    driver.switch_to.window(driver.window_handles[0])
#
@given('トップバーと基本設定画面が表示されている3 The top bar and the basic settings are displayed')
def chinsara_G(chinsara):
    time.sleep(5)   

#
@when('地球儀アイコンを押下し任意の言語を選択 Select the globe icon')
def chinsara_W(chinsara):
    #言語を切り替えボタンを押下
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[3]/div/div/button').click()
    time.sleep(5)
    #英語を選択
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/div/div/div').click()
    time.sleep(5)    

#
@then('管理画面の表示言語が選択した言語で表示される The display language of admin panel will be displayed in the selected language')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/span').text
    assert ('Basic Settings' == element) is True    
    
#
@then('ただし、ワークコード名、ウィジェット名、グループ名、ユーザー名（アカウント名）は変わらない Work code names, widget names, group names, and user names wont be changed')
def chinsara_T(chinsara):
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[1]/td[1]/span').text
    assert ('あごぽよクリーニング香椎本店' == element) is True    