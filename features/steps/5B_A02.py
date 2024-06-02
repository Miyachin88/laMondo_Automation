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
from selenium.webdriver.chrome.options import Options


# Chromeオプションを設定:通知を拒否
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Scenario: [A02-01]ウィジェットを表示する Show widget
# https://jaqool.atlassian.net/browse/GPT-760
@Given('ゲスト画面にウィジェットが表示されていない / The widget is not displayed on the guest screen')
def a02_01_g(aaa):
    print('a')
@When('「すべてのウィジェットを有効にする。」のトグルをONにする / Turn on the toggle for "Enable all widgets."')
def a02_01_w(aaa):
    #ログイン
    driver.get('https://beta-tenant-admin.im.kotozna.chat/ja/login')
    time.sleep(5)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('developer+kenta-lamondo@kotozna.com')
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('000000')
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    # dev要素を見つけて、そのテキストを取得する
    time.sleep(10)

    #ウィジェットをON
    toggle_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/input')
    if toggle_button.is_selected():
        time.sleep(3)
    else:
        #一度OFF
        toggle_button.click()
        #再度ON
        time.sleep(10)
        toggle_button.click()        
    #ウィジェット設定へ移動
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()
    time.sleep(10)
    #infoボタンをクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[1]/td[6]/div/div/button').click()
    driver.switch_to.window
    time.sleep(15)
    #ウィジェットを開く
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div[2]').click()
    time.sleep(10) 

    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 2番目のタブに切り替える
    second_tab_handle = tab_handles[1]
    driver.switch_to.window(second_tab_handle)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(30)
@Then('ゲスト画面で該当のウィジェットが表示されている / The corresponding widget is displayed on the guest screen')
def a02_01_t(aaa):
    print('a')
@Then('ゲスト画面を開くと、通常フローでGPT・スタッフに問い合わせが送信できる')
def a02_01_t2(aaa):
    toggle_button = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/div/div[1]/div/main/div/div/div[2]/div/div/div[1]/div/div[2]')))
    element = toggle_button.text
    assert 'あごぽよクリーニング香椎本店のチャットボットへようこそ！チャットサービスはlaMondoを搭載しています。' == element
    #これは元の画面に戻るだけ
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    second_tab_handle = tab_handles[0]
    driver.switch_to.window(second_tab_handle)
    time.sleep(10)
    #戻るボタンをクリック
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[4]/div[2]/button').click()


# Scenario: [A02-02]ウィジェットを非表示にする Hide widget
# https://jaqool.atlassian.net/browse/GPT-761

@Given('ゲスト画面にウィジェットが表示されている / The widget is displayed on the guest screen')
def a02_02_g(aaa):
    print('a')
@When('「すべてのウィジェットを有効にする。」のトグルをOFFにする / Turn off the toggle for "Enable all widgets."')
def a02_02_w(aaa):
    #基本設定へ移動
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]').click()
    #ウインドウを現在の画面に戻す
    driver.current_window_handle
    time.sleep(3)
    #ウィジェットをOFF
    toggle_button = toggle_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/input')
    toggle_button.click()
    time.sleep(3)
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 2番目のタブに切り替える
    second_tab_handle = tab_handles[1]
    driver.switch_to.window(second_tab_handle)
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
@Then('ゲスト画面で該当のウィジェットが表示されていない / The widget is not displayed on the guest screen')
def a02_02_t(aaa): 
    print('a')
@Then('ゲスト画面を開くと、「チャット機能は現在ご利用できません」が表示される')
def a02_02_t2(aaa):
    #ページのアクセス不可文言を確認
    toggle_button = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/p')))
    element = toggle_button.text
    #print(element)
    assert 'チャット機能は現在ご利用いただけません。' == element
    #これは元の画面に戻るだけ
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    second_tab_handle = tab_handles[0]
    driver.switch_to.window(second_tab_handle)
    time.sleep(3)
    #ウィジェットをON
    toggle_button = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div')))
    toggle_button.click()
    time.sleep(10)



# Scenario: [A02-03]ゲストによる回答評価の利用を有にする（Survey）Make use of guest response evaluation (Survey)
# https://jaqool.atlassian.net/browse/GPT-762

@Given('"チャット終了後の「ゲスト評価」を利用する。"トグルがOFFになっている "Use the guest evaluation after the chat. " is OFF')
def a02_03_g(aaa):
    print('a')
    print('b')
    time.sleep(1)
