# "/home/user/python_practice/test.txt" のように、絶対パスも使用できます 

file = open('test.txt')
print(file.read())
file.close()# ← 終わったら忘れずに閉じる！