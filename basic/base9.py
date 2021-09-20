# # リスト
# list_a = [1, 2, 3, 4]
# list_b = []

# print(list_a)
# print(list_a[-2])

# list_a = [1, [1, 2, 'apple'], 3, 'banana']

# print(list_a[1][2])
# print(list_a)
# list_a[1][2] = "lemon"
# print(list_a)

# # リストのメソッド

# list_a = [1, 2, 3, 4, 5]

# list_b = list_a[1:4:2] # 一つ飛ばし
# print(list_b)

# # append, extend, insert, clear

# list_a.append('apple')
# print(list_a)
# list_a.extend(['banana', 'melon'])
# print(list_a)
# list_a.insert(1, "grape")
# print(list_a)
# list_a.clear()
# print(list_a)

# remove, pop, count, index
list_a = [0, 1, 1, 2, 2, 3, 3, 3, 4]
list_a.remove(3)  # 最初に出てきた3を削除
print(list_a)
value = list_a.pop()  # 一番最後に取り出された値を取り出している
print(list_a, value)
print(list_a.count(1))  # 要素のカウント
print(list_a.index(2))  # 一番最初に出てきた2のインデックス

# copy

print(list_a)
list_b = list_a.copy()  # list_aの中身の書き換えを防ぐ
list_b[0] = "AAAAA"
print(list_a)

# sort reverse
list_a = ["banana", "apple", "lemon", "grape"]
print(list_a)
list_a.sort()
print(list_a)

# sort reverse
list_a = ["banana", "apple", "lemon", "grape"]

print(list_a)

# list_a.sort() # 昇順に並び替え
list_a = sorted(list_a)  # 組み込み関数ver
list_a.reverse()
print(list_a)