@When('"チャット終了後の「ゲスト評価」を利用する。"のトグルをONにする Turn on the "Use the guest evaluation after the chat."')
def a02_03_t1(aaa):
    #ゲスト評価をON
    toggle_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/input')
    if toggle_button.is_selected():   
        time.sleep(3)
    else:
        toggle_button.click()
        time.sleep(3)
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 2番目のタブに切り替える
    second_tab_handle = tab_handles[1]
    driver.switch_to.window(second_tab_handle)
    time.sleep(10)
    driver.refresh()
    time.sleep(10)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(5)
    # スタートボタンを押下
    element = driver.find_element(By.XPATH,'/html/body/span/div/div[1]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('A02-03 こんにちは')
    # メッセージを送信
    driver.find_element(By.XPATH,'/html/body/span/div/div[1]/div/main/div/div/div[2]/div[2]/div/button[2]').click()
    time.sleep(30)
@Then('ステップ④ゲストによる評価の「ゲストによる評価を利用する」がONになる Guest Rating on the Step 4 is turned ON')
def a02_03_t2(aaa):
    print('a')
@Then('ゲスト画面で、GPTからの回答後ゲスト評価が表示される After GPT replies, the Guest Rating is displayed on the guest screen')
def a02_03_t2(aaa):
    #チャットを評価の文言を確認
    evalchat = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/div/div[1]/div/main/div/div/div[2]/div[2]/div/div')))
    element = evalchat.text
    #print(element)
    assert 'チャットを評価！' == element

# Scenario: [A02-04]ゲストによる回答評価の利用を無にする（Survey）Eliminate the use of guest response ratings (Survey)
# https://jaqool.atlassian.net/browse/GPT-763

@Given('ステップ④ゲストによる評価の「ゲストによる評価を利用する」がONになっている Guest Rating on the Step 4 is ON')
def a02_04_g(aaa):
    #これは元の画面に戻るだけ
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    second_tab_handle = tab_handles[0]
    driver.switch_to.window(second_tab_handle)
@When('"ゲスト評価"のトグルをOFFにする Turn off the "Guest Rating"')
def a02_04_w(aaa):
    time.sleep(3)
    #ゲスト評価をOFF
    toggle_button = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div')))
    toggle_button.click()
    time.sleep(3)
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 2番目のタブに切り替える
    second_tab_handle = tab_handles[1]
    driver.switch_to.window(second_tab_handle)
    time.sleep(10)
    #一度リロード
    driver.refresh()
    time.sleep(10)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(5)
    # スタートボタンを押下
    element = driver.find_element(By.XPATH,'/html/body/span/div/div[1]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('A02-04 こんにちは')
    # メッセージを送信
    driver.find_element(By.XPATH,'/html/body/span/div/div[1]/div/main/div/div/div[2]/div[2]/div/button[2]').click()
    time.sleep(30)
@Then('ステップ④ゲストによる評価の「ゲストによる評価を利用する」がOFFになる Guest Rating on the Step 4 is turned OFF')
def a02_04_t(aaa):
    print('a')
@Then('ゲスト画面で、GPTからの回答後にゲスト評価が表示されなくなる On the guest screen, the Guest Rating is no longer displayed after GPT replies')
def a02_04_t2(aaa):
    #チャットを評価の文言がないことを判定
    evalchat = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/div/div[1]/div/main/div/div/div[2]/div[2]/div/div')))
    element = evalchat.text
    #print(element)
    assert 'チャットを評価！' != element
    # 現在のタブを閉じる
    driver.close()

# Scenario: [A02-05]WorkCodeを追加する Add work code
# https://jaqool.atlassian.net/browse/GPT-764

@Given('基本設定画面のワークコードマスタに、現在登録されているワークコード一覧が表示されている / A list of work codes currently registered in the work code master is displayed.')
def a02_05_g(aaa):
    print('a')
    time.sleep(1)
@When('「＋」ボタンを押し、ワークコード名を入力して保存する / Press the "+" button, enter a name and save')
def a02_05_w(aaa):
    #Given 基本設定画面のワークコードマスタに、現在登録されているワークコード一覧が表示されている / A list of work codes currently registered in the work code master is displayed.
    # タブのハンドルを取得する
    tab_handles = driver.window_handles
    # 1番目のタブに切り替える
    second_tab_handle = tab_handles[0]
    driver.switch_to.window(second_tab_handle)
    time.sleep(5)
    
    #事前にワークコードを削除
    # 対象の要素を取得
    target_element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody')
    # 対象の要素内に含まれるinputタグの数を数える
    input_tags = target_element.find_elements(By.XPATH,'.//tr')
    input_count = len(input_tags)
    if input_count == 6:
        #ワークコードのチェックボックスをチェック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[1]/div/div[1]/div/div/div/input').click()
        time.sleep(3)
        #ゴミ箱をクリック
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/button').click()
        time.sleep(5)

    #When 「＋」ボタンを押し、ワークコード名を入力して保存する / Press the "+" button, enter a name and save
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/button').click()
    time.sleep(2)
    #driver.switch_to.window
    time.sleep(2)
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[3]/div/form/div[2]/div[1]/div/div[3]/input').send_keys('ワークコードテスト')
    time.sleep(3)
    #保存ボタンを押下して、ワークコードを保存
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[4]/div[3]/button').click()
    driver.refresh()
    time.sleep(10)
@Then('ワークコード一覧に数字→アルファベット→ひらがな→漢字の順に新たなワークコードが追加され、スタッフ画面にも同様に表示される / A new work code is added to the work code list in the order of numbers → alphabet → hiragana → kanji, and the same is displayed on the staff screen.')
def a02_05_t2(aaa):
    #Then ワークコード一覧に数字→アルファベット→ひらがな→漢字の順に新たなワークコードが追加され、スタッフ画面にも同様に表示される / A new work code is added to the work code list in the order of numbers → alphabet → hiragana → kanji, and the same is displayed on the staff screen.
    evalchat = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[2]/span')))
    #作成したワークコードの名前を判定
    element = evalchat.text
    #print(element)
    assert 'ワークコードテスト' == element

# Scenario: [A02-06]WorkCodeを削除する Delete workcode
# https://jaqool.atlassian.net/browse/GPT-765

@Given('ワークコードマスタに現在登録されているワークコード一覧が表示されている1 / A list of work codes currently registered in the work code master is displayed.')
def a02_06_g(aaa):
    print('a')
@When('削除したいワークコードに✅をし、ごみ箱ボタンをクリックする  /✅  on the work code you want to delete and click the Recycle Bin button')
def a02_06_w(aaa):
    #ワークコードのチェックボックスをチェック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[1]/div/div[1]/div/div/div/input').click()
    time.sleep(3)
    #ゴミ箱をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/button').click()
    time.sleep(3)
@Then('ワークコード一覧から削除され、スタッフ画面にも反映されている / It has been deleted from the work code list and reflected on the staff screen.')
def a02_06_t(aaa):
    #Then ワークコード一覧に数字→アルファベット→ひらがな→カタカナ→漢字の順に新たなワークコードが追加され、スタッフ画面にも同様に表示される / A new work code is added to the work code list in the order of numbers → alphabet → hiragana → kanji, and the same is displayed on the staff screen.
    wkcddelete = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[2]/span')))
    #作成したワークコードの名前を判定
    element = wkcddelete.text
    #print(element)
    assert '一般' == element

# Scenario: [A02-07]WorkCodeを編集する Edit workcode
# https://jaqool.atlassian.net/browse/GPT-766

@Given('ワークコードマスタに現在登録されているワークコード一覧が表示されている2 / A list of work codes currently registered in the work code master is displayed.')
def a02_07_g(aaa):
    print('a')
@When('編集したいワークコードのペンシルマークをクリックし、名前を編集する / Click the pencil mark of the work code you want to edit, and edit name')
def a02_07_w(aaa):
    #ゲスト評価をONに戻す
    toggle_button = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div')))
    toggle_button.click()

    ##ワークコードテストを追加
    #When 「＋」ボタンを押し、ワークコード名を入力して保存する / Press the "+" button, enter a name and save
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/button').click()
    time.sleep(5)
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[3]/div/form/div[2]/div[1]/div/div[3]/input').send_keys('ワークコードテスト')
    time.sleep(3)
    #保存ボタンを押下して、ワークコードを保存
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[4]/div[3]/button').click()
    time.sleep(3)
    driver.refresh()
    time.sleep(5)
    #ワークコードテストの名称を編集(ワークコードテストの鉛筆ボタンをクリック)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[3]/div/div/button').click()
    #ワークコードテストの名称を編集して
    wait = WebDriverWait(driver, 300)
    edittext = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[2]/div/form/div/div/div/div[3]/input')))
    edittext.send_keys('編集')
    time.sleep(3)
    #ワークコードのチェックボックスをチェック
    wait2 = WebDriverWait(driver, 300)
    wkcd = wait2.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[3]/div/div/button/span[3]/i')))
    wkcd.click()
    time.sleep(10)
@Then('どこかをクリックすると保存され、スタッフ画面にも反映されている / Click anywhere to save it and reflect it on the staff screen')
def a02_07_t(aaa):
    #編集後の名前をチェック
    editcheck = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[2]/span')))
    #作成したワークコードの名前を判定
    element = editcheck.text
    assert 'ワークコードテスト編集' == element
    #終わったらワークコードを削除する。
    time.sleep(10)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[1]/div/div[1]/div/div/div/input').click()
    time.sleep(3)
    #ゴミ箱をクリック
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/button').click()
    time.sleep(10)