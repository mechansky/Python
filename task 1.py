l1 = ['строка', 123, 3.22, [2, 2, 8], (1, 4, 8, 8)]

print(f'наш условный список: {l1}')
for element in l1:
    a = type(element)
    print(f'{element}: {str(a)}')