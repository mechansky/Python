result = float(input('Сколько километров пробежал спортсмен в первый день? '))
goal = float(input('Какого результата спортсмен хочет достичь? (в километрах) '))
day = 1

print('Результат:\n')
while result < goal:
    print(f'{day}-й день: {result:.2f} км')
    day +=1
    result = float(result * 1.1)
    if result > goal:
        print(f'{day}-й день: {result:.2f} км')
    else:
        continue

print(f'Итог: прибавляя 10% к результату ежедневно, спортсмен достигнет конечной цели в {goal:.2f} км на {day}-й день.')


input()