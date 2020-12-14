l1 = []
len_l1 = int(input('Сколько элементов будет в списке? '))
n = 1

while n <= len_l1:
    l1.append(input(f' Введите элемент №{n}: '))
    n += 1
print(f'Наш список:\n{l1}')

n = 0

while n < len(l1):
    try:
        l1[n], l1[n + 1] = l1[n + 1], l1[n]
    except Exception:
        break
    n = n + 2
print(f'Поменяем соседние элементы местами. Теперь наш список выглядит так:\n{l1}')

input()