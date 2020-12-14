l = [7, 5, 3, 3, 2]
number = int(input('введите цифру: '))

if number in l:
    l.insert(l.index(number) + 1, number)
elif number > max(l):
    l.insert(0, number)
elif number < min(l):
    l.append(number)

print(l)

input()