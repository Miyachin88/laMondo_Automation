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


def chinchin():
    # 
    print('chinchin')
    driver.get('https://kotozna.com/')
    time.sleep(10)
    driver.find_element(By.XPATH,'//*[@id="ktzn-tm-icon"]').click()
    time.sleep(20)
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    # iframeに切り替え
    driver.switch_to.frame(iframe)
    time.sleep(5)
    element = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('Kotozna test 製品の価格を教えて？')
    driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div[2]/div/button').click()
    time.sleep(20)
    

"""
A01日本人が管理画面にログインする Japanese administrator tries to log in to the Admin Panel
https://jaqool.atlassian.net/browse/GPT-753
"""


# [AB01-01]メールアドレスを入力する Enter your email address on the login screen
# https://jaqool.atlassian.net/browse/GPT-754

driver.get('https://beta-tenant-admin.im.kotozna.chat/ja/login')
time.sleep(10)

element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('kenta+b230109-admin@kotozna.com')
time.sleep(3)

element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input')
chinsara = element.get_attribute('value')

# [AB01-02]PINコードを入力する Enter your PIN code to complete login
# https://jaqool.atlassian.net/browse/GPT-755
#

#ログインボタンを押下
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[3]/button').click()
time.sleep(5)

#

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('000000')
time.sleep(10)

#

element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input')
chinsara = element.get_attribute('value')   
cur_url = driver.current_url
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()

# [AB01-03]使い方動画を閲覧する Watching how-to video
# https://jaqool.atlassian.net/browse/GPT-756
# 

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

# dev要素を見つけて、そのテキストを取得する
dev_element = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[2]')  # dev要素をCSSセレクタで見つける場合
dev_text = dev_element.text
if "基本設定" in dev_text:
    # 特定の文字列が含まれている場合の処理
    print("OK")
else:
# 特定の文字列が含まれていない場合の処理
    print("NG")


time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[1]/button').click()
time.sleep(10)


driver.current_window_handle
widget_title = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[1]').text
if 'あごぽよクリーニング香椎本店' == widget_title:
    print('3-1OK')

#
iframe = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div[3]/div[1]/iframe')))
movsrc = iframe.get_attribute('src')
print(movsrc)
if 'https://www.youtube.com/embed/e23dN762YTg' == movsrc:
    print('3-2OK')



# [AB01-04]ヘルプセンターにアクセスする Open the help center link
# https://jaqool.atlassian.net/browse/GPT-757
#

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
#別タブへ移動  
driver.switch_to.window(driver.window_handles[1])    

# [AB01-05]表示言語を変更する Changing display language
# https://jaqool.atlassian.net/browse/GPT-758
#

cur_url = driver.current_url
if 'https://lamondo.manual.kotozna.com/ja/home' == cur_url:
    print('4-1OK')
    # 現在のタブを閉じる
    driver.close()

driver.switch_to.window(driver.window_handles[0]) 
time.sleep(5)


#言語を切り替えボタンを押下
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[3]/div/div/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/div/div/div').click()
time.sleep(5)

element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/span').text
if 'Basic Settings' == element:
    print('5-1OK')
#ウィジェット設定へ移動
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()
time.sleep(3)
element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/table/tbody/tr[1]/td[1]/span').text
if 'あごぽよクリーニング香椎本店' == element:
    print('5-2OK')
    

# [AB01-06]ハンバーガーボタンで表示方法を変更 Changing display with Hamburger button
# https://jaqool.atlassian.net/browse/GPT-1060
#ハンバーガーボタンをクリック
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[1]').click()
time.sleep(3)
element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]')
width = element.get_attribute('style')
if width[7:9] == '60':
    print('AB01-06 OK')
else :
    print(width[7:9])

time.sleep(3)    
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[1]').click()


#Scenario: [A02-01]ウィジェットを表示する Show widget
#https://jaqool.atlassian.net/browse/BBS-65
#言語を切り替えボタンを押下
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[3]/div/div/button').click()
time.sleep(5)
#日本語を選択
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/div/div').click()
time.sleep(5)    

#基本設定へ移動
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]').click()
time.sleep(10)  

