@BDDSTORY-GPT-793
Feature: Save Widget
  @BDDTEST-GPT-345
  @BDD_autmation
  Scenario: [AW08-01]ウィジェット設定を保存する Save Widget Settings
    Given ❻デザイン設定」画面が表示されている ❻Design Setting screen is displayed
    When 右下の「保存」を選択するIn the lower right hand corner, select "SAVE"＊ウィジェットを新規作成時（初回設定時）のみ出る
    Then 画面がステップ❼に遷移し、画面上部に「成功」メッセージが表示される Screen moves to ❼Snippet and success message displayed at top of screen
    And 右下に（編集済みの）ウィジェットアイコンが表示される Modified Widget Icon is displayed on the bottom right
