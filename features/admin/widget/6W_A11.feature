@BDDSTORY-GPT-770
Feature: 新規ウィジェットを作成する Create a new widget
  @BDDTEST-GPT-328
  @BDD_autmation
  Scenario: [A11-01]ウィジェット設定画面を開く Open the widget setting screen
    Given 基本設定の画面が表示されている The basic setting screen is displayed
    When 左のメニューバーから「ウィジェット設定」をクリックする Click "Widget Settings" from the left menu bar
    Then 現在登録されているウィジェット一覧が表示されるA list of currently registered widgets is displayed.
    And GPTと連携しているウィジェットのGPTステータスには✓が入っている

  @BDDTEST-GPT-329
  @BDD_autmation
  Scenario: [A11-02]新規ウィジェット作成画面に進む Go to the new widget creation screen
    Given 現在登録されているウィジェット一覧が表示されているA list of currently registered widgets is displayed.
    When 右上の追加ボタンをクリックするClick the add button in the upper right
    Then 「1担当グループ」から「8スニペット」までの登録面に遷移するTransition to the registration side from "1charge group" to "7 snippet"
