import webbrowser
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import*
import time
from selenium.webdriver.support.ui import WebDriverWait
import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#管理画面にログインする
driver.get('https://beta-tenant-admin.im.kotozna.chat/ja/login')
time.sleep(10)

element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('kenta+gpt-adminoshima-3096@kotozna.com')
time.sleep(3)

#ログインボタンを押下
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[3]/button').click()
time.sleep(5)

#PINを入力してログイン
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('000000')
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
time.sleep(10)

"""
W01新規ウィジェットを作成する Create a new widget
https://jaqool.atlassian.net/browse/GPT-770
"""

# [AW01-01]ウィジェット設定画面を開く Open the widget setting screen
# https://jaqool.atlassian.net/browse/GPT-328
# 

#Given 基本設定の画面が表示されている The basic setting screen is displayed
#When 左のメニューバーから「ウィジェット設定」をクリックする Click "Widget Settings" from the left menu bar
cur_url = driver.current_url
if 'https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/basicConfiguration' in cur_url:
    #ウィジェット設定へ移動
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()

time.sleep(5)

#Then 現在登録されているウィジェット一覧が表示されるA list of currently registered widgets is displayed.
checkp1 = 0
checkp2 = 0
checkp3 = 0
widget_setting = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]')  # dev要素をCSSセレクタで見つける場合
widget = widget_setting.text
if '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]' == widget:
    #ウィジェット設定へ移動
    checkp1 = 1
#And GPTと連携しているウィジェットのGPTステータスには✓が入っている
element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[7]/td[2]/div/template/div/i')
check = element.get_attribute('class')
#
if 'mdi-check-all mdi v-icon notranslate v-theme--light v-icon--size-default text-green' in check:
    checkp2 = 1
element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[12]/td[2]/div/template/div/i')
#
notcheck = element.get_attribute('class')
if 'mdi-minus mdi v-icon notranslate v-theme--light v-icon--size-default' in notcheck:
    checkp3 = 1
#一覧が表示され、ステータスが変わっているか
if 'mdi-minus mdi v-icon notranslate v-theme--light v-icon--size-default' in notcheck:
    #一覧が表示され、ステータスが変わっているか
    print("AW01-01 OK")

# [AW01-02]ウィジェット設定画面を開く Open the widget setting screen
# https://jaqool.atlassian.net/browse/GPT-329
# 

#Given 現在登録されているウィジェット一覧が表示されているA list of currently registered widgets is displayed.
#When 右上の追加ボタンをクリックするClick the add button in the upper right
#Then 「❶担当グループ」から「❼スニペット」までの登録面に遷移するTransition to the registration side from "❶ charge group" to "❼ snippet"



"""
W02 Create New Widget Step ❶
https://jaqool.atlassian.net/browse/GPT-774
"""
# [AW02-01]ウィジェット名称を設定する Set the widget name
# https://jaqool.atlassian.net/browse/GPT-332
# 
#Given ウィジェット番号がデフォルトで設定されている Widget number is set by default
#When ウィジェット名横のペンシルボタンから名称を変更し、✓ボタンを押す Change the name from the pencil button next to the widget name and press the ✓ button.
#Then ウィジェット番号→指定した名前に変更されるWidget number → changed to the specified name. Name appears in chat header and initial messages.

# [AW02-02]担当グループを割り当てる Assign a responsible group
# https://jaqool.atlassian.net/browse/GPT-333
# 
#Given 担当グループ選択覧が空白である The group selection box is blank
#When 担当グループ選択覧の▼をクリックし、グループ名をクリックする Click ▼ in the group selection box, and click the group name.
#Then 担当グループが設定される The group in charge is set

# [AW02-03]担当グループの割り当てを外す Unassign a responsible group
# https://jaqool.atlassian.net/browse/GPT-334
# 

#Given 担当グループが設定されている The group in charge is set
#When 担当グループ選択覧の✕をクリック Click ✕ in the group selection box
#Then 担当グループ選択覧が空欄になる The group selection box is blank
