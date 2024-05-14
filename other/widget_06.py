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
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import calendar
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

#ドライバー
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#その他
# 現在の日時を取得
now = datetime.now()
# 曜日を取得
weekday = calendar.day_name[now.weekday()]
# 日付のフォーマットを指定
#date_format = now.strftime("%Y/%m/%d %a %H:%M")
#現在時刻
date_format = now.strftime("%H:%M")
#今日の日付
monthday_format = now.strftime("%m%d")
# 出力する日付を表示
#print(date_format)
#print(monthday_format)

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

#管理画面にログインする
def login_admin():
    driver.get('https://beta-tenant-admin.im.kotozna.chat/ja/login')
    time.sleep(10)

    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('kenta+gpt-adminoshima-3096@kotozna.com')
    time.sleep(3)

    #ログインボタンを押下
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[3]/button').click()
    time.sleep(5)

    #PINを入力してログイン
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('000000')
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    time.sleep(10)

login_admin()

"""
W01新規ウィジェットを作成する Create a new widget
https://jaqool.atlassian.net/browse/GPT-770
"""

# [AW01-01]ウィジェット設定画面を開く Open the widget setting screen
# https://jaqool.atlassian.net/browse/GPT-328
# 

#Given 基本設定の画面が表示されている The basic setting screen is displayed
#When 左のメニューバーから「ウィジェット設定」をクリックする Click "Widget Settings" from the left menu bar
def test_A11_01g():
    cur_url = driver.current_url
    if 'https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/basicConfiguration' in cur_url:
        #ウィジェット設定へ移動
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()

    time.sleep(5)

test_A11_01g()

#Then 現在登録されているウィジェット一覧が表示されるA list of currently registered widgets is displayed.
result_a11_01 = "" 
def test_A11_01w():
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
        result_a11_01 = "AW01-01 OK" 

test_A11_01w()

# [AW01-02]ウィジェット設定画面を開く Open the widget setting screen
# https://jaqool.atlassian.net/browse/GPT-329
# 

#Given 現在登録されているウィジェット一覧が表示されているA list of currently registered widgets is displayed.
#When 右上の追加ボタンをクリックするClick the add button in the upper right
#driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').click()
#time.sleep(5)
#Then 「❶担当グループ」から「❼スニペット」までの登録面に遷移するTransition to the registration side from "❶ charge group" to "❼ snippet"
#現在のURLが”newWidgetSetting”であることを確認
result_a11_02 = "" 
def test_A11_02w():
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').click()
    time.sleep(5)
    cur_url = driver.current_url
    if 'https://beta-tenant-admin.im.kotozna.chat/ja/laMondo/newWidgetSetting' in cur_url:
        #ウィジェット設定へ移動
        print("AW01-02 OK")
        result_a11_01 = "AW01-02 OK" 
    else :
        print("AW01-02 NG")

test_A11_02w()

"""
W02 Create New Widget Step ❶
https://jaqool.atlassian.net/browse/GPT-774
"""
# [AW02-01]ウィジェット名称を設定する Set the widget name
# https://jaqool.atlassian.net/browse/GPT-332
# 
def test_AW02_01():
    #Given ウィジェット番号がデフォルトで設定されている Widget number is set by default
    #When ウィジェット名横のペンシルボタンから名称を変更し、✓ボタンを押す Change the name from the pencil button next to the widget name and press the ✓ button.
    #ワークコードテストの名称を編集
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div').click()
    #Then ウィジェット番号→指定した名前に変更されるWidget number → changed to the specified name. Name appears in chat header and initial messages.
    wait = WebDriverWait(driver, 300)
    wkcdname = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div[1]/form/div/div[1]/div/div[3]/input')))
    wkcdname.send_keys(Keys.COMMAND + "a" )
    wkcdname.send_keys( Keys.DELETE )
    wkcdname.send_keys('AW02-01 test')
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div[2]').click()
    widget_setting = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/h1')
    aw2_1 = widget_setting.text
    if 'AW02-01 test' == aw2_1:
        #テキストの判別
        print("AW02-01 OK")
        
