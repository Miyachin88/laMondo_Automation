from fileinput import filename
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import*
import time

#ドライバのインストール
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#[BBS A16-01]管理画面の言語変更（英語） Change admin panel language to English
#https://jaqool.atlassian.net/browse/BBS-65
@given('You are viewing any community')
def chinsara_G(chinsara):
    driver.get('https://beta-tenant-admin.im.kotozna.chat/ja/login')
    time.sleep(10)

@when('Select English from the language change button on the upper right')
def chinsara_W(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input').send_keys('kenta+b230109-admin@kotozna.com')
    time.sleep(3)


@then('The admin panel including the community names and post are displayed in English')
def chinsara_T(chinsara):
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/form/div/div[1]/div/div[3]/input')
    chinsara = element.get_attribute('value')
    assert ('kenta+b230109-admin@kotozna.com' == chinsara) is True