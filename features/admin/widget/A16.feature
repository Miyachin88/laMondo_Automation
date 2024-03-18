@BDDSTORY-GPT-791
Feature: Create New Widget Step ❹　ゲストによる評価設定
  @BDDTEST-GPT-335
  @BDD_autmation
  Scenario: [A15-01]メッセージ評価をONにする / Turn on Message Rating
    Given Tenant Admin Panel Guest Rating setting is displayed/ ゲストによる評価設定画面を開いている
    When Turn on "Message Rating"/ メッセージ評価を利用するのスイッチをONにする
    Then In Guest Screen, each message from GPT has clickable "thumbs up/down"/ ゲスト画面では、GPTからの返信毎にいいね！ボタンが表示される

  @BDDTEST-GPT-336
  @BDD_autmation
  Scenario: [A15-02]ゲストによる評価をONにする Turn "Guest Rating" option ON
    Given ❹ゲストによる評価画面で、「ゲストによる評価を利用する」トグルがオフになっている/❹Guest Rating screen is displayed with Guest rating automatically off
    When トグルをオンにする/Switch toggle to "ON"
    Then ゲスト評価のデザイン選択肢が表示される/The four candidates of the design are displayed on the admin panel

  @BDDTEST-GPT-337
  @BDD_autmation
  Scenario: [A15-03]「５アイコン」に設定する If ON, Set Guest Rating to "5 icons"
    ① （ゲスト画面では）５アイコンがカラーではなくなりました（SP69より）
    ② ”チャットとの会話はいかがでしたか？”　がアイコンの上部に表示される
    ③ ”とても不満” “普通“ “とても満足“　がアイコンの下の表示される
    ④評価アイコンを選択すると、そのアイコンのみカラーになる

    Clickable Icons: No color 5-scale emoticons
    Rating Question: “How satisfied are you with the conversation?“
    Rating Guidance: i.e. “Very Dissatisfied”, “Neutral“ , “Very Satisfied“
    Selected icon becomes colored

    Given ❹ゲストによる評価画面におり、トグルがオンになっている/Guest Rating is turned on 
    When 「５アイコン」を選択する/Select "5 Icon"
    Then 管理画面ではサンプルが表示され、ゲスト画面で会話終了後に５段階評価のアイコンが表示される/Guest rating survey is set to rate chat between 5 icons, display sample of "5 Icon" is automatically displayed

  @BDDTEST-GPT-338
  @BDD_autmation
  Scenario: [A15-04]「 星」に設定する If ON, Set Guest Rating to "Stars"
    Given ❹ゲストによる評価画面におり、トグルがオンになっている/Guest Rating is turned on
    When 「星」を選択する/Select "Emoji"
    Then 管理画面ではサンプルが表示され、ゲスト画面で会話終了後に星5段階評価のアイコンが表示されるGuest rating survey is set to rate chat between 5 icons, display sample of "Emoji" is automatically displayed

  @BDDTEST-GPT-339
  @BDD_autmation
  Scenario: [A16-01]初期メッセージを変更する / Change Chat Messages
    Given Tenant Admin Panel System Message Setting is displayed/ システムメッセージ設定画面を開いている
    When Change text in "Chat Messages (When beginning a new chat)" and Save/ 初期メッセージ設定欄のメッセージを変更し、保存を押下
    Then In Guest Screen, that text is shown after pressing "Start"/ ゲスト画面で、スタートボタン押下後に表示されるメッセージが変わる

  @BDDTEST-GPT-340
  @BDD_autmation
  Scenario: [A16-02]メッセージインプットプレースホルダーを変更する / Change Placeholder Message
    Given Tenant Admin Panel System Message Setting is displayed/ システムメッセージ設定画面を開いている
    When Change text in "Placeholder Message" and Save/ メッセージインプットプレースホルダー設定欄のメッセージを変更する
    Then In Guest Screen, that text is shown in the user input field before typing/ ゲスト画面で、メッセージ入力前のメッセージ入力欄の文言が変更になる