test_AW02_01()

# [AW02-02]担当グループを割り当てる Assign a responsible group
# https://jaqool.atlassian.net/browse/GPT-333
# 
def test_AW02_02():
    #Given 担当グループ選択覧が空白である The group selection box is blank
    #When 担当グループ選択覧の▼をクリックし、グループ名をクリックする Click ▼ in the group selection box, and click the group name.
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[3]').click()
    time.sleep(5)
    #Then 担当グループが設定される The group in charge is set
    widget_setting = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[3]/div/div/span')
    aw2_2 = widget_setting.text
    if 'ごみ' == aw2_2:
        #テキストの判別
        print("AW02-02 OK")
    else :
        print(aw2_2)

test_AW02_02()


# [AW02-03]担当グループの割り当てを外す Unassign a responsible group
# https://jaqool.atlassian.net/browse/GPT-334
# 
def test_AW02_03():
    #Given 担当グループが設定されている The group in charge is set
    #When 担当グループ選択覧の✕をクリック Click ✕ in the group selection box
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[4]/i').click()
    time.sleep(3)
    #Then 担当グループ選択覧が空欄になる The group selection box is blank
    widget_setting = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[3]/div/div/span')
    aw2_3 = widget_setting.text
    if '' == aw2_3:
        #テキストの判別
        print("AW02-03 OK")

test_AW02_03()


"""
W02Create New Widget Step ❷
https://jaqool.atlassian.net/browse/GPT-775
"""
#いったん一覧に戻る
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/button').click()
time.sleep(10)

# [AW03-01]チャットの営業可能時間を設定する（毎日） Set chat business hours (Daily)
# https://jaqool.atlassian.net/browse/GPT-776
# 
def test_AW03_01():
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)

    ##営業時間の設定
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

    #受付時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-01 title')
    time.sleep(3)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #プルダウンを表示
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)
    #毎日を選択
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(5)

    ####時刻を入力

    #時刻を変換
    #時間を設定
    settingh = str(date_format[:2])
    sethour = int(settingh)
    #分を設定
    settingm = str(date_format[-2:])
    setminute = int(settingm)

    #時間を設定
    #ケース1 : 23時台の時
    if (settingh == 23):
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(settingh - 1):
            businessh_1st.click()
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59):
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input')
        #保存して閉じますをクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10)  

    #ケース2 : 0-22時台の時
    else:
        #時計を操作(開始時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(sethour + 1):
            businessh_1st.click()
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(setminute + (60 - setminute)):
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input')
        #保存して閉じますをクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10)   

    #ウィジェット設定に戻り自動化用のウィジェットを開く
        openW()
        time.sleep(15)
        driver.switch_to.window
        wait = WebDriverWait(driver, 180)
        notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
        if notaccept.text[:13] == '受付時間は下記の通りです。':
            print("AW03-01 OK")
            
    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)

#test_AW03_01()
#AW03-01の終わり

# [AW03-02]チャットの営業可能時間を設定する（曜日） Set chat business hours (day of the week)
# https://jaqool.atlassian.net/browse/GPT-777
# 
def test_AW03_02():
    #ウィジェットを閉じる必要あり
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

    #受付時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-02 title')
    time.sleep(10)
    #対象をクリック 曜日を指定
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)
    #曜日を指定をクリック
    wait = WebDriverWait(driver, 300)
    businessdtw = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div')))    
    businessdtw.click()
    time.sleep(5)
    #曜日をクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div')))
    add_businessh.click()
    time.sleep(10)
    ##休日なら月曜日をクリックして、平日なら土曜日をクリックするプログラム
    #休日の場合
    if weekday == "Saturday" or weekday == "Sunday":
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[1]/div/div/div/input').click()
        time.sleep(5)
        #保存して閉じますをクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10) 
    #平日の場合
    else:
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[6]/div[1]/div/div/div/input').click()
        time.sleep(5)
        #保存して閉じますをクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10) 

    #ウィジェット設定に戻り自動化用のウィジェットを開く
        openW()
        time.sleep(15)
        driver.switch_to.window
        wait = WebDriverWait(driver, 180)
        notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
        if notaccept.text[:13] == '受付時間は下記の通りです。':
            print("AW03-02 OK")

    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)

