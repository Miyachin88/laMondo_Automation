@BDDSTORY-GPT-377
Feature: [A20] バリエーション設定
  @BDDTEST-GPT-717
  @ZFJ_Automation
  Scenario: [AW22-01]バリエーション設定画面を開く
    Given ウィジェット設定が開かれていて、登録済みのウィジェットがある
    When ウィジェット右側のロケーションアイコンを押下
    Then バリエーション設定画面が表示される

  @BDDTEST-GPT-718
  @ZFJ_Automation
  Scenario: [AW22-02]バリエーション追加ボタンを押す
    Given バリエーション設定画面が表示されている
    When 右上のバリエーション追加ボタンを押下
    Then バリエーションを追加するポップアップが表示される

  @BDDTEST-GPT-719
  @ZFJ_Automation
  Scenario: [AW22-03] バリエーションの名前を入力する
    Given バリエーションを追加するポップアップが表示されていて名前欄が入力されていない
    When 名前にValiation Name Aを入力する(例 Chanel)
    Then 名前欄にValiation Name Aが入力できる

  @BDDTEST-GPT-720
  @ZFJ_Automation
  Scenario: [AW22-04] バリエーションを入力する
    Given バリエーションを追加するポップアップが表示されている
    When バリエーション欄にValiation Aを入力する(説明欄を参照)
    Then バリエーション欄にValiation Aが入力できる

  @BDDTEST-GPT-721
  @ZFJ_Automation
  Scenario: [AW22-05] バリエーションを保存する
    Given バリエーションを追加するの名前欄とバリエーション欄が入力されている
    When 右下の"保存"ボタンを押下
    Then バリエーション設定画面に、名前、バリエーション、スニペット、ゲスト画面URL、QRコードが生成され、追加される　＊画像参照

  @BDDTEST-GPT-722
  @ZFJ_Automation
  Scenario: [AW22-11] スニペットのコピー＆ペースト
    Given バリエーション設定のスニペットの項目にスニペットとコピーボタンが表示されている(Snippet A)
    When Snippet Aの右のコピーボタンを押下し、テスト用サイトにペースト
    Then Snippet Aがペーストできる

  @BDDTEST-GPT-723
  @ZFJ_Automation
  Scenario: [AW22-12] スニペットのウィジェットの実行
    Given テスト用サイトにSnippet Aがペーストされていて、ウィジェットが表示されている
    When ウィジェットを押下し、スタートを押下
    Then laMondoを実行できる

  @BDDTEST-GPT-724
  @ZFJ_Automation
  Scenario: [AW22-13] ゲスト画面URLを別タブで開く
    Given バリエーション設定のスニペットの項目にゲスト画面URLと、コピーボタン、別タブで開くボタンが表示されている
    When 別タブで開くボタンを押下
    Then ゲスト画面が開き、laMondoスタート画面が表示される

  @BDDTEST-GPT-725
  @ZFJ_Automation
  Scenario: [AW22-14] 二次元バーコードのコピー＆ペースト
    Given バリエーション設定のスニペットの項目に二次元バーコードが表示されている(2D-code A)
    When 二次元バーコードをクリックしてリンクをコピーし、別タブを開いてペースト
    Then 二次元バーコードが表示される

  @BDDTEST-GPT-726
  @ZFJ_Automation
  Scenario: [AW22-15] 二次元バーコードの読み取り
    Given 二次元バーコードが表示されている
    When スマートフォンで読み取り実行
    Then laMondoのスタート画面が表示される

  @BDDTEST-GPT-727
  @ZFJ_Automation
  Scenario: [AW22-21] バリエーションの編集画面を表示する
    Given バリエーション設定のバリエーション(Vali-A)の右端に鉛筆ボタンが表示されている
    When 鉛筆ボタンを押下
    Then バリエーションを編集するポップアップが表示され、Vali-Aの情報が表示される

  @BDDTEST-GPT-728
  @ZFJ_Automation
  Scenario: [AW22-22] バリエーションを編集する
    Given バリエーションを編集するポップアップが表示され、Vali-Aの情報が表示されている
    When 名前欄、バリエーション欄を編集し、保存を押下
    Then バリエーション設定画面に戻り、Vali-Aの名前、バリエーションが変更されている

  @BDDTEST-GPT-729
  @ZFJ_Automation
  Scenario: [AW22-23] バリエーションの削除確認を表示する
    Given バリエーション設定のバリエーション(Vali-A)の右端にゴミ箱ボタンが表示されている　＊デフォルトのバリエーションは削除ボタンが押せなくなっている
    When ゴミ箱ボタンを押下
    Then 削除確認のポップアップが表示される

  @BDDTEST-GPT-730
  @ZFJ_Automation
  Scenario: [AW22-24] バリエーションの削除の実行
    Given 削除確認のポップアップが表示されている
    When 削除ボタンを押下
    Then Vali-Aがバリエーション設定画面から非表示になる
