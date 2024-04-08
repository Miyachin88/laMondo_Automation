@BDDSTORY-GPT-792
Feature: Create New Widget Step ❻　デザイン設定
  @BDDTEST-GPT-341
  @BDD_autmation
  Scenario: [A17-01]ウィジェットロゴを設定する Set Widget Logo
    Given 「❻デザイン設定」画面が表示されている ❻Design Setting screen is displayed
    When ウィジェットロゴの「ロゴを変更」をクリックし、画像データをアップロードするSelect "Change Logo" and upload an image to be used
    Then 表示サンプルが選択したウィジェットロゴにて表示される。Preview displays selected widget logo, widget logo is set

  @BDDTEST-GPT-342
  @BDD_autmation
  Scenario: [A17-02]チャットヘッダーの色を選択する Select Chat Header Color
    Given 「❻デザイン設定」画面が表示されているDesign Setting screen is displayed
    When チャットヘッダーの色を既存の色から選択する。Select chat header color from existing colors
    Then 表示サンプルが選択した色にて表示される。Preview displays selected chat color, chat color is set

  @BDDTEST-GPT-343
  @BDD_autmation
  Scenario: [A17-03]チャットヘッダーの色をカスタム設定する Create Custom Chat Header Color
    Given 「❻デザイン設定」画面が表示されている Design Setting screen is displayed
    When "カスタム"の横の入力欄に、6桁のHEXコードを入力する、またはカラーシートから選択するSelect input box next to custom and input 6 digit color HEX code, or select color box next to "Custom"and set
    Then 表示サンプルが選択した色にて表示される。Preview displays set chat color, chat color is set

  @BDDTEST-GPT-344
  @BDD_autmation
  Scenario: [A17-04]チャットアイコンを設定する Set Chat Icon Image Setting
    Given 「❻デザイン設定」画面が表示されているDesign Setting screen is displayed
    When 「アイコン設定」の「アイコンを変更」から画像をアップロードするSelect "Change Icon" and upload an image to be used
    Then 表示サンプルが選択したアイコンにて表示される。Preview displays selected icon, icon is set

  @BDDTEST-GPT-907
  Scenario: [AW07-05]ウィジェットアイコンを設定する Set Widget Icon Image Setting
    Given 「❻デザイン設定」画面が表示されている ❻Design Setting screen is displayed
    When ウィジェットが閉じている時のアイコンの「アイコンを変更」をクリックし、画像データをアップロードするSelect ""Change Icon"" and upload an image to be used
    Then 表示サンプルが選択したアイコンにて表示される。Preview displays selected widget icon, widget icon is set

  @BDDTEST-GPT-908
  Scenario: [AW07-06]ウィジェットアイコンのサイズを大きくする
    Given 「❻デザイン設定」画面が表示されている Design Setting screen is displayed
    When アイコンサイズ(px)の＋を押下 Press "+" of Icon size(px)
    Then 表示サンプルのウィジェットアイコンサイズが変わる Preview displays changed size, widget icon on Web page is set

  @BDDTEST-GPT-909
  Scenario: [AW07-07]ウィジェットアイコンのサイズを小さくする
    Given 「❻デザイン設定」画面が表示されている Design Setting screen is displayed
    When アイコンサイズ(px)の "-" を押下 Press "-" of Icon size(px)
    Then 表示サンプルのウィジェットアイコンサイズが変わる Preview displays changed size, widget icon on Web page is set

  @BDDTEST-GPT-910
  Scenario: [AW07-08]ウィジェットアイコンのフォントサイズを大きくする
    Given 「❻デザイン設定」画面が表示されている Design Setting screen is displayed
    When フォントサイズ(px)の"＋"を押下 Press "+" of Icon size(px)
    Then 表示サンプルのウィジェット上「チャットする」のフォントサイズが変わる Preview displays changed size, widget icon on Web page is set

  @BDDTEST-GPT-911
  Scenario: [AW07-09]ウィジェットアイコンのフォントサイズを小さくする
    Given 「❻デザイン設定」画面が表示されている Design Setting screen is displayed
    When フォントサイズ(px)の "-" を押下 Press "-" of Icon size(px)
    Then 表示サンプルのウィジェット上「チャットする」のフォントサイズが変わる Preview displays changed size, widget icon on Web page is set
