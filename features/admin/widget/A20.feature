@BDDSTORY-GPT-772
Feature: Edit Existing Widget
  @BDDTEST-GPT-330
  @BDD_autmation
  Scenario: [AW31-01]既存のウィジェットを編集する  Edit Existing Widget
    Given 現在登録されているウィジェット一覧が表示されているA list of currently registered widgets is displayed.
    When 編集したいウィジェット横の鉛筆マークをクリックするSelect pencil icon of the widget you wish to edit
    Then 「❶担当グループ」設定のページに遷移するTransition to the Widget setting page "❶ charge group"
