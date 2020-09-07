# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random

def my_func(prev_item, item):
    if prev_item < item:
        return True
    else:
        return False

my_list = [random.randint(10, 100) for _ in range(10)]
print(f"My list: {my_list}")

res_list = [j for i, j in zip(my_list, my_list[1:]) if j > i]
print(f"My result list: {res_list}")

