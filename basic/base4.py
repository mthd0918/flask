# 10. 整数型、浮動小数点数型、数値演算、ビット演算、シフト演算～基本講座１～

# int 整数
# float 浮動小数点数


# 数値型

value = 1
# print(value)
# value = -2
# print(value)
# value = value + 4
# print(value)
# print(value * 4)
# print(value / 3)
# value = 10
# print(value // 3)  # 切り下げ
# print(value % 3)

value += 3
# value -= 2
print(value)

print(value ** 3)

# 浮動小数点数
height = 175.5

print(height)
print(type(height))
print(height + 10)  # 175.5 + 10.0


# シフト演算
value = 8  # 1000 => 0010
print(value >> 2)
print(value << 3)  # 1000 => 100000

# 論理積、論理和
print(12 & 21)  # 01100 and 10101 = 00100 => 4
print(12 | 21)  # 01100 or 10101 = 11101 => 29

value = 12
value &= 21  # value = value & 21
print(value)
