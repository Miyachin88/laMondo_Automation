@BDDSTORY-BBS-27
Feature: BBS Admin 16.管理画面の言語変更
  @BDDTEST-BBS-65
  Scenario: [BBS A16-01]管理画面の言語変更（英語） Change admin panel language to English
    Given You are viewing any community
    When Select English from the language change button on the upper right
    Then The admin panel including the community names and post are displayed in English