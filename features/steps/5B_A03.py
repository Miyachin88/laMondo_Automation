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
A03スタッフ画面に移動する Go to the staff panel
https://jaqool.atlassian.net/browse/GPT-767
"""

#@BDDTEST-GPT-768
#Scenario: [A03-01]スタッフ画面へのリンクをクリックする Go to the staff panel via the link
#https://jaqool.atlassian.net/browse/GPT-768

@given('管理画面を開いている / The management screen is open')
def chinsara_G(chinsara):
    print(chinsara)

#
@when('左下の「スタッフ画面を開く」をクリックする / Click "Open Staff Screen" at the bottom left')
def chinsara_W(chinsara):
    time.sleep(3)

#
@then('ログイン画面が開く / The log in screen will be displayed')
def chinsara_T(chinsara):
    print(chinsara)