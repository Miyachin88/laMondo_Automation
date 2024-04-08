@BDDSTORY-GPT-784
Feature: Create New Widget Step ❸　不在時のメール受信設定
  @BDDTEST-GPT-785
  Scenario: [A14-01]不在時のメール受信設定画面に移動する Move to Out of Business Hours Behavior Setting screen
    Given ❷営業時間の設定画面が表示されている / ❷The business hours setting screen is displayed.
    When 右下の「保存して次へ」をクリックする / Select "Next" at the bottom right hand corner
    Then 「❸不在時のメール受信設定」画面が表示される / ❸"Out of Business Hours Behaviour Setting" screen is displayed

  @BDDTEST-GPT-786
  Scenario: [A14-02]メール送信用フォームを営業時間外に表示設定する Set Email inquiries when staff are unavailable (Outside Business Hours)
    Given 「❸不在時のメール受信設定」画面が表示される / ❸"Out of Business Hours Behaviour Setting" screen is displayed
    When 「営業時間外」のチェックボックスをクリックする / Under "Email inquiries when staff are unavailable", select "Outside of Business Hours"
    Then 「不在時メール送信先」と「不在判定時間」の入力が可能になる / " "Unavailable Staff Mail Destination" and "Time Staff Did Not Respond" become active.

  @BDDTEST-GPT-787
  Scenario: [A14-03]不在時メール送信先を設定する Set  "Unavailable Staff Mail Destination"
    Given 「不在時メール送信先」と入力欄が表示されている / Input box is displayed under "Unavailable Staff Mail Destination"
    When 営業時間外もしくは不在時のチェックボックスにチェックを入れ、メールアドレス追加ボタン(赤い丸に白の十字)を押下
    Then 入力欄にメールアドレスを入れる / Input email address in the form abc@def.ghi

  @BDDTEST-GPT-788
  Scenario: [A14-04]不在時メール送信先を追加する Add  "Unavailable Staff Mail Destination"
    Given 「❸不在時のメール受信設定」画面が表示される / ❸"Out of Business Hours Behaviour Setting" screen is displayed
    When 不在時メール送信先の＋ボタンをクリックする / Under "Unavailable Staff Mail Destination", select ➕
    Then 入力欄が追加される / Input box is displayed under ""Unavailable Staff Mail Destination"

  @BDDTEST-GPT-789
  Scenario: [A14-05]不在時メール送信先を削除する Delete  "Unavailable Staff Mail Destination"
    Given 不在時メール送信先が設定されている / Unavilable staff mail destination email is set
    When 入力欄右横の×をクリックする / Select ❌ next to input box displayed under "Unavailable Staff Mail Destination"
    Then 該当の入力欄ごと消える / Unavilable staff mail destination email is deleted

  @BDDTEST-GPT-790
  Scenario: [A14-06]不在判定時間を設定する Set "Time Staff Did Not Respond"
    Given 「❸不在時のメール受信設定」画面が表示される / ❸"Out of Business Hours Behaviour Setting"screen is displayed
    When 不在時に✅を入れる / Check ✅ ”Staff Unavailable”
    And 不在判定時間に1-10までの数字を半角で入力する / Under "Time Staff Did Not Respond" input number between "1-10"
    Then ゲスト画面で設定した分数だけ経過後、メール送信用フォームが表示されるようになる / After "Set #" of minutes pass without staff response to guest, the email inquiry form is sent to guest