#test_AW03_02()

# [AW03-03]チャットの営業可能時間を設定する（特定の日のみ）Set chat business hours (only on specific days)
# https://jaqool.atlassian.net/browse/GPT-778
# 

def test_AW03_03():
    #ウィジェットを閉じる必要あり
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

    #受付時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-03 title')
    time.sleep(10)
    #対象をクリック 曜日を指定
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)
    #日を指定をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div[2]/div').click()
    time.sleep(5)
    #日をクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div[2]/div[2]/div/div/div/input')))
    add_businessh.click()
    time.sleep(10)

    for i in range(6):  # 配列の長さまたは6の少ない方をループ回数とする
        #週を探索および設置
        flag = False 
        hello1 = str(i + 1)
        setsearchweek = "/div[" + str(hello1) + "]"
        for j in range(7):  # i+1回数の少ない方をループ回数とする
            #曜日を探索および設置
            hello2 = str(j + 1)
            setsearchdayoftheweek = "/div[" + hello2 + "]"        
            setpath = "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]" + setsearchweek + setsearchdayoftheweek
            dateset = driver.find_element(By.XPATH,setpath)
            widget = dateset.text
            #文字の色を取得
            setpathcolor = "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]" + setsearchweek + setsearchdayoftheweek + "/div"        
            widgetcolor = driver.find_element(By.XPATH,setpathcolor)
            color = widgetcolor.value_of_css_property('color')
            #日付が1-9日の時とそうでない時の条件分岐
            if widget in ['1','2','3','4','5','6','7','8','9'] :
                #日付が合致していたらクリックする
                if (widget == monthday_format[-1:]) & (color == 'rgba(33, 33, 33, 1)'):
                    dateset.click()
                    #選択ボタンをクリック
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    time.sleep(3)
                    #時計を操作(終了時間のみ)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
                    time.sleep(5)
                    wait = WebDriverWait(driver, 300)
                    businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
                    for _ in range(23): #23時に設定
                        businessh_1st.click() #受付時間の時間を入力
                    #分を設定
                    wait = WebDriverWait(driver, 300)
                    businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
                    #時刻を設定
                    for _ in range(59): #59分に設定
                        businessm_1st.click()
                    #選択をクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()            
                    #保存して閉じますをクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
                    time.sleep(10)
                    flag = True  # フラグをTrueに設定
                    break;
            #10日から31日の時
            else :
                #日付が合致しているかつ文字が黒の時はクリックする
                if (widget == monthday_format[-2:]) & (color == 'rgba(33, 33, 33, 1)'): 
                    dateset.click()
                    #選択ボタンをクリック
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    time.sleep(3)
                    #時計を操作(終了時間のみ)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
                    time.sleep(5)
                    wait = WebDriverWait(driver, 300)
                    businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
                    for _ in range(23): #23時に設定
                        businessh_1st.click() #受付時間の時間を入力
                    #分を設定
                    wait = WebDriverWait(driver, 300)
                    businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
                    #時刻を設定
                    for _ in range(59): #59分に設定
                        businessm_1st.click()            
                    #保存して閉じますをクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
                    time.sleep(10)
                    flag = True  # フラグをTrueに設定    
        if flag:  # フラグがTrueの場合、外側のループを抜ける
            break


    #ウィジェット設定に戻り自動化用のウィジェットを開く
    time.sleep(10)
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__title.pa-4')))
    if notaccept.text[:13] == '利用規約':
        print("AW03-03 OK")

    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)

    #16日
    #/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]/div[3]/div[2]
    #22日
    #/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]/div[4]/div[1]
    #23日
    #/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]/div[4]/div[2]

#test_AW03_03()
#AW03-03の終わり

