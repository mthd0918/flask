# 辞書型のメソッド


car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}

tmp_car = {'country': 'Japan', 'prefetcture': 'Aichi', 'model': 'カローラ'}

car.update(tmp_car)  # 追加、更新
print(car)

car['city'] = 'Toyota-shi'
car['year']
print(car)

value = car.popitem()
print(car)
print(value)

value = car.pop('model')
print(car)
print(value)

car.clear()
print(car)

del car
print(car)
