import account
import pandas as pd

def main():
    z3()

def testNumberOperations():
    oper_list =[3 + 7, 5 - 6, 7/2, 7//2, 7%3, 7**2]
    for i in range(len(oper_list)):
        print(oper_list[i])

def Bank():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    period = int(input("Введите период ведения счета в месяцах: "))

    result = account.calculate_income(rate, money, period)
    print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n",
          "Период: ", period, "\n", "Сумма на счете в конце периода: ", result)

def z3():
    values = [12, 134, 10, 47, 100, 20, 50, 160, 210]
    tens = list()
    for i in values:
        if i % 10 == 0:
            tens.append(i)
    print(tens)

main()