# [AW03-04]チャットの対応不可時間を設定する（毎日）Set chat unavailable hours (Daily)
# https://jaqool.atlassian.net/browse/GPT-779
# 
def test_AW03_04():
    #ウィジェットを閉じる必要あり
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

    #受付不可時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-04 title')
    time.sleep(3)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #プルダウンを表示
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)
    #毎日を選択
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(5)

    ####時刻を入力

    #時刻を変換
    #時間を設定
    settingh = str(date_format[:2])
    sethour = int(settingh)
    #分を設定
    settingm = str(date_format[-2:])
    setminute = int(settingm)

    #時間を設定
    #ケース1 : 23時台の時
    if (settingh == 23):
        #時計を操作(開始時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(sethour - 1): #22時に設定
            businessh_1st.click()
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(setminute + (60 - setminute)): #59分に設定
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input')
        #保存して閉じますをクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10) 

    #ケース2 : 0-22時台の時
    else:
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(sethour + 1): #23時に設定
            businessh_1st.click() #受付時間の時間を入力
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59): #59分に設定
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input')
        #保存して閉じますをクリックdiv/div/div[2]').click()
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10)  

    #ウィジェット設定に戻り自動化用のウィジェットを開く
        openW()
        time.sleep(15)
        driver.switch_to.window
        wait = WebDriverWait(driver, 180)
        notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
        if notaccept.text[:23] == '以下は受付時間外となりますのでご了承ください。':
            print("AW03-04 OK")
            
    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)
#test_AW03_04()
#AW03-04の終わり

# [AW03-05]チャットの対応不可時間を設定する（曜日）Set chat unavailable hours (day of the week)
# https://jaqool.atlassian.net/browse/GPT-780
# 
def test_AW03_05():
    #ウィジェットを閉じる必要あり
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

    #受付不可時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-05 title')
    time.sleep(10)
    #対象をクリック 曜日を指定
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)
    #曜日を指定をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div').click()
    time.sleep(5)
    #曜日をクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div')))
    add_businessh.click()
    time.sleep(10)
    ##休日なら土日をクリックして、平日なら月ー金曜日をクリックするプログラム
    #休日の場合
    if weekday == "Saturday" or weekday == "Sunday":
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[6]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[7]/div[1]/div/div/div/input').click()
        time.sleep(5)
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(23): #23時に設定
            businessh_1st.click() #受付時間の時間を入力
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59): #59分に設定
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        #保存して閉じますをクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10) 
    #平日の場合
    else:
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[4]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[5]/div[1]/div/div/div/input').click()
        time.sleep(5)
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(23): #23時に設定
            businessh_1st.click() #受付時間の時間を入力
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59): #59分に設定
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        #保存して閉じますをクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10) 


    #ウィジェット設定に戻り自動化用のウィジェットを開く
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
    if notaccept.text[:23] == '以下は受付時間外となりますのでご了承ください。':
        print("AW03-05 OK")

    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)
    
#test_AW03_05()
#AW03-05の終わり



