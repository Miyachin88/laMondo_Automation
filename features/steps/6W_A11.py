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
from func import susa
import sys
from func import widget_06


#ドライバのインストール
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = susa.getDriver()

"""
AW01新規ウィジェットを作成する Create a new widget
https://jaqool.atlassian.net/browse/GPT-770

kenta+b230109-admin@kotozna.com
developer+kenta-lamondo@kotozna.com
"""

widget_06.openW()
print(widget_06.result_a11_01)

# Scenario: [A11-01]ウィジェット設定画面を開く Open the widget setting screen
# https://jaqool.atlassian.net/browse/GPT-328
@given('基本設定の画面が表示されている The basic setting screen is displayed')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('左のメニューバーから「ウィジェット設定」をクリックする Click "Widget Settings" from the left menu bar')
def chinsara_W(chinsara):
    widget_06.test_A11_01g()
    widget_06.test_A11_01w()

#
@then('現在登録されているウィジェット一覧が表示されるA list of currently registered widgets is displayed.')
def chinsara_T(chinsara):
    assert widget_06.result_a11_01 == 'AW01-01 OK'

#
@then('GPTと連携しているウィジェットのGPTステータスには✓が入っている')
def chinsara_T(chinsara):
    print(chinsara)

# Scenario: [A11-02]新規ウィジェット作成画面に進む Go to the new widget creation screen
# https://jaqool.atlassian.net/browse/GPT-329
@given('現在登録されているウィジェット一覧が表示されているA list of currently registered widgets is displayed.')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('右上の追加ボタンをクリックするClick the add button in the upper right')
def chinsara_W(chinsara):
    widget_06.test_A11_02w()

#
@then('「1担当グループ」から「8スニペット」までの登録面に遷移するTransition to the registration side from "1charge group" to "7 snippet"')
def chinsara_T(chinsara):
    assert widget_06.result_a11_02 == 'AW01-02 OK'