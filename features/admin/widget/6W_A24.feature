@BDDSTORY-GPT-773
Feature: Display Widget Information
  @BDDTEST-GPT-331
  @BDD_autmation
  Scenario: [AW23-01]ウィジェットの情報を表示する Display Widget Information
    Given 現在登録されているウィジェット一覧が表示されている A list of currently registered widgets is displayed.
    When ウィジェット名横のインフォメーションマークをクリックする Select info icon of the widget you wish to see
    Then 該当ウィジェットのスニペットコード、URL、二次元バーコード、動作確認ボタンがポップアップ表示されるPop-up displays snippet code, guest chat URL, 2D barcode for guest chat, and operation check button