# [AW03-06]チャットの対応不可時間を設定する（特定の日のみ）Set chat unavailable hours (only on specific days)
# https://jaqool.atlassian.net/browse/GPT-781
# 
def test_AW03_06():

    #ウィジェットを閉じる必要あり
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

    #受付不可時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-06 title')
    time.sleep(10)
    #対象をクリック 日を指定
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)
    #日を指定をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div[2]/div').click()
    time.sleep(5)
    #日をクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div[2]/div[2]/div/div/div/input')))
    add_businessh.click()
    time.sleep(10)

    for i in range(6):  # 配列の長さまたは6の少ない方をループ回数とする
        #週を探索および設置
        flag = False 
        hello1 = str(i + 1)
        setsearchweek = "/div[" + str(hello1) + "]"
        for j in range(7):  # i+1回数の少ない方をループ回数とする
            #曜日を探索および設置
            hello2 = str(j + 1)
            setsearchdayoftheweek = "/div[" + hello2 + "]"        
            setpath = "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]" + setsearchweek + setsearchdayoftheweek
            dateset = driver.find_element(By.XPATH,setpath)
            widget = dateset.text
            #文字の色を取得
            setpathcolor = "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]" + setsearchweek + setsearchdayoftheweek + "/div"        
            widgetcolor = driver.find_element(By.XPATH,setpathcolor)
            color = widgetcolor.value_of_css_property('color')
            #日付が1-9日の時とそうでない時の条件分岐
            if widget in ['1','2','3','4','5','6','7','8','9'] :
                #日付が合致していたらクリックする
                if (widget == monthday_format[-1:]) & (color == 'rgba(33, 33, 33, 1)'):
                    dateset.click()
                    #選択ボタンをクリック
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    time.sleep(3)
                    #時計を操作(終了時間のみ)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
                    time.sleep(5)
                    wait = WebDriverWait(driver, 300)
                    businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
                    for _ in range(23): #23時に設定
                        businessh_1st.click() #受付時間の時間を入力
                    #分を設定
                    wait = WebDriverWait(driver, 300)
                    businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
                    #時刻を設定
                    for _ in range(59): #59分に設定
                        businessm_1st.click()
                    #選択をクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()               
                    #保存して閉じますをクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
                    time.sleep(10)
                    flag = True  # フラグをTrueに設定
                    break;                   
            #10日から31日の時
            else :
                #日付が合致しているかつ文字が黒の時はクリックする
                if (widget == monthday_format[-2:]) & (color == 'rgba(33, 33, 33, 1)'): 
                    dateset.click()
                    #選択ボタンをクリック
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    time.sleep(3)
                    #時計を操作(終了時間のみ)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
                    time.sleep(5)
                    wait = WebDriverWait(driver, 300)
                    businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
                    for _ in range(23): #23時に設定
                        businessh_1st.click() #受付時間の時間を入力
                    #分を設定
                    wait = WebDriverWait(driver, 300)
                    businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
                    #時刻を設定
                    for _ in range(59): #59分に設定
                        businessm_1st.click()            
                    #保存して閉じますをクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
                    time.sleep(10)
                    flag = True  # フラグをTrueに設定
                #else :
        if flag:  # フラグがTrueの場合、外側のループを抜ける
            break

    #ウィジェット設定に戻り自動化用のウィジェットを開く
    time.sleep(10)
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
    if notaccept.text[:23] == '以下は受付時間外となりますのでご了承ください。':
        print("AW03-06 OK")

    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)

#test_AW03_06()
#AW03-06の終わり

