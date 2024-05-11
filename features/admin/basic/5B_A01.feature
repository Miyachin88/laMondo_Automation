@BDDSTORY-GPT-753
Feature: 日本人が管理画面にログインする Japanese administrator tries to log in to the Admin Panel
  @BDDTEST-GPT-754
  Scenario: [A01-01]メールアドレスを入力する Enter your email address on the login screen
    Given laMondo管理画面を開く Open the lamondo admin panel
    When メールアドレスを入力する Input email address
    Then PINコード入力画面に遷移し、PINコードが送信される Transit to the PIN code input screen and send the PIN code

  @BDDTEST-GPT-755
  Scenario: [A01-02]PINコードを入力する Enter your PIN code to complete login
    Given PINコード入力画面が表示されているThe PIN code entry screen is displayed
    When PINコードを入力して「ログイン」をクリックEnter your PIN code and click "Login"
    Then 管理画面にログイン完了する（＝基本設定のページが開く）Login to the management screen is completed (= the basic setting page opens)

  @BDDTEST-GPT-756
  Scenario: [A01-03]使い方動画を閲覧する Watching how-to video
    Given laMondo管理画面にログインしている / You are logged in to the admin panel
    Given トップバーと基本設定画面が表示されている1 / The top bar and the basic settings are displayed
    When トップバーの[使い方動画を見る]ボタンを押下 / Select the [Using laMondo] button on the top bar
    Then ウィジェット1と記載されたウィンドウが開く / A window will open labeled Widget 1
    Then 使い方動画が再生できる / How-to video can be played

  @BDDTEST-GPT-757
  Scenario: [A01-04]ヘルプセンターにアクセスする Open the help center link
    Given 管理画面にログインしている2 / You are logged in to the admin panel
    Given トップバーと基本設定画面が表示されている2 / The top bar and the basic settings are displayed
    When ？アイコンを押下 / Select "?" button
    Then 別タブにて、"Kotozna laMondoヘルプセンター"サイトが開く / "Kotozna laMondo Help Center" website will be opend in a new tab
    Then 管理画面の表示言語が日本語の場合ヘルプセンターは日本語で表示され、管理画面の表示言語が日本語以外の場合ヘルプセンターは英語で表示される / If the admin panel display language is Japanese, the website will be displayed in Japanese, and if the admin panel display language is other than Japanese, the website will be displayed in English.

  @BDDTEST-GPT-758
  Scenario: [A01-05]表示言語を変更する Changing display language
    Given 管理画面にログインしている3 You are logged in to the admin panel
    Given トップバーと基本設定画面が表示されている3 The top bar and the basic settings are displayed
    When 地球儀アイコンを押下 Select the globe icon
    When 任意の言語を選択する Select any language  
    Then 管理画面の表示言語が選択した言語で表示される The display language of admin panel will be displayed in the selected language
    Then ただし、ワークコード名、ウィジェット名、グループ名、ユーザー名（アカウント名）は変わらない Work code names, widget names, group names, and user names wont be changed

  @BDDTEST-GPT-1060
  Scenario: [AB01-06]ハンバーガーボタンで表示方法を変更 Changing display with Hamburger button
    Given 基本設定の画面が表示されている1 The basic setting screen is displayed
    Given 左のメニューバーに「ウィジェット設定」など、設定機能名とアイコンが表示されている Settings names such as "Widget settings" and icons are listed on the left
    When 左上のハンバーガーボタンをクリックする Click the Hamburger button on the upper left
    Then 左のメニューバーの設定機能名が非表示になり、アイコン表示のみになる Only icons are displayed, and settings names are hidden