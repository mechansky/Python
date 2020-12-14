months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
seasons = ['зима', 'весна', 'лето', 'осень']
d1 = {
    seasons[0]: [months[-1], months[:2]],
    seasons[1]: months[2:5],
    seasons[2]: months[5:8],
    seasons[3]: months[8:11]
}

month = int(input('введите значение: '))

for keys, values in d1.items():
    if month in values:
        print(keys)

input()