# [AW03-07]営業不可時間を複数設定する Set multiple Out of Business Hours
# https://jaqool.atlassian.net/browse/GPT-782
# 
def test_AW03_07():
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)

    ##営業時間の設定
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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
    
    # 曜日を設定
    # 
    #受付不可時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-07 title1')
    time.sleep(10)
    
    #対象をクリック 曜日を指定
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)
    #曜日を指定をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div').click()
    time.sleep(5)
    #曜日をクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div')))
    add_businessh.click()
    time.sleep(10)
    ##休日なら土日をクリックして、平日なら月ー金曜日をクリックするプログラム
    #休日の場合
    if weekday == "Saturday" or weekday == "Sunday":
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[6]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[7]/div[1]/div/div/div/input').click()
        time.sleep(5)
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(23): #23時に設定
            businessh_1st.click() #受付時間の時間を入力
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59): #59分に設定
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        #保存して閉じますをクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10) 
    #平日の場合
    else:
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[4]/div[1]/div/div/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[5]/div[1]/div/div/div/input').click()
        time.sleep(5)
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(23): #23時に設定
            businessh_1st.click() #受付時間の時間を入力
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59): #59分に設定
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()

    #受付不可時間の2個目をクリック
    wait = WebDriverWait(driver, 300)
    add_dotw = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_dotw.click()
    # 
    #日時を設定       
    time.sleep(10) 
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-07 title2')
    time.sleep(10)
    
    #対象をクリック 日を指定
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/div/div[4]/div/div[2]/div[1]/div/div[4]').click()
    time.sleep(5)    
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/div/div[4]/div/div[2]/div[1]/div/div[5]').click()
    time.sleep(5)
    #日を指定(優先度高)をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div[2]/div').click()
    time.sleep(5)    
    #日をクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/div/div[4]/div[2]/div[2]/div/div/div/input')))
    add_businessh.click()
    time.sleep(10)

    for i in range(6):  # 配列の長さまたは6の少ない方をループ回数とする
        #週を探索および設置
        flag = False 
        hello1 = str(i + 1)
        setsearchweek = "/div[" + str(hello1) + "]"
        for j in range(7):  # i+1回数の少ない方をループ回数とする
            #曜日を探索および設置
            hello2 = str(j + 1)
            setsearchdayoftheweek = "/div[" + hello2 + "]"        
            setpath = "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]" + setsearchweek + setsearchdayoftheweek
            dateset = driver.find_element(By.XPATH,setpath)
            widget = dateset.text
            #文字の色を取得
            setpathcolor = "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div[3]" + setsearchweek + setsearchdayoftheweek + "/div"        
            widgetcolor = driver.find_element(By.XPATH,setpathcolor)
            color = widgetcolor.value_of_css_property('color')
            #日付が1-9日の時とそうでない時の条件分岐
            if widget in ['1','2','3','4','5','6','7','8','9'] :
                #日付が合致していたらクリックする
                if (widget == monthday_format[-1:]) & (color == 'rgba(33, 33, 33, 1)'):
                    dateset.click()
                    #選択ボタンをクリック
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    time.sleep(3)
                    #時計を操作(終了時間のみ)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
                    time.sleep(5)
                    wait = WebDriverWait(driver, 300)
                    businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
                    for _ in range(23): #23時に設定
                        businessh_1st.click() #受付時間の時間を入力
                    #分を設定
                    wait = WebDriverWait(driver, 300)
                    businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
                    #時刻を設定
                    for _ in range(59): #59分に設定
                        businessm_1st.click()
                    #選択をクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()               
                    #保存して閉じますをクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
                    time.sleep(10)
                    flag = True  # フラグをTrueに設定
                    break;                   
            #10日から31日の時
            else :
                #日付が合致しているかつ文字が黒の時はクリックする
                if (widget == monthday_format[-2:]) & (color == 'rgba(33, 33, 33, 1)'): 
                    dateset.click()
                    #選択ボタンをクリック
                    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
                    time.sleep(3)
                    #時計を操作(終了時間のみ)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
                    time.sleep(5)
                    wait = WebDriverWait(driver, 300)
                    businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
                    for _ in range(23): #23時に設定
                        businessh_1st.click() #受付時間の時間を入力
                    #分を設定
                    wait = WebDriverWait(driver, 300)
                    businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
                    #時刻を設定
                    for _ in range(59): #59分に設定
                        businessm_1st.click()            
                    #保存して閉じますをクリック
                    time.sleep(5)
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
                    time.sleep(10)
                    flag = True  # フラグをTrueに設定
                #else :
        if flag:  # フラグがTrueの場合、外側のループを抜ける
            break

    #ウィジェット設定に戻り自動化用のウィジェットを開く
    time.sleep(10)
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
    if notaccept.text == '以下は受付時間外となりますのでご了承ください。 00:00 - 23:59':
        print("AW03-07 OK")

    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)

#test_AW03_07()

# [AW03-08]営業可能時間を複数設定する
# https://jaqool.atlassian.net/browse/GPT-783
# 

