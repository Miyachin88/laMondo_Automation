@BDDSTORY-GPT-759
Feature: A02基本設定をする Set Basic Settings
  @BDDTEST-GPT-760
  Scenario: [A02-01]ウィジェットを表示する Show widget
    Given ゲスト画面にウィジェットが表示されていない / The widget is not displayed on the guest screen
    When 「すべてのウィジェットを有効にする。」のトグルをONにする / Turn on the toggle for "Enable all widgets."
    Then ゲスト画面で該当のウィジェットが表示されている / The corresponding widget is displayed on the guest screen
    Then ゲスト画面を開くと、通常フローでGPT・スタッフに問い合わせが送信できる

  @BDDTEST-GPT-761
  Scenario: [A02-02]ウィジェットを非表示にする Hide widget
    Given ゲスト画面にウィジェットが表示されている / The widget is displayed on the guest screen
    When 「すべてのウィジェットを有効にする。」のトグルをOFFにする / Turn off the toggle for "Enable all widgets."
    Then ゲスト画面で該当のウィジェットが表示されていない / The widget is not displayed on the guest screen
    Then ゲスト画面を開くと、「チャット機能は現在ご利用できません」が表示される

  @BDDTEST-GPT-762
  Scenario: [A02-03]ゲストによる回答評価の利用を有にする（Survey）Make use of guest response evaluation (Survey)
    Given "チャット終了後の「ゲスト評価」を利用する。"トグルがOFFになっている "Use the guest evaluation after the chat. " is OFF
    Given ステップ④ゲストによる評価の「ゲストによる評価を利用する」がOFFになっている
    When "チャット終了後の「ゲスト評価」を利用する。"のトグルをONにする Turn on the "Use the guest evaluation after the chat."
    Then ステップ④ゲストによる評価の「ゲストによる評価を利用する」がONになる

  @BDDTEST-GPT-763
  Scenario: [A02-04]ゲストによる回答評価の利用を無にする（Survey）Eliminate the use of guest response ratings (Survey)
    Given "チャット終了後の「ゲスト評価」を利用する。"トグルがONになっている""Use the" guest evaluation "after the chat. " is ON"
    When 「チャット終了後の「ゲスト評価」を利用する。」のトグルをOFFにする"Use the" guest evaluation "after the chat. Toggle off"
    Then ゲスト画面で、チャット終了後に回答評価が表示されなくなる On the guest screen, the answer rating is no longer displayed after the chat ends

  @BDDTEST-GPT-764
  Scenario: [A02-05]WorkCodeを追加する Add work code
    Given 基本設定画面のワークコードマスタに、現在登録されているワークコード一覧が表示されている / A list of work codes currently registered in the work code master is displayed.
    When 「＋」ボタンを押し、ワークコード名を入力して保存する / Press the "+" button, enter a name and save
    Then ワークコード一覧に数字→アルファベット→ひらがな→漢字の順に新たなワークコードが追加され、スタッフ画面にも同様に表示される / A new work code is added to the work code list in the order of numbers → alphabet → hiragana → kanji, and the same is displayed on the staff screen.

  @BDDTEST-GPT-765
  Scenario: [A02-06]WorkCodeを削除する Delete workcode
    Given ワークコードマスタに現在登録されているワークコード一覧が表示されている / A list of work codes currently registered in the work code master is displayed.
    When 削除したいワークコードに✅をし、ごみ箱ボタンをクリックする  /✅  on the work code you want to delete and click the Recycle Bin button
    Then ワークコード一覧から削除され、スタッフ画面にも反映されている / It has been deleted from the work code list and reflected on the staff screen.

  @BDDTEST-GPT-766
  Scenario: [A02-07]WorkCodeを編集する Edit workcode
    Given ワークコードマスタに現在登録されているワークコード一覧が表示されている / A list of work codes currently registered in the work code master is displayed.
    When 編集したいワークコードのペンシルマークをクリックし、名前を編集する / Click the pencil mark of the work code you want to edit, and edit name
    Then どこかをクリックすると保存され、スタッフ画面にも反映されている / Click anywhere to save it and reflect it on the staff screen
