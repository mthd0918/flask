# タプル

fruit = ('apple', 'banana', 'lemon')

print(fruit)
print(type(fruit))
print(fruit[0])
# fruit[1] = 'grape'
fruit = fruit + ('grape',)  # コロンを忘れずに！！
print(fruit)

list_fruit = ['apple', 'banana']
fruit = tuple(list_fruit)
print(fruit.count('apple'))
print(fruit.index('banana'))

pos = (135, 35)

countries = {pos: 'Japan'}

print(countries.get(135, 35))