def test_AW03_08():
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)

    ##営業時間の設定
    ##タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
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

    #受付時間をクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(10)
    #受付時間追加ボタンをクリック
    wait = WebDriverWait(driver, 300)
    add_businessh = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/button')))
    add_businessh.click()
    #タイトルを入力
    wait = WebDriverWait(driver, 300)
    businessh_name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/form/div/div[1]/div/div[3]/input')))
    businessh_name.send_keys('AW03-08 title')
    time.sleep(3)
    #対象をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]').click()
    time.sleep(5)
    #プルダウンを表示
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]/div').click()
    time.sleep(10)
    #毎日を選択
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(5)
    #2つ目の時間設定ボタンをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[6]/button').click()
    time.sleep(5)
    #時間を設定
    ####時刻を入力

    #時刻を変換
    #時間を設定
    # 現在の日時を取得
    now = datetime.now()
    # 曜日を取得
    weekday2 = calendar.day_name[now.weekday()]
    # 日付のフォーマットを指定
    #date_format = now.strftime("%Y/%m/%d %a %H:%M")
    #現在時刻
    date_format2 = now.strftime("%H:%M")
    #今日の日付
    monthday_format2 = now.strftime("%m%d")
    
    settingh = str(date_format2[:2])
    sethour = int(settingh)
    #分を設定
    settingm = str(date_format[-2:])
    setminute = int(settingm)
    
    #ケース1 : 23時台の時
    if (settingh == 23) or (settingh == 0):
        #時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(settingh - 1):
            businessh_1st.click()
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59):
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input')
        #保存して閉じますをクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10)  

    #ケース2 : 1-22時台の時
    else:
        #1番目の時計を操作(終了時間のみ)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(sethour - 1):
            businessh_1st.click()
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59):
            businessm_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)

        #2番目の時計を操作(開始時間)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr[2]/td[1]/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(sethour + 1):
            businessh_1st.click()
        #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()
        time.sleep(5)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/div/div/div/div/div/input')
        
        #2番目の時計を操作(終了時間)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr[2]/td[3]/div/div/div/div/div/div/input').click()
        time.sleep(5)
        wait = WebDriverWait(driver, 300)
        businessh_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]')))
        for _ in range(23): #23時に設定
            businessh_1st.click() #受付時間の時間を入力
        #分を設定
        wait = WebDriverWait(driver, 300)
        businessm_1st = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]')))
        #時刻を設定
        for _ in range(59): #59分に設定
            businessm_1st.click()  
                #選択をクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/button').click()

        #保存して閉じますをクリック
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/button').click()
        time.sleep(10)
        flag = True
        
    #ウィジェット設定に戻り自動化用のウィジェットを開く
    time.sleep(10)
    openW()
    time.sleep(15)
    driver.switch_to.window
    wait = WebDriverWait(driver, 180)
    notaccept = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text.d-flex.flex-column.justify-start.px-4.pb-3')))
    if len(notaccept.text) == 42:
        print("AW03-08 OK")
    else :
        print(len(notaccept.text))

#test_AW03_08()

def closetab():
    driver.close()
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    first_tab_handle = tab_handles[0]
    driver.switch_to.window(first_tab_handle)
    cur_url = driver.current_url
    driver.refresh()
    time.sleep(10)

#closetab()

# [AW04-01]不在時のメール受信設定画面に移動する
# https://jaqool.atlassian.net/browse/GPT-785
# 

def test_AW04_01():
    # 自動化用のウィジェットの鉛筆マークをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[7]/div/div/button').click()
    time.sleep(3)
    # 自動化用のウィジェットの①担当グループにて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    # 自動化用のウィジェットの②営業時間にて”保存して次へ”をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    time.sleep(5)
    #ページのタイトルが”不在時のメール受信設定”であるかを判定
    wait = WebDriverWait(driver, 180)
    currentpage = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/label')))
    if currentpage.text == "不在時のメール受信設定":
        print("AW04-01 OK")
    else :
        print(currentpage.text)
        

test_AW04_01()

# [AW04-02]メール送信用フォームを営業時間外に表示設定する
# https://jaqool.atlassian.net/browse/GPT-786
# 

