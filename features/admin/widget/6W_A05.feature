@BDDSTORY-GPT-791
Feature: AW05Create New Widget Step ❹　ゲストによる評価設定
  @BDDTEST-GPT-335
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW05-01]メッセージ評価をONにする / Turn on Message Rating
    Given Tenant Admin Panel Guest Rating setting is displayed/ ゲストによる評価設定画面を開いている
    When Turn on "Message Rating"/ メッセージ評価を利用するのスイッチをONにする
    Then In Guest Screen, each message from GPT has clickable "thumbs up/down"/ ゲスト画面では、GPTからの返信毎にいいね！ボタンが表示される

  @BDDTEST-GPT-336
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW05-02]ゲストによる評価をONにする Turn "Guest Rating" option ON
    Given ❹ゲストによる評価画面で、「ゲストによる評価を利用する」トグルがオフになっている/❹Guest Rating screen is displayed with Guest rating automatically off
    When トグルをオンにする/Switch toggle to "ON"
    Then ゲスト評価のデザイン選択肢が表示される/The four candidates of the design are displayed on the admin panel

  @BDDTEST-GPT-337
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW05-03]「５アイコン」に設定する If ON, Set Guest Rating to "5 icons"
    Given ❹ゲストによる評価画面におり、トグルがオンになっている1/Guest Rating is turned on 
    When 「５アイコン」を選択する/Select "5 Icon"
    Then 管理画面ではサンプルが表示され、ゲスト画面で会話終了後に５段階評価のアイコンが表示される/Guest rating survey is set to rate chat between 5 icons, display sample of "5 Icon" is automatically displayed

  @BDDTEST-GPT-338
  @BDD_autmation
  @ZFJ_Automation
  Scenario: [AW05-04]「 星」に設定する If ON, Set Guest Rating to "Stars"
    Given ❹ゲストによる評価画面におり、トグルがオンになっている2/Guest Rating is turned on
    When 「星」を選択する/Select "Emoji"
    Then 管理画面ではサンプルが表示され、ゲスト画面で会話終了後に星5段階評価のアイコンが表示されるGuest rating survey is set to rate chat between 5 icons, display sample of "Emoji" is automatically displayed
