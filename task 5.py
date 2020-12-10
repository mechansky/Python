proceeds = float(input('Введите сумму выручки от продаж: '))
costs = float(input('Введите сумму издержек: '))

profit = proceeds - costs
profitability = profit / proceeds * 100

if proceeds > costs:
    print(f'Поздравляем! Ваше предприятие работает в прибыль.\nПрибыль составляет {profit:.2f} рублей')
    print(f'Рентабельность составляет {profitability:.2f}%')
    workers = int(input('сколько сотрудников работает на предприятии? '))
    profitOfWorkers = profit / workers
    print(f'На одного сотрудника приходится {profitOfWorkers:.2f} руб прибыли!')
elif proceeds < costs:
    profit = abs(profit)
    print(f'К сожалению, предприятие работает в убыток.\nУбыток составляет {profit:.2f} рублей')
elif proceeds == costs:
    print('Вы работаете в ноль!')
else:
    print('Ошибка!')

input()