def test_AW04_02():
    #営業時間外をクリック
    time.sleep(10)
    outofbusihour = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/input')
    #営業時間外のチェックボックスがクリックされている
    if outofbusihour.is_selected():
        #メールアドレスを消去
        # 対象の要素を取得
        target_element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]')
        # 対象の要素内に含まれるinputタグの数を数える
        input_tags = target_element.find_elements(By.XPATH,'.//input')
        input_count = len(input_tags)
        for _ in range(input_count):
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]/button').click()
            time.sleep(3)
        # 不在判定時間を消去
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.BACK_SPACE)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.ENTER)
        #チェックボックスをクリック
        outofbusihour.click()
        time.sleep(3)
        #再度チェックボックスをクリック
        outofbusihour.click()
    else :   
        outofbusihour.click()

    time.sleep(10)
    # 自動化用のウィジェットの③不在時のメール受信設定にて”保存して次へ”をクリック
    #driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/button').click()
    #time.sleep(5)
    # 自動化用のウィジェットの④ゲストによる評価にて”戻る”をクリック
    #driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/button').click()
    #time.sleep(10)
    #ページの項目が”不在時メール送信先”であるかを判定
    unavailable_Staff_Mail_Destination = driver.find_element(By.CSS_SELECTOR,'#app > div > div > div > div > div.body.d-flex.align-center.justify-center > div.body-content > div > div > div.lamondo-new-widget-left > div.lamondo-new-widget-left-content > div > div.d-flex.align-start.flex-column.width-100 > div.lamondo-new-widget-email-req-add.px-4.mt-2.width-100.d-flex.align-start.flex-column.justify-start > label')
    #ページの項目が”不在判定時間”であるかを判定
    time_Staff_Did_Not_Respond = driver.find_element(By.CSS_SELECTOR,'#app > div > div > div > div > div.body.d-flex.align-center.justify-center > div.body-content > div > div > div.lamondo-new-widget-left > div.lamondo-new-widget-left-content > div > div.d-flex.align-start.flex-column.width-100 > label')  

    if (unavailable_Staff_Mail_Destination.text == "不在時メール送信先*") & (time_Staff_Did_Not_Respond.text == "不在判定時間*"):
        print("AW04-02 OK")
    else :
        print(unavailable_Staff_Mail_Destination.text) 
        print(time_Staff_Did_Not_Respond.text)

test_AW04_02()

# [AW04-03]不在時メール送信先を設定する
# https://jaqool.atlassian.net/browse/GPT-787
# 

def test_AW04_03():

    staffunavailable = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/div/input')
    #不在時のチェックボックスがクリックされている
    if staffunavailable.is_selected():
        #チェックボックスをクリック
        staffunavailable.click()
        time.sleep(3)
        #再度チェックボックスをクリック
        staffunavailable.click()
    else :   
        staffunavailable.click()

    # メールアドレスを入力
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[1]/form/div/div[1]/div/div[3]/input').send_keys('aw04_03@kotozna.com')
    # 不在判定時間を入力
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(10)

    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[1]/form/div/div[1]/div/div[3]/input')
    mailaddress = element.get_attribute('value')
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input')
    outoftime = element.get_attribute('value')
    if (mailaddress == "aw04_03@kotozna.com") & (outoftime == "10"):
        print("AW04-03 OK")
    else :
        print(mailaddress) 
        print(outoftime)

test_AW04_03()

# [AW04-04]不在時メール送信先を追加する
# https://jaqool.atlassian.net/browse/GPT-788
# 

def test_AW04_04():
    # メールアドレス追加ボタンをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/button').click()  
    time.sleep(5)
    element = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[1]/form/div/div[1]/div/div[3]/input')    
    if len(element) > 0:
        print("AW04-04 OK")

test_AW04_04()

# [AW04-05]不在時メール送信先を削除する
# https://jaqool.atlassian.net/browse/GPT-789
# 
def test_AW04_05():
    # 2番目のメールアドレスを入力
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[1]/form/div/div[1]/div/div[3]/input').send_keys("aw04_05@kotozna.com")  
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[1]/form/div/div[1]/div/div[3]/input')
    mailaddress2 = element.get_attribute('value')
    if (mailaddress2 == "aw04_05@kotozna.com"):
        print("AW04-05 OK")

test_AW04_05()

# [AW04-06]不在判定時間を設定する
# https://jaqool.atlassian.net/browse/GPT-790
# 

def test_AW04_06():
    # 不在判定時間を消去
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(Keys.ENTER)
    # 不在判定時間を入力
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input').send_keys(5)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/form/div/div[1]/div/div[3]/input')
    outoftime = element.get_attribute('value')
    if outoftime == "5":
        print("AW04-06 OK")
        
test_AW04_06()