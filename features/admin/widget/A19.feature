@BDDSTORY-GPT-796
Feature: Create New Widget Step ❼　スニペット確認
  @BDDTEST-GPT-348
  @BDD_autmation
  Scenario: [AW09-01]作成したスニペットコードをコピーする Copy Created Snippet
    Given 「❼スニペット」画面が表示されている❼Snippet screen screen is displayed
    When スニペットコード横のコピーアイコンをクリックするSelect copy button in corner of snippet box
    Then クリップボードにスニペットコードがコピーされるSnippet code is copied to clipboard

  @BDDTEST-GPT-349
  @BDD_autmation
  Scenario: [AW09-02]作成したスニペットコードを使う Test Created Widget Snippet
    Given 「❼スニペット」画面にて、スニペットコードがクリップボードにコピーされているSnippet screen is displayed and snippet code is copied
    When テスト用のウェブサイトにスニペットコードを貼り付けるPaste snippet code into test website
    Then テスト用ウェブサイトにウィジェットが表示されるWidget will appear in bottom right hand corner of website with proper settings

  @BDDTEST-GPT-350
  @BDD_autmation
  Scenario: [AW09-03]作成したURLを使う Test Created Widget Link
    Given「❼スニペット」画面が表示されているSnippet screen screen is displayed

    Given 「❼スニペット」画面が表示されているSnippet screen screen is displayed
    When URLをクリックするSelect link, select copy button, or select "open in a new tab" icon
    Then ウィジェットの中身のみが別タブで表示されるWidget chat opens (depending on method)

  @BDDTEST-GPT-351
  @BDD_autmation
  Scenario: [AW09-04]作成したQRコードを使う Test 2D barcode


  @BDDTEST-GPT-352
  @BDD_autmation
  Scenario: [AW09-05]作成したQRコードをダウンロードする Download 2D barcode
    Given 「❼スニペット」画面が表示されている Snippet screen screen is displayed
    When QRコード下のダウンロードボタンを押す Select "Download" button
    Then PNGでPCにQRコードデータがダウンロードされる New tab is opened displaying .png format of 2D Barcode

  @BDDTEST-GPT-353
  @BDD_autmation
  Scenario: [AW09-06]動作確認ページを開く Test Live Chat Guest Page
    Given 「❼スニペット」画面が表示される Snippet screen screen is displayed
    When 「動作確認ページを開く」を選択 Select "Open Operation Check Page"
    Then 別タブが起動し、チャット画面が表示される Automatically moved to a new tab and widget chat opens
