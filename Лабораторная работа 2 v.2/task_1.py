money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

raznica = spend - salary# По условию первый месяц повышения цен нет.
months = 0
while raznica < money_capital:
 raznica = spend - salary
 spend *= 1 + increase  # В данном случае цифра 1 необходима для перевода процентов в целое число.
 money_capital -= raznica
 months += 1

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)
