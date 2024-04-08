@BDDSTORY-GPT-767
Feature: A03スタッフ画面に移動する Go to the staff panel
  @BDDTEST-GPT-768
  Scenario: [A03-01]スタッフ画面へのリンクをクリックする Go to the staff panel via the link
    Given 管理画面を開いている / The management screen is open
    When 左下の「スタッフ画面を開く」をクリックする / Click "Open Staff Screen" at the bottom left
    Then ログイン画面が開く / The log in screen will be displayed