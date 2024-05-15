#!/bin/bash

# 指定のディレクトリに移動
cd /Users/kentamiyachi/PythonPro/laMondo/features/admin/widget/

# behave コマンドを実行
behave 6W_A01.feature 6W_A02.feature 6W_A03.feature --junit

DIRECTORY="/Users/kentamiyachi/PythonPro/laMondo/features/admin/widget/reports"

# テスト結果アップロードのパス
PYTHON_SCRIPT="/Users/kentamiyachi/PythonPro/laMondo/other/upload_execute.py"

while true; do
    # ディレクトリ内のファイル数をカウント
    FILE_COUNT=$(ls -1 "${DIRECTORY}" | wc -l)

    # ファイル数が3ならば指定のPythonスクリプトを実行
    if [ "${FILE_COUNT}" -eq 3 ]; then
        python "${PYTHON_SCRIPT}"
    fi

    # 5分間待機
    sleep 300
done