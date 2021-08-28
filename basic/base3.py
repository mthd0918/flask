# 9. 論理型、AND、OR

# 論理型、TrueとFalseの二つの値を扱う変数型

is_animal = True
if is_animal:
    print('動物です')

is_man = False
is_adult = False

# or文(論理型)
if is_man or is_adult:
    print('男か大人です')

# and文(論理積)
if is_man and is_adult:
    print('成人男性です')
