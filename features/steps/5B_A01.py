from contextlib import AsyncExitStack
from fileinput import filename
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import*
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
import time



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Scenario: [A01-01]メールアドレスを入力する Enter your email address on the login screen
# https://jaqool.atlassian.net/browse/GPT-753
@Given('laMondo管理画面を開く Open the lamondo admin panel')
def a01_01_g(aaa):
    pass

#
@When('メールアドレスを入力する Input email address')
def a01_01_w(aaa):
    driver.get('https://beta-tenant-admin.im.kotozna.chat/ja/login')
    time.sleep(10)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('kenta+b230109-admin@kotozna.com')
    time.sleep(3)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input')
    chinsara = element.get_attribute('value')
    if chinsara == "kenta+b230109-admin@kotozna.com":
        #テキストの判別
        print("AB01-01 OK")
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
        time.sleep(5)


#
@Then('PINコード入力画面に遷移し、PINコードが送信される Transit to the PIN code input screen and send the PIN code')
def a01_01_t(self):
    cur_url = driver.current_url
    assert cur_url == "https://beta-tenant-admin.im.kotozna.chat/ja/login"


# Scenario: [A01-02]PINコードを入力する Enter your PIN code to complete login
# https://jaqool.atlassian.net/browse/GPT-753
@given('PINコード入力画面が表示されているThe PIN code entry screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('PINコードを入力して「ログイン」をクリックEnter your PIN code and click "Login"')
def chinsara_W(chinsara):
    #PINを入力
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('000000')
    time.sleep(10)

    #PINをクリック
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input')
    chinsara = element.get_attribute('value')   
    cur_url = driver.current_url
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()

    # dev要素を見つけて、そのテキストを取得する
    time.sleep(10)

#
@then('管理画面にログイン完了する（＝基本設定のページが開く）Login to the management screen is completed (= the basic setting page opens)')
def chinsara_T(chinsara):
    cur_url = driver.current_url
    dev_element = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[2]')  # dev要素をCSSセレクタで見つける場合
    dev_text = dev_element.text
    assert ('https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/basicConfiguration' in cur_url) & ("基本設定" in dev_text)

    
# Scenario: [A01-03]使い方動画を閲覧する Watching how-to video
# https://jaqool.atlassian.net/browse/GPT-753
@given('laMondo管理画面にログインしている / You are logged in to the admin panel')
def chinsara_G(chinsara):
    time.sleep(3)

@given('トップバーと基本設定画面が表示されている1 / The top bar and the basic settings are displayed')
def chinsara_G(chinsara):   
    print("chinsara")

#
@when('トップバーの[使い方動画を見る]ボタンを押下 / Select the [Using laMondo] button on the top bar')
def chinsara_W(chinsara):
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[1]/button').click()
    time.sleep(10)
    driver.current_window_handle
#
@then('ウィジェット1と記載されたウィンドウが開く / A window will open labeled Widget 1')
def chinsara_T(chinsara):
    widget_title = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[1]').text
    #
    assert 'あごぽよクリーニング香椎本店' == widget_title

#
@then('使い方動画が再生できる / How-to video can be played')
def chinsara_T(chinsara):
    #
    iframe = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div[3]/div[1]/iframe')))
    movsrc = iframe.get_attribute('src')
    assert 'https://www.youtube.com/embed/e23dN762YTg' == movsrc
    
# Scenario: [A01-04]ヘルプセンターにアクセスする Open the help center link
# https://jaqool.atlassian.net/browse/GPT-753
@given('管理画面にログインしている2 / You are logged in to the admin panel')
def chinsara_G(chinsara):
    print(chinsara)

@given('トップバーと基本設定画面が表示されている2 / The top bar and the basic settings are displayed')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('？アイコンを押下 / Select "?" button')
def chinsara_W(chinsara):
    #あごぽよクリーニングのウインドウを❌で閉じる
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/button').click()
    time.sleep(3)
    #

    #ウインドウを現在の画面に戻す
    driver.current_window_handle

    #
    time.sleep(3)
    #?アイコンを押下
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/i').click()

#
@then('別タブにて、"Kotozna laMondoヘルプセンター"サイトが開く / "Kotozna laMondo Help Center" website will be opend in a new tab')
def chinsara_T(chinsara):
    #別タブへ移動  
    driver.switch_to.window(driver.window_handles[1])
    cur_url = driver.current_url
    assert 'https://lamondo.manual.kotozna.com/ja/home' == cur_url

#
@then('管理画面の表示言語が日本語の場合ヘルプセンターは日本語で表示され、管理画面の表示言語が日本語以外の場合ヘルプセンターは英語で表示される / If the admin panel display language is Japanese, the website will be displayed in Japanese, and if the admin panel display language is other than Japanese, the website will be displayed in English.')
def chinsara_T(chinsara):
    judge_jpn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/div/div/ul/div/li[1]/div/a/span/span').text
    assert 'ホーム' == judge_jpn
    # 現在のタブを閉じる
    driver.close()
    
# Scenario: [A01-05]表示言語を変更する Changing display language
# https://jaqool.atlassian.net/browse/GPT-753
@given('管理画面にログインしている3 You are logged in to the admin panel')
def chinsara_G(chinsara):
    print(chinsara)
@given('トップバーと基本設定画面が表示されている3 The top bar and the basic settings are displayed')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('地球儀アイコンを押下 Select the globe icon')
def chinsara_W(chinsara):
    driver.switch_to.window(driver.window_handles[0]) 
    time.sleep(5)

    #言語を切り替えボタンを押下
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[3]/div/div/button').click()
    time.sleep(5)
@when('任意の言語を選択する Select any language')
def chinsara_W(chinsara):
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/div/div/div').click()
    time.sleep(5)

#
@then('管理画面の表示言語が選択した言語で表示される The display language of admin panel will be displayed in the selected language')
def chinsara_T(chinsara):
    judge_eng = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/span').text
    #ウィジェット設定へ移動
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()
    time.sleep(5)
    judge_jpn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[1]/td[1]/span').text
    assert ('Basic Settings' == judge_eng) & ('あごぽよクリーニング香椎本店' == judge_jpn)
    time.sleep(3)

#
@then('ただし、ワークコード名、ウィジェット名、グループ名、ユーザー名（アカウント名）は変わらない Work code names, widget names, group names, and user names wont be changed')
def chinsara_T(chinsara):
    print(chinsara)
    
# Scenario: [AB01-06]ハンバーガーボタンで表示方法を変更 Changing display with Hamburger button
# https://jaqool.atlassian.net/browse/GPT-753
@given('基本設定の画面が表示されている1 The basic setting screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)

@given('左のメニューバーに「ウィジェット設定」など、設定機能名とアイコンが表示されている Settings names such as "Widget settings" and icons are listed on the left')
def chinsara_W(chinsara):
    print(chinsara)

#
@when('左上のハンバーガーボタンをクリックする Click the Hamburger button on the upper left')
def chinsara_T(chinsara):
    #ハンバーガーボタンをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[1]').click()
    time.sleep(3)

#
@then('左のメニューバーの設定機能名が非表示になり、アイコン表示のみになる Only icons are displayed, and settings names are hidden')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]')
    width = element.get_attribute('style')
    assert width[7:9] == '60'
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[1]').click()


