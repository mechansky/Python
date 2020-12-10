number = int(input('Введите количество секунд, чтобы перевести их в часы: '))

hours = number // 3600
minutes = int(number % 3600 / 60)
sec = number % 3600  % 60

print(f'Форматируем {number} сек.:\n{hours}ч:{minutes}м:{sec}с')

input()