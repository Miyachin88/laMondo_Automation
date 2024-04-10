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
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = susa.getDriver()

"""
AW02 Create New Widget Step ❶
https://jaqool.atlassian.net/browse/GPT-774

kenta+b230109-admin@kotozna.com
developer+kenta-lamondo@kotozna.com
"""

# Scenario: [AW02-01]ウィジェット名称を設定する Set the widget name
# https://jaqool.atlassian.net/browse/GPT-332
@given('ウィジェット番号がデフォルトで設定されている Widget number is set by default')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('ウィジェット名横のペンシルボタンから名称を変更し、✓ボタンを押す Change the name from the pencil button next to the widget name and press the ✓ button.')
def chinsara_W(chinsara):
    time.sleep(3)

#
@then('ウィジェット番号→指定した名前に変更されるWidget number → changed to the specified name. Name appears in chat header and initial messages.')
def chinsara_T(chinsara):
    print(chinsara)


# Scenario: [AW02-02]担当グループを割り当てる Assign a responsible group
# https://jaqool.atlassian.net/browse/GPT-333
@given('担当グループ選択覧が空白である The group selection box is blank')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('担当グループ選択覧の▼をクリックし、グループ名をクリックする Click ▼ in the group selection box, and click the group name.')
def chinsara_W(chinsara):
    time.sleep(3)

#
@then('担当グループが設定される The group in charge is set')
def chinsara_T(chinsara):
    print(chinsara)
    

# Scenario: [AW02-03]担当グループの割り当てを外す Unassign a responsible group
# https://jaqool.atlassian.net/browse/GPT-334
@given('"担当グループが設定されている The group in charge is set')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('"担当グループ選択覧の✕をクリック Click ✕ in the group selection box')
def chinsara_W(chinsara):
    time.sleep(3)

#
@then('"担当グループ選択覧が空欄になる The group selection box is blank')
def chinsara_T(chinsara):
    print(chinsara)