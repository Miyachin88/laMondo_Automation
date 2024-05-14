@BDDSTORY-GPT-775
Feature: AW03 Create New Widget Step ❷
  @BDDTEST-GPT-776
  Scenario: [AW03-01]チャットの営業可能時間を設定する（毎日） Set chat business hours (Daily)
    Given ❷営業時間の設定画面が表示されている / ❷The business hours setting screen is displayed.
    When タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
    And タイトル欄に任意のタイトルを入力 / Set title
    And 対象のプルダウンから"毎日"を選択 / Select "daily" as Subject
    And 開始/終了時間を設定 / Set start / end time
    And "保存"を押下 / Press "SAVE"
    Then このウィジェットから受付時間外にお問い合わせを送ると、受付可能時間メッセージ、またはメール送信用フォームが表示される（設定による） / If you send an inquiry from this widget outside the reception hours, out-of-business-hour message or the email sending form will be displayed.

  @BDDTEST-GPT-777
  Scenario: [AW03-02]チャットの営業可能時間を設定する（曜日） Set chat business hours (day of the week)
    Given ❷営業時間の設定画面が表示されている / ❷The business hours setting screen is displayed.
    When タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
    And タイトル欄に任意のタイトルを入力 / Set title
    And 対象のプルダウンから"曜日（優先度中）"を選択 / Select "Specify Day of the Week" as Subject
    And 曜日のプルダウンから任意の曜日を選択 / Select any day as Day of the Week 
    And 開始/終了時間を設定 / Set start / end time
    And "保存"を押下 / Press "SAVE"
    Then このウィジェットから受付時間外にお問い合わせを送ると、受付可能時間メッセージ、またはメール送信用フォームが表示される（設定による） / If you send an inquiry from this widget outside the reception hours, out-of-business-hour message or the email sending form will be displayed.

  @BDDTEST-GPT-778
  Scenario: [AW03-03]チャットの営業可能時間を設定する（特定の日のみ）Set chat business hours (only on specific days)
    Given ❷営業時間の設定画面が表示されている / ❷The business hours setting screen is displayed.
    When タイプのプルダウンから"受付時間"を選択 / Select "Business Hours" as Type
    And タイトル欄に任意のタイトルを入力 / Set title
    And 対象のプルダウンから"日を指定（優先度高）"を選択 / Select "Specify Date" as Subject
    And 曜日のプルダウンから任意の日を選択 / Select any date as Date 
    And 開始/終了時間を設定 / Set start / end time
    And "保存"を押下 / Press "SAVE"
    Then このウィジェットから受付時間外にお問い合わせを送ると、受付可能時間メッセージ、またはメール送信用フォームが表示される（設定による） / If you send an inquiry from this widget outside the reception hours, out-of-business-hour message or the email sending form will be displayed.

  @BDDTEST-GPT-779
  Scenario: [AW03-04]チャットの対応不可時間を設定する（毎日）Set chat unavailable hours (Daily)
    Given ❷営業時間の設定画面が表示されている / ❷The business hours setting screen is displayed.
    When タイプのプルダウンから"受付不可時間"を選択 / Select "Out of Business Hours" as Type
    And タイトル欄に任意のタイトルを入力 / Set title
    And 対象のプルダウンから"毎日"を選択 / Select "daily" as Subject
    And 開始/終了時間を設定 / Set start / end time
    And "保存"を押下 / Press "SAVE"
    Then このウィジェットから受付時間外にお問い合わせを送ると、受付可能時間メッセージ、またはメール送信用フォームが表示される（設定による） / If you send an inquiry from this widget outside the reception hours, out-of-business-hour message or the email sending form will be displayed.

  @BDDTEST-GPT-780
  Scenario: [AW03-05]チャットの対応不可時間を設定する（曜日）Set chat unavailable hours (day of the week)
    Given ❷営業時間の設定画面が表示されている / ❷The business hours setting screen is displayed.
    When タイプのプルダウンから"受付不可時間"を選択 / Select "Out of Business Hours" as Type
    And タイトル欄に任意のタイトルを入力 / Set title
    And 対象のプルダウンから"曜日（優先度中）"を選択 / Select "Specify Day of the Week" as Subject
    And 曜日のプルダウンから任意の曜日を選択 / Select any day as Day of the Week 
    And 開始/終了時間を設定 / Set start / end time
    And "保存"を押下 / Press "SAVE"
    Then このウィジェットから受付時間外にお問い合わせを送ると、受付可能時間メッセージ、またはメール送信用フォームが表示される（設定による） / If you send an inquiry from this widget outside the reception hours, out-of-business-hour message or the email sending form will be displayed.

  @BDDTEST-GPT-781
  Scenario: [AW03-06]チャットの対応不可時間を設定する（特定の日のみ）Set chat unavailable hours (only on specific days)
    Given ❷営業時間の設定画面が表示されている / ❷The business hours setting screen is displayed.
    When タイプのプルダウンから"受付不可時間"を選択 / Select "Out of Business Hours" as Type
    And タイトル欄に任意のタイトルを入力 / Set title
    And 対象のプルダウンから"日を指定（優先度高）"を選択 / Select "Specify Date" as Subject
    And 曜日のプルダウンから任意の日を選択 / Select any date as Date 
    And 開始/終了時間を設定 / Set start / end time
    And "保存"を押下 / Press "SAVE"
    Then このウィジェットから受付時間外にお問い合わせを送ると、受付可能時間メッセージ、またはメール送信用フォームが表示される（設定による） / If you send an inquiry from this widget outside the reception hours, out-of-business-hour message or the email sending form will be displayed.

  @BDDTEST-GPT-782
  Scenario: [AW03-07]営業不可時間を複数設定する Set multiple Out of Business Hours
    Given ❷営業時間の設定画面が表示されている / ❷The business hours setting screen is displayed.
    And 設定タイプが"営業不可時間"になっている / "Out of Business Hours" is set in Business Hours setting type
    When 「曜日」と「特定の日」を設定する(優先度：高) / Set "Specific Day of the Week" and "Specific Date"(High)
    And 特定日について、受付時間内に設定する 例）4/10(月) 11:00にアクセスする場合は4/10の10:00 - 20:00
    And 「曜日」と「特定の日」を設定する(優先度：中) / Set "Specific Day of the Week" and "Specific Date"(Middle)
    And 曜日について、受付時間内に設定する 例）4/10(月) 11:00にアクセスする場合は火〜日の10:00 - 20:00
    Then このウィジェットから受付時間外にお問い合わせを送ると、受付時間外メッセージが表示される(添付画像参照) / If you send an inquiry from this widget outside the reception hours, the Out-of-business-hour message will be displayed.

  @BDDTEST-GPT-783
  Scenario: [AW03-08]営業可能時間を複数設定する
    Given ❷営業時間の設定画面が表示されている / ❷The business hours setting screen is displayed.
    When 営業可能時間を1日の中で複数設定する。営業可能時間を設定 例）4/10(月) 13:00にアクセスする場合は毎日の10:00 - 13:00
    And 営業可能時間を1日の中で複数設定する。営業外時間を設定 例）4/10(月) 13:00にアクセスする場合はの毎日の14:00 - 20:00
    Then このウィジェットから受付時間外にお問い合わせを送ると、受付時間外メッセージが表示される / If you send an inquiry from this widget outside the reception hours, the Out-of-business-hour message will be displayed.
