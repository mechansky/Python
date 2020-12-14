a = input('Введите строку из нескольких слов: ')
n = 1
l = a.split(" ")

for element in l:
    print(f'{n}. {element[:10]}')
    n += 1

input()

