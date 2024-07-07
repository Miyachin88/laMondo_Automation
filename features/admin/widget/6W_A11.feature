@BDDSTORY-GPT-794
Feature: Cancel Widget Creation　新規ウィジェット作成をキャンセルする
  @BDDTEST-GPT-346
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW11-01]ウィジェット設定をキャンセルする Cancel Widget Creation
    Given 「❻デザイン設定」画面が表示されている❻Design Setting screen is displayed
    When 右下の 「キャンセル 」（初回のみ）を選択するIn the lower right hand corner, select "Cancel" ＊ウィジェットを新規作成時（初回設定時）のみ出る
    Then ウィジェットの新規作成処理がキャンセルされ、データが保存されないCreate new widget process is cancelled, no data is saved