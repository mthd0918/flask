
# 8 定数について

# 定数はプログラム上で一度設定すれば変えることのできない値に設定(お約束)

# 予約語、あらかじめ決められている言葉

# 特殊なprint文
# print(f'{val}')
# print(f'{val=}')

# 変数の応用

animal = 'dog'
動物 = 'cat'
print(動物)

# 定数

age = 18
LEGAL_AGE = 20

if age < LEGAL_AGE:  # ageが20より小さいときに処理を実行
    print('未成年')
else:
    print('成人')

# format文
print(f'age = {age}')  # 3.6
print(f'{age=}')  # 3,8
