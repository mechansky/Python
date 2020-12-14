d = {'название': [], 'цена': [], 'количество': [], 'ЕИ': []}

product1 = (1, {'название': ''})
product1[1]['название'] = input('введите название товара №1 ')
product1[1]['цена'] = float(input(f'введите цену товара №1 '))
product1[1]['количество'] = float(input(f'введите количество товара №1: '))
product1[1]['ЕИ'] = input(f'введите единицу измерения товара №1: ')

product2 = (1, {'название': ''})
product2[1]['название'] = input('введите название товара №2 ')
product2[1]['цена'] = float(input(f'введите цену товара №2 '))
product2[1]['количество'] = float(input(f'введите количество товара №2: '))
product2[1]['ЕИ'] = input(f'введите единицу измерения товара №2: ')

product3 = (1, {'название': ''})
product3[1]['название'] = input('введите название товара №3 ')
product3[1]['цена'] = float(input(f'введите цену товара №3 '))
product3[1]['количество'] = float(input(f'введите количество товара №3: '))
product3[1]['ЕИ'] = input(f'введите единицу измерения товара №3: ')


for keys, values in d.items():
    if keys in product1[1]:
        d[keys].append(product1[1][keys])
    if keys in product2[1]:
        d[keys].append(product2[1][keys])
    if keys in product3[1]:
        d[keys].append(product3[1][keys])

print(f'Список товаров:\n{product1}\n{product2}\n{product3}')
print(f'Сводная аналитика по товарам:\n{d}')