#ウィジェットをON
toggle_button = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div')))
#一度OFF
toggle_button.click()
#再度ON
time.sleep(10)
toggle_button.click()
print('A02-1-1 OK')
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
print(driver.current_url)
#element = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/div/div[6]/div/div')
#driver.execute_script('arguments[0].click();', element)
toggle_button = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/div/div[1]/div/main/div/div/div[2]/div/div/div[1]/div/div[2]')))
element = toggle_button.text
print(element)
if 'あごぽよクリーニング香椎本店のチャットボットへようこそ！チャットサービスはlaMondoを搭載しています。' == element:
    print('A02-1-2 OK')

#これは元の画面に戻るだけ
# タブのハンドルを取得する
tab_handles = driver.window_handles
# 1番目のタブに切り替える
second_tab_handle = tab_handles[0]
driver.switch_to.window(second_tab_handle)
time.sleep(10)
#戻るボタンをクリック
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[4]/div[2]/button').click()


#Scenario: [A02-02]ウィジェットを非表示にする Hide widget
#https://jaqool.atlassian.net/browse/GPT-761
#基本設定へ移動
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]').click()
#ウインドウを現在の画面に戻す
driver.current_window_handle
time.sleep(3)
#ウィジェットをOFF
toggle_button = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div')))
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
#ページのアクセス不可文言を確認
toggle_button = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/p')))
element = toggle_button.text
print(element)
if 'チャット機能は現在ご利用いただけません。' == element:
    print('A02-2 OK')


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
time.sleep(3)
#Scenario: [A02-03]ゲストによる回答評価の利用を有にする（Survey）Make use of guest response evaluation (Survey)
#https://jaqool.atlassian.net/browse/GPT-761
#ゲスト評価をOFF
toggle_button = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div')))
toggle_button.click()
time.sleep(3)
#ゲスト評価をON
toggle_button = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div')))
toggle_button.click()
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
#チャットを評価の文言を確認
evalchat = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/div/div[1]/div/main/div/div/div[2]/div[2]/div/div')))

element = evalchat.text
print(element)
if 'チャットを評価！' == element:
    print('A02-3 OK')


#Scenario: [A02-04]ゲストによる回答評価の利用を無にする（Survey）Eliminate the use of guest response ratings (Survey)
#https://jaqool.atlassian.net/browse/GPT-763

#これは元の画面に戻るだけ
# タブのハンドルを取得する
tab_handles = driver.window_handles
# 1番目のタブに切り替える
second_tab_handle = tab_handles[0]
driver.switch_to.window(second_tab_handle)
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
#チャットを評価の文言がないことを判定
evalchat = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/div/div[1]/div/main/div/div/div[2]/div[2]/div/div')))

element = evalchat.text
print(element)
if 'チャットを評価！' != element:
    print('A02-4 OK')

#Scenario: [A02-05]WorkCodeを追加する Add work code
#https://jaqool.atlassian.net/browse/GPT-764

#Given 基本設定画面のワークコードマスタに、現在登録されているワークコード一覧が表示されている / A list of work codes currently registered in the work code master is displayed.
# タブのハンドルを取得する
tab_handles = driver.window_handles
# 1番目のタブに切り替える
second_tab_handle = tab_handles[0]
driver.switch_to.window(second_tab_handle)
time.sleep(5)
#When 「＋」ボタンを押し、ワークコード名を入力して保存する / Press the "+" button, enter a name and save
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/button').click()
time.sleep(2)
driver.switch_to.window
time.sleep(2)
element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[3]/div/form/div[2]/div[1]/div/div[3]/input').send_keys('ワークコードテスト')
time.sleep(3)
#保存ボタンを押下して、ワークコードを保存
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[4]/div[3]/button').click()
time.sleep(3)
driver.switch_to.window
#ウィジェット設定へ移動
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]').click()
time.sleep(3)
#基本設定へ移動
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]').click()
time.sleep(5)  
#Then ワークコード一覧に数字→アルファベット→ひらがな→漢字の順に新たなワークコードが追加され、スタッフ画面にも同様に表示される / A new work code is added to the work code list in the order of numbers → alphabet → hiragana → kanji, and the same is displayed on the staff screen.
evalchat = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[2]/span')))
#作成したワークコードの名前を判定
element = evalchat.text
print(element)
if 'ワークコードテスト' == element:
    print('A02-5 OK')

#Scenario: [A02-06]WorkCodeを削除する Delete workcode
#https://jaqool.atlassian.net/browse/GPT-765

