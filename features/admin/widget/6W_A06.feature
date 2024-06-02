@BDDSTORY-GPT-1056
Feature: Create New Widget Step ❺　システムメッセージ設定
  @BDDTEST-GPT-339
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW06-01]初期メッセージを変更する / Change Chat Messages
    Given Tenant Admin Panel System Message Setting is displayed1/ システムメッセージ設定画面を開いている
    When Change text in "Chat Messages (When beginning a new chat)" / 初期メッセージ設定欄のメッセージを（テナント言語で）変更
    Then Changed test is displayed1 (not saved yet)/ 変更値が表示されている（未保存）

  @BDDTEST-GPT-340
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW06-02]メッセージインプットプレースホルダーを変更する / Change Placeholder Message
    Given Tenant Admin Panel System Message Setting is displayed2/ システムメッセージ設定画面を開いている
    When Change text in "Placeholder Message2" / メッセージインプットプレースホルダー設定欄のメッセージを（テナント言語で）変更する
    Then Changed test is displayed (not saved yet)/ 変更値が表示されている（未保存）

  @BDDTEST-GPT-1235
  @ZFJ_Automation
  Scenario: [AW06-03]サンプル質問をONにする Turn ON the Sample Questions
    Given Tenant Admin Panel System Message Setting is displayed3/ システムメッセージ設定画面を開いている
    Given Sample Questions switch is OFF/ サンプル質問のツイッチがオフになっている
    When Turn on "Sample Questions"/ サンプル質問のスイッチをONにする
    Then Three input boxes for custom questions for guest screen will appear/ サンプル質問の入力欄が3つ表示される

  @BDDTEST-GPT-1236
  @ZFJ_Automation
  Scenario: [AW06-04]サンプル質問を追加する Add Sample Questions
    Given Three input boxes for custom questions for guest screen will appear/ サンプル質問の入力欄が3つ表示されている
    When Input one or two sample question(s) in tenant language/ サンプル質問を1つまたは2つ（テナント言語で）入力する
    Then "Save and Next" button becomes active/ "保存して次へ"ボタンがアクティブになっている

  @BDDTEST-GPT-1055
  @ZFJ_Automation
  Scenario: [AW06-05]システムメッセージ設定の保存
    システムメッセージ（初期メッセージ、メッセージインプットプレースホルダー、サンプル質問）は機械翻訳され、ゲスト端末の言語で表示される

    Given Tenant Admin Panel System Message Setting is displayed4/ システムメッセージ設定画面を開いている
    Given Texts are displayed in "Chat Messages (When beginning a new chat)", "Placeholder Message" field and "Sample Questions" field/ 初期メッセージ、メッセージインプットプレースホルダー、サンプル質問設定欄に文章が入力されている
    When Press "SAVE AND NEXT" / "保存して次へ"を押下
    Then Design Setting screen is displayed/ デザイン設定画面に遷移する
    Then On the guest screen, "Chat Messages (When beginning a new chat)" and "Placeholder Message" are changed/ ゲスト画面の初期メッセージとメッセージ入力欄のメッセージが変更されている
    Then System Messages of all widgets in this tenant are changed/ システムメッセージが変更されている＊同テナントのウィジェット全て
    Then Sample Questions are displayed/ サンプル質問が表示されている＊同テナントのウィジェット全て