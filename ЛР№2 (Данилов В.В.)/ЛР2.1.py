money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while spend < money_capital:
    if month == 1:
        month += 1
        money_capital += salary - spend
    else:
        month +=1
        spend *= (1 + increase)
        money_capital += salary - spend

print("Количество месяцев, которое можно протянуть без долгов:", month)
