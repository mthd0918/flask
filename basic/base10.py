# Dictionary(辞書型)

car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015, 1: 100}

print(car['brand'])
print(car.get('bran', 'Dose not exist'))
print(car.get('bran', 12))

print(car.get(1))

print(car.keys())  # キー一覧
print(car.values())  # 値一覧
print(car.items())  # キー + 値

for k, v in car.items():
    print('key =  {}, vales = {}'.format(k, v))

    if 'brand' in car:
        print('car のブランドは{}'.format(car['brand']))
