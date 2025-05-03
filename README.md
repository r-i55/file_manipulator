# file_manipulator

Python製のコマンドラインツールで、テキストファイルの操作を行うことができます。

## ✨ 機能

- `reverse`: ファイルの内容を逆順にして出力ファイルに保存
- `copy`: ファイルの内容をコピー
- `duplicate-contents`: 指定回数、ファイルの内容を複製
- `replace-string`: 指定文字列を別の文字列に置き換え

## 🚀 使い方

```bash
# 使い方の例
python3 manipulator_practice.py reverse input.txt output.txt
python3 manipulator_practice.py copy input.txt output.txt
python3 manipulator_practice.py duplicate-contents input.txt 3
python3 manipulator_practice.py replace-string input.txt old new
