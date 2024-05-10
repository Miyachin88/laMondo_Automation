from contextlib import AsyncExitStack
from fileinput import filename
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import*
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Scenario: [A01-01]メールアドレスを入力する Enter your email address on the login screen
# https://jaqool.atlassian.net/browse/GPT-753
@given('Open the admin panel')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('メールアドレスを入力する Input email address')
def chinsara_W(chinsara):
    print(chinsara)

#
@then('PINコード入力画面に遷移し、PINコードが送信される Transit to the PIN code input screen and send the PIN code')
def chinsara_T(chinsara):
    print(chinsara)


# Scenario: [A01-02]PINコードを入力する Enter your PIN code to complete login
# https://jaqool.atlassian.net/browse/GPT-753
@given('PINコード入力画面が表示されているThe PIN code entry screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('PINコードを入力して「ログイン」をクリックEnter your PIN code and click "Login"')
def chinsara_W(chinsara):
    print(chinsara)

#
@then('管理画面にログイン完了する（＝基本設定のページが開く）Login to the management screen is completed (= the basic setting page opens)')
def chinsara_T(chinsara):
    print(chinsara)

    
# Scenario: [A01-03]使い方動画を閲覧する Watching how-to video
# https://jaqool.atlassian.net/browse/GPT-753
@given('管理画面にログインしている / You are logged in to the admin panel')
def chinsara_G(chinsara):
    print(chinsara)

@given('トップバーと基本設定画面が表示されている1 / The top bar and the basic settings are displayed')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('トップバーの[使い方動画を見る]ボタンを押下 / Select the [Using laMondo] button on the top bar')
def chinsara_W(chinsara):
    print(chinsara)

#
@then('ウィジェット1と記載されたウィンドウが開く / A window will open labeled Widget 1')
def chinsara_T(chinsara):
    print(chinsara)

#
@then('使い方動画が再生できる / How-to video can be played')
def chinsara_T(chinsara):
    print(chinsara)
    
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
    print(chinsara)

#
@then('別タブにて、"Kotozna laMondoヘルプセンター"サイトが開く / "Kotozna laMondo Help Center" website will be opend in a new tab')
def chinsara_T(chinsara):
    print(chinsara)

#
@then('管理画面の表示言語が日本語の場合ヘルプセンターは日本語で表示され、管理画面の表示言語が日本語以外の場合ヘルプセンターは英語で表示される / If the admin panel display language is Japanese, the website will be displayed in Japanese, and if the admin panel display language is other than Japanese, the website will be displayed in English.')
def chinsara_T(chinsara):
    print(chinsara)
    
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
    print(chinsara)
@when('任意の言語を選択する Select any language')
def chinsara_W(chinsara):
    print(chinsara)

#
@then('管理画面の表示言語が選択した言語で表示される The display language of admin panel will be displayed in the selected language')
def chinsara_T(chinsara):
    print(chinsara)

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
    print(chinsara)

#
@then('左のメニューバーの設定機能名が非表示になり、アイコン表示のみになる Only icons are displayed, and settings names are hidden')
def chinsara_T(chinsara):
    print(chinsara)


