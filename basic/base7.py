# 文字列型

fruit = 'apple'
print(fruit)

print(type(fruit))

print(fruit*10)
print(fruit * 10)

new_fruit = fruit + " banana"
print(new_fruit)

fruits = """
banana
grape
"""

print(fruits)

fruit = "banana"
print(fruit[2])
print(fruit[-1])  # 後ろから表示

# encode, decode => bytes[]
# encode データをほかの形式へ変換
# decode エンコードされたデータを元に戻す
# ????ここまじわからん????
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))

# count

msg = "ABCDEABC"
print(msg.count("ABCDEF"))  # 存在しない => 0


# statswith endswith
print(msg.startswith('ABCD'))
print(msg.endswith('C'))

# strip 両端, rstrip 右端, lstrip 両端 を削除
msg = ' ABC'
print(msg)
print(msg.strip())
msg = "ABCDEFABC"
print(msg.strip('CBA'))  # 該当するものを順次削除
print(msg.lstrip('CBA'))
print(msg.rstrip('CBA'))

# upper, lower, swapcase, replace, capitalize

msg = "abcABC"
msg_u = msg.upper()  # 大文字
msg_l = msg.lower()  # 小文字
msg_s = msg.swapcase()  # 大文字込み時入れ替え 日本語は変わらない
print(msg_u, msg_l, msg_s)

# replace
msg = "ABCDEABC"
msg_r = msg.replace('ABC', "FFF", -1)  # 第三引数のデフォルトの値は-1 1にすると一つ目のABCがFFFに入れ替わる
print(msg_r)

msg = "hello woRld"  # 一番最初だけ大文字
print(msg.capitalize())
