@BDDSTORY-GPT-774
Feature: AW02Create New Widget Step1
  @BDDTEST-GPT-332
  @BDD_autmation
  Scenario: AW02-01ウィジェット名称を設定する Set the widget name
    Given ウィジェット番号がデフォルトで設定されている Widget number is set by default
    When ウィジェット名横のペンシルボタンから名称を変更し、✓ボタンを押す Change the name from the pencil button next to the widget name and press the ✓ button.
    Then ウィジェット番号→指定した名前に変更されるWidget number → changed to the specified name. Name appears in chat header and initial messages.

  @BDDTEST-GPT-333
  @BDD_autmation
  Scenario: AW02-02]担当グループを割り当てる Assign a responsible group
    Given 担当グループ選択覧が空白である The group selection box is blank
    When 担当グループ選択覧の▼をクリックし、グループ名をクリックする Click ▼ in the group selection box, and click the group name.
    Then 担当グループが設定される The group in charge is set

  @BDDTEST-GPT-334
  @BDD_autmation
  Scenario: [AW02-03]担当グループの割り当てを外す Unassign a responsible group
    Given 担当グループが設定されている The group in charge is set
    When 担当グループ選択覧の✕をクリック Click ✕ in the group selection box
    Then 担当グループ選択覧が空欄になる The group selection box is blank