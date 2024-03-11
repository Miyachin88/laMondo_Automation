import webbrowser
import webbrowser
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import*
import time
import json
import gspread

# Safariに切り替えです
options = webdriver.safari.options.Options()
driver = webdriver.Safari(options=options)
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

"""
OTBのページを開く
"""
def otb():
    print('chinchin')
    # ページに繋ぐ
    driver.get('https://osaka-info.jp/')
    time.sleep(10)
    # クッキーボタンを押下
    driver.find_element(By.XPATH,'//*[@id="onetrust-close-btn-container"]/button').click()
    time.sleep(5)
    # ウィジェットをクリック
    driver.find_element(By.XPATH,'//*[@id="ktzn-tm-icon"]').click()
    time.sleep(20)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(5)
    # スタートボタンを押下
    element = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('Kotozna test 今日の天気')
    # メッセージを送信
    driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div[2]/div/button').click()
    time.sleep(20)

"""
グランスノー英語のページを開く
"""
def granEn():
    print('chinchin')
    # ページに繋ぐ
    driver.get('https://www.okuibuki.co.jp/en/')
    time.sleep(10)
    # ウィジェットをクリック
    driver.find_element(By.XPATH,'//*[@id="ktzn-tm-icon"]').click()
    time.sleep(20)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(5)
    # スタートボタンを押下
    element = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('ことつなテスト(PC) 駐車場はありますか？')
    # メッセージを送信
    driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div[2]/div/button').click()
    time.sleep(20)

"""
グランスノー中国サイトのページを開く
"""
def granCh():
    print('chinchin')
    # ページに繋ぐ
    driver.get('https://www.okuibuki.co.jp/cn/')
    time.sleep(10)
    # ウィジェットをクリック
    driver.find_element(By.XPATH,'//*[@id="ktzn-tm-icon"]').click()
    time.sleep(20)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(5)
    # スタートボタンを押下
    element = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('ことつなテスト(PC) リフト券はいくらですか？')
    # メッセージを送信
    driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div[2]/div/button').click()
    time.sleep(20)

"""
グランスノー中国LPのページを開く
"""
def granCl():
    print('chinchin')
    # ページに繋ぐ
    driver.get('https://cn.okuibuki.com/')
    time.sleep(10)
    # ウィジェットをクリック
    driver.find_element(By.XPATH,'//*[@id="ktzn-tm-icon"]').click()
    time.sleep(20)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(5)
    # スタートボタンを押下
    element = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('ことつなテスト(PC) シャトルバスはありますか？')
    # メッセージを送信
    driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div[2]/div/button').click()
    time.sleep(20)

"""
グランスノー台湾LPのページを開く
"""
def granTw():
    print('chinchin')
    # ページに繋ぐ
    driver.get('https://tw.okuibuki.com/')
    time.sleep(10)
    # ウィジェットをクリック
    driver.find_element(By.XPATH,'//*[@id="ktzn-tm-icon"]').click()
    time.sleep(20)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(5)
    # スタートボタンを押下
    element = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('ことつなテスト(PC) 日帰りはできますか？')
    # メッセージを送信
    driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div[2]/div/button').click()
    time.sleep(20)

"""
グランスノー香港LPのページを開く
"""
def granHk():
    print('chinchin')
    # ページに繋ぐ
    driver.get('https://hk.okuibuki.com/')
    time.sleep(10)
    # ウィジェットをクリック
    driver.find_element(By.XPATH,'//*[@id="ktzn-tm-icon"]').click()
    time.sleep(20)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(5)
    # スタートボタンを押下
    element = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('ことつなテスト(PC) 電車での行き方は？')
    # メッセージを送信
    driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div[2]/div/button').click()
    time.sleep(20)
    
"""
文化財のページを開く
"""
def bunka():
    print('chinchin')
    # ページに繋ぐ
    driver.get('https://hiddenheritage.jp/')
    time.sleep(10)
    # ウィジェットをクリック
    driver.find_element(By.XPATH,'//*[@id="ktzn-tm-icon"]').click()
    time.sleep(20)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(5)
    # スタートボタンを押下
    element = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('ことつなテスト(PC) 歴史のあるお寺は？')
    # メッセージを送信
    driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div[2]/div/button').click()
    time.sleep(20)

def jewel():
    print('chinchin')
    # ページに繋ぐ
    driver.get('https://www.jewelchangiairport.com')
    time.sleep(10)
    # ウィジェットをクリック
    driver.find_element(By.XPATH,'//*[@id="ktzn-tm-icon"]').click()
    time.sleep(20)
    # iframeに切り替え
    iframe = driver.find_element(By.ID,'ktzn-tm-frame')
    driver.switch_to.frame(iframe)
    time.sleep(5)
    # スタートボタンを押下
    element = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div/div/div[6]/div/div')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10)
    # メッセージを入力
    element = driver.find_element(By.XPATH, '//*[@id="inputMessage"]').send_keys('ことつなテスト(PC) 免税店は？')
    # メッセージを送信
    driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[2]/div[2]/div/button').click()
    time.sleep(20)