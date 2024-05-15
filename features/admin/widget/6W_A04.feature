@BDDSTORY-GPT-784
Feature: Create New Widget Step ❸　不在時のメール受信設定
  @BDDTEST-GPT-785
  @ZFJ_Automation
  Scenario: [AW04-01]不在時のメール受信設定画面に移動する Move to Out of Business Hours Behavior Setting screen
    Given 営業時間の設定画面が表示されている
    When 右下の「保存して次へ」をクリックする
    Then 「不在時のメール受信設定」画面が表示される

  @BDDTEST-GPT-786
  @ZFJ_Automation
  Scenario: [AW04-02]メール送信用フォームを営業時間外に表示設定する Set Email inquiries when staff are unavailable (Outside Business Hours)
    Given 「不在時のメール受信設定」画面が表示されている1
    When 「営業時間外」のチェックボックスに✓を入れる
    Then 「不在時メール送信先」と「不在判定時間」の入力が可能になる

  @BDDTEST-GPT-787
  @ZFJ_Automation
  Scenario: [AW04-03]不在時メール送信先を設定する Set  "Unavailable Staff Mail Destination"
    Given 「不在時メール送信先」入力欄が表示されている
    When 入力欄にメールアドレスを入れる
    When 不在判定時間に1-10までの数字を半角で入力する1
    Then 入力値が表示されている（未保存）

  @BDDTEST-GPT-788
  @ZFJ_Automation
  Scenario: [AW04-04]不在時メール送信先を追加する Add  "Unavailable Staff Mail Destination"
    Given 「不在時のメール受信設定」画面が表示されている2
    When 不在時メール送信先の＋ボタンをクリックする
    Then 入力欄が追加される

  @BDDTEST-GPT-789
  @ZFJ_Automation
  Scenario: [AW04-05]不在時メール送信先を削除する Delete  "Unavailable Staff Mail Destination"
    Given 不在時メール送信先が設定されている
    When 入力欄右横の×をクリックする
    Then 該当の入力欄ごと消える

  @BDDTEST-GPT-790
  @ZFJ_Automation
  Scenario: [AW04-06]不在判定時間を設定する Set "Time Staff Did Not Respond"
    Given 「不在時のメール受信設定」画面が表示される
    When 不在時のチェックボックスにチェックを入れる
    When 不在判定時間に1-10までの数字を半角で入力する2
    Then ゲスト画面でスタッフ呼び出し後、設定した分数が経過すると、メール送信用フォームが表示される
