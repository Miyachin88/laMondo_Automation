import webbrowser
import chinchin
import susara
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import*
import time
import json
import safarisusara

"""
safarisusara.otb()
safarisusara.granEn()
safarisusara.granCh()
safarisusara.granCl()
safarisusara.granTw()
safarisusara.granHk()
safarisusara.bunka()
safarisusara.jewel()
"""

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

susara.otb()
susara.granEn()
susara.granCh()
susara.granCl()
susara.granTw()
susara.granHk()
susara.bunka()
susara.jewel()


