# Реализоватьскрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv as my_argv

try:
    script_name, amount_hours, rate, bonus = my_argv
except ValueError:
    print("Invalid args")
    exit()

def salary_calc (amount_hours, rate, bonus):
    return (float(amount_hours) * float(rate)) + float(bonus)

print("Salary: {}".format(salary_calc (amount_hours, rate, bonus)))