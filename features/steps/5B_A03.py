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


# Scenario: [A03-01]ウィジェットを表示する Show widget
# https://jaqool.atlassian.net/browse/GPT-760
@Given('管理画面を開いている / The management screen is open')
def a02_01_g(aaa):
    #ログイン
    driver.get('https://beta-tenant-admin.im.kotozna.chat/ja/login')
    time.sleep(5)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('developer+kenta-lamondo@kotozna.com')
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('000000')
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[3]/button').click()
    # dev要素を見つけて、そのテキストを取得する
    time.sleep(15)
@When('左下の「スタッフ画面を開く」をクリックする / Click "Open Staff Screen" at the bottom left')
def a02_01_w(aaa):
    #スタッフ画面を開くを押下
    openstaff = WebDriverWait(driver, 300)
    open = openstaff.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[7]/div/button')))
    open.click()
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
@Then('ログイン画面が開く / The log in screen will be displayed')
def a03_01_w(aaa):
    # URL取得
    time.sleep(10)
    cur_url = driver.current_url
    assert 'https://beta-staff.im.kotozna.chat/ja/main/conversations' in cur_url