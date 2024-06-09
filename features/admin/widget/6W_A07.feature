@BDDSTORY-GPT-792
Feature: Create New Widget Step ❻　デザイン設定
  @BDDTEST-GPT-341
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW07-01]ウィジェットロゴを設定する Set Widget Logo
    Given 「❻デザイン設定」画面が表示されている1 ❻Design Setting screen is displayed
    When ウィジェットロゴの「ロゴを変更」をクリックし、画像データをアップロードするSelect "Change Logo" and upload an image to be used
    Then 表示サンプルが選択したウィジェットロゴにて表示される。Preview displays selected widget logo, widget logo is set

  @BDDTEST-GPT-342
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW07-02]チャットヘッダーの色を選択する Select Chat Header Color
    Given 「❻デザイン設定」画面が表示されている2Design Setting screen is displayed
    When チャットヘッダーの色を既存の色から選択する。Select chat header color from existing colors
    Then 表示サンプルのチャットヘッダーとウィジェットアイコンが選択した色にて表示される1。Preview displays selected chat color, chat color is set

  @BDDTEST-GPT-343
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW07-03]チャットヘッダーの色をカスタム設定する Create Custom Chat Header Color
    Given 「❻デザイン設定」画面が表示されている3 Design Setting screen is displayed
    When "カスタム"の横の入力欄に、6桁のHEXコードを入力する、またはカラーシートから選択するSelect input box next to custom and input 6 digit color HEX code, or select color box next to "Custom"and set
    Then 表示サンプルのチャットヘッダーとウィジェットアイコンが選択した色にて表示される2。Preview displays set chat color, chat color is set

  @BDDTEST-GPT-344
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW07-04]チャットアイコンを設定する Set Chat Icon Image Setting
    Given 「❻デザイン設定」画面が表示されている4Design Setting screen is displayed
    When 「アイコン設定」の「アイコンを変更」から画像をアップロードするSelect "Change Icon" and upload an image to be used
    Then 表示サンプルが選択したアイコンにて表示される1。Preview displays selected icon, icon is set

  @BDDTEST-GPT-907
  @ZFJ_Automation
  Scenario: [AW07-05]ウィジェットアイコンを設定する Set Widget Icon Image Setting
    Given 「❻デザイン設定」画面が表示されている5 ❻Design Setting screen is displayed
    When ウィジェットが閉じている時のアイコンの「アイコンを変更」をクリックし、画像データをアップロードするSelect ""Change Icon"" and upload an image to be used
    Then 表示サンプルが選択したアイコンにて表示される2。Preview displays selected widget icon, widget icon is set

  @BDDTEST-GPT-908
  @ZFJ_Automation
  Scenario: [AW07-06]ウィジェットアイコンのサイズを大きくする
    最大値：120

    Given 「❻デザイン設定」画面が表示されている6 Design Setting screen is displayed
    When アイコンサイズ(px)の＋を押下1 Press "+" of Icon size(px)
    Then 表示サンプルのウィジェットアイコンサイズが変わる1 Preview displays changed size, widget icon on Web page is set

  @BDDTEST-GPT-909
  @ZFJ_Automation
  Scenario: [AW07-07]ウィジェットアイコンのサイズを小さくする
    最小値：25

    Given 「❻デザイン設定」画面が表示されている7 Design Setting screen is displayed
    When アイコンサイズ(px)の "-" を押下2 Press "-" of Icon size(px)
    Then 表示サンプルのウィジェットアイコンサイズが変わる2 Preview displays changed size, widget icon on Web page is set

  @BDDTEST-GPT-910
  @ZFJ_Automation
  Scenario: [AW07-08]ウィジェットアイコンのフォントサイズを大きくする
    最大値：26

    Given 「❻デザイン設定」画面が表示されている8 Design Setting screen is displayed
    When フォントサイズ(px)の"＋"を押下1 Press "+" of Icon size(px)
    Then 表示サンプルのウィジェット上「チャットする」のフォントサイズが変わる1 Preview displays changed size, widget icon on Web page is set

  @BDDTEST-GPT-911
  @ZFJ_Automation
  Scenario: [AW07-09]ウィジェットアイコンのフォントサイズを小さくする
    最小値：10

    Given 「❻デザイン設定」画面が表示されている9 Design Setting screen is displayed
    When フォントサイズ(px)の "-" を押下2 Press "-" of Icon size(px)
    Then 表示サンプルのウィジェット上「チャットする」のフォントサイズが変わる2 Preview displays changed size, widget icon on Web page is set

  @BDDTEST-GPT-1237
  @ZFJ_Automation
  Scenario: [AW07-10]ウィジェットメッセージを変更する Change the Widget Message

    Given「❻デザイン設定」画面が表示されている10 ❻Design Setting screen is displayed
    Given ウィジェットメッセージ欄に「チャットする」と表示されている
    When ウィジェットメッセージ欄の文言を（テナント言語で）変更する　Change the text in the "Widget Message" input field in tenant language
    Then 変更値が表示サンプルに表示されている（未保存)　Changed text is displayed (not saved yet)

  @BDDTEST-GPT-1238
  @ZFJ_Automation
  Scenario: [AW07-11]ウィジェットメッセージの変更を保存する Save the change of Widget Message

    Given ウィジェットメッセージ欄に変更済みの文言が表示されている　Changed text is displayed in the "Widget Message" input field (not saved yet)
    When ウィジェットメッセージ入力欄横の"保存"を押下　Press "Save" next to the input field
    Then 表示サンプルのウィジェットメッセージが書き換わる　Preview displays the changed text