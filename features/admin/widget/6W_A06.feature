@BDDSTORY-GPT-1056　
@BDDSTORY-GPT-522
@ZFJ_Automation
Feature: Create New Widget Step ❺　システムメッセージ設定
  @BDDTEST-GPT-1373
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW06-01]初期メッセージを変更する / Change Chat Messages
    Given Tenant Admin Panel System Message Setting is displayed1/ システムメッセージ設定画面を開いている
    When Change text in "Chat Messages (When beginning a new chat)" / 初期メッセージ設定欄のメッセージを（テナント言語で）変更
    Then Changed test is displayed1 (not saved yet)/ 変更値が表示されている（未保存）

  @BDDTEST-GPT-1374
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW06-02]メッセージインプットプレースホルダーを変更する / Change Placeholder Message
    Given Tenant Admin Panel System Message Setting is displayed2/ システムメッセージ設定画面を開いている
    When Change text in "Placeholder Message2" / メッセージインプットプレースホルダー設定欄のメッセージを（テナント言語で）変更する
    Then Changed test is displayed (not saved yet)/ 変更値が表示されている（未保存）

  @BDDTEST-GPT-1375
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW06-03]サンプル質問をONにする Turn ON the Sample Questions
    Given Tenant Admin Panel System Message Setting is displayed3/ システムメッセージ設定画面を開いている
    Given Sample Questions switch is OFF/ サンプル質問のツイッチがオフになっている
    When Turn on "Sample Questions"/ サンプル質問のスイッチをONにする
    Then One input box and "+" button will appear/ サンプル質問の入力欄1つと"+"ボタンが表示される

  @BDDTEST-GPT-1376
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW06-04]サンプル質問を登録する Input Sample Questions
    Given One input box for custom questions for guest screen will appear/ サンプル質問の入力欄が1つ表示されている
    When Input sample question in tenant language/ サンプル質問を（テナント言語で）入力する
    Then "Save and Next" button becomes active/ "保存して次へ"ボタンがアクティブになっている

  @BDDTEST-GPT-1377
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW06-05]サンプル質問を追加する Add Sample Questions最大10個まで設定可能（＝11個以上は設定不可）
    Given Some sample questions are displayed1/ サンプル質問が入力されている
    When Press "+" to add an input field/ "+"を押下する
    Then Sample question input field is added up to 10 "+" button becomes gray out/ サンプル質問入力欄が10個まで追加でき、"+"ボタンはグレーアウトする

  @BDDTEST-GPT-1378
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW06-06]追加したサンプル質問を入力する Input Sample Questions in added Sample Questions
    Given Added sample question input fields are displayed and blank/ サンプル質問欄が追加され空欄である
    When Input sample question(s) in that input fields/ サンプル質問追加欄に質問を入力する
    Then Added sample questions are displayed (not saved yet)/ 追加されたサンプル質問が表示されている
    Then "Save and Next" button becomes active2/ "保存して次へ"ボタンがアクティブになっている

  @BDDTEST-GPT-1379
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW06-07]サンプル質問表示中もメッセージ入力欄を表示する
    Given Toggle of Display message input field when displaying sample questions is "OFF"  / ウィジェット設定にてサンプル質問表示中もメッセージ入力欄を表示するのトグルがOFF
    When Change toggle of Display message input field when displaying sample questions is "ON"/ サンプル質問表示中もメッセージ入力欄を表示するのトグルをONにする
    Then Sample message and message input box are displayed if you open guest screen / ゲスト画面を開くとサンプルメッセージおよびメッセージのテキストボックスが表示されている

  @BDDTEST-GPT-1380
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW06-08]サンプル質問表示中もメッセージ入力欄を表示しない
    Given Toggle of Display message input field when displaying sample questions is "ON"  / ウィジェット設定にてサンプル質問表示中もメッセージ入力欄を表示するのトグルが"ON"
    When Change toggle of Display message input field when displaying sample questions is "OFF"/ サンプル質問表示中もメッセージ入力欄を表示するのトグルを"OFF"にする
    Then Message input box is NOT displayed if you open guest screen / ゲスト画面を開くとメッセージのテキストボックスが表示されない

  @BDDTEST-GPT-1381
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW06-09]システムメッセージ設定の保存
    Given Tenant Admin Panel System Message Setting is displayed/ システムメッセージ設定画面を開いている
    Given Texts are displayed in "Chat Messages (When beginning a new chat)", "Placeholder Message" field and "Sample Questions" field/ 初期メッセージ、メッセージインプットプレースホルダー、サンプル質問設定欄に文章が入力されている
    When Press "SAVE AND NEXT" / "保存して次へ"を押下
    Then Design Setting screen is displayed/ デザイン設定画面に遷移する
    Then System Messages of all widgets in this tenant are changed/ 管理画面上でシステムメッセージが変更されている＊同テナント全てのウィジェット
    Then Sample Questions are displayed/ 管理画面上でサンプル質問が表示されている＊該当ウィジェットのみ
    Then On the guest screen, "Chat Messages (When beginning a new chat)" and "Placeholder Message" are changed/ ゲスト画面で初期メッセージとメッセージ入力欄のメッセージが変更されている
    Then On the guest screen,  "Chat Messages (When beginning a new chat)" and "Placeholder Message" are translated in the guest device language/ ゲスト画面で初期メッセージとメッセージ入力欄のメッセージが端末言語に機械翻訳されている