#ワークコードのチェックボックスをチェック
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[1]/div/div[1]/div/div/div/input').click()
time.sleep(3)
#ゴミ箱をクリック
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/button').click()
time.sleep(3)
#Then ワークコード一覧に数字→アルファベット→ひらがな→カタカナ→漢字の順に新たなワークコードが追加され、スタッフ画面にも同様に表示される / A new work code is added to the work code list in the order of numbers → alphabet → hiragana → kanji, and the same is displayed on the staff screen.
wkcddelete = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[2]/span')))
#作成したワークコードの名前を判定
element = wkcddelete.text
print(element)
if '一般' == element:
    print('A02-6 OK')
else :
    print('A02-6 NG')

#Given ワークコードマスタに現在登録されているワークコード一覧が表示されている / A list of work codes currently registered in the work code master is displayed.
#When 削除したいワークコードに✅をし、ごみ箱ボタンをクリックする /✅ on the work code you want to delete and click the Recycle Bin button
#Then ワークコード一覧から削除され、スタッフ画面にも反映されている / It has been deleted from the work code list and reflected on the staff screen.

#Scenario: [A02-07]WorkCodeを編集する Edit workcode
#https://jaqool.atlassian.net/browse/GPT-766
#ゲスト評価をONに戻す
toggle_button = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div')))
toggle_button.click()

##ワークコードテストを追加
#When 「＋」ボタンを押し、ワークコード名を入力して保存する / Press the "+" button, enter a name and save
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/button').click()
time.sleep(2)
driver.switch_to.window
time.sleep(2)
element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[3]/div/form/div[2]/div[1]/div/div[3]/input').send_keys('ワークコードテスト')
time.sleep(3)
#保存ボタンを押下して、ワークコードを保存
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[4]/div[3]/button').click()
time.sleep(3)
driver.switch_to.window
time.sleep(3)
#ワークコードテストの名称を編集
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[3]/div/div/button').click()

#ワークコードテストの名称を編集して
wait = WebDriverWait(driver, 300)
edittext = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[2]/div/form/div/div/div/div[3]/input')))
edittext.clear()
time.sleep(3)
edittext.send_keys('編集')
time.sleep(3)
#ワークコードのチェックボックスをチェック
wait2 = WebDriverWait(driver, 300)
wkcd = wait2.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[3]/div/div/button/span[3]/i')))
wkcd.click()
driver.refresh()
time.sleep(10)
#編集後の名前をチェック
editcheck = WebDriverWait(driver,180).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[2]/span')))
#作成したワークコードの名前を判定
element = editcheck.text
print(element)
if 'ワークコードテスト編集' == element:
    print('A02-7 OK')
else:
    print(element)

#終わったらワークコードを削除する。
time.sleep(10)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[5]/td[1]/div/div[1]/div/div/div/input').click()
time.sleep(3)
#ゴミ箱をクリック
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/button').click()
time.sleep(10)


#Scenario: [AB03-01]スタッフ画面へのリンクをクリックする Go to the staff panel via the link
#https://jaqool.atlassian.net/browse/GPT-767

#Given ワークコードマスタに現在登録されているワークコード一覧が表示されている / A list of work codes currently registered in the work code master is displayed.
#When 編集したいワークコードのペンシルマークをクリックし、名前を編集する / Click the pencil mark of the work code you want to edit, and edit name
#Then どこかをクリックすると保存され、スタッフ画面にも反映されている / Click anywhere to save it and reflect it on the staff screen
#スタッフ画面を開くを押下
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[6]/div/button').click()
time.sleep(10)
#別タブへ移動  
# 現在のタブのハンドルを取得
current_handle = driver.current_window_handle
# タブのハンドルのリストを取得
all_handles = driver.window_handles
# 2番目のタブのハンドルを特定
target_handle = all_handles[1]
# 2番目のタブに切り替え
driver.switch_to.window(target_handle)

cur_url = driver.current_url
print(cur_url)
"""
# ポップアップダイアログに切り替える
alert = Alert(driver)
# ポップアップダイアログのテキストを表示
print(alert.text)
# ポップアップダイアログで「許可する」ボタンをクリック
alert.accept()
# ポップアップダイアログが閉じるまで待機
WebDriverWait(driver, 10).until(EC.alert_is_present())
"""
# URL取得
cur_url = driver.current_url
if 'https://lamondo.im.kotozna.chat/beta/index.html?hash_code=36c172acb1c1fb341e6c56891231b9b33d34a88cb01d7452f9dde711e64e1be2' in cur_url:
    # 特定の文字列が含まれている場合の処理
    print("A03-1 OK")
else:
    print("A03-1 NG")