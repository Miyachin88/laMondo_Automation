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


# [A01-01]メールアドレスを入力する Enter your email address on the login screen
# https://jaqool.atlassian.net/browse/GPT-754

driver.get('https://beta-tenant-admin.im.kotozna.chat/ja/login')
time.sleep(10)


element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('kenta+b230109-admin@kotozna.com')
time.sleep(3)



element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input')
chinsara = element.get_attribute('value')

# [A01-02]PINコードを入力する Enter your PIN code to complete login
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

# [A01-03]使い方動画を閲覧する Watching how-to video
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



# [A01-04]ヘルプセンターにアクセスする Open the help center link
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
print('A02-1OK')
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
    print('A02-2OK')