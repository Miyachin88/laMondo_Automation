@BDDSTORY-GPT-831
Feature: エスカレーション機能の設定
  @BDDTEST-GPT-832
  Scenario: [AW 21-01]ウィジェット設定画面を開く


    Given 基本設定の画面が表示されている The basic setting screen is displayed
    When 左のメニューバーから「ウィジェット設定」をクリックする Click "Widget Settings" from the left menu bar
    Then 現在登録されているウィジェット一覧が表示されるA list of currently registered widgets is displayed.
    And エスカレーションスイッチが全てオフになっている

  @BDDTEST-GPT-833
  Scenario: [AW 21-02]エスカレーション機能をONにする


    Given エスカレーションスイッチが全てオフになっている
    When GPTステータスに✓が入っている任意のウィジェットのスイッチをオンにする
    Then スイッチがピンク色に切り替わり、"レコードは正常に編集されました。"と表示される
    And ゲスト画面のメッセージ入力欄にはエスカレーションボタンが表示される

  @BDDTEST-GPT-834
  Scenario: [AW 21-03]エスカレーション機能をOFFにする
    Given エスカレーションスイッチ（GPTステータスの右隣）がオンになっているウィジェットがある
    When スイッチをオフにする
    Then スイッチがグレーに切り替わり、"レコードは正常に編集されました。"と表示される
    And ゲスト画面のメッセージ入力欄からエスカレーションボタンが非表示になる
