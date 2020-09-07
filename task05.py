#Реализовать формирование списка, используя функцию range() и возможности генератора.
#В список должны войти четные числа от 100 до 1000 (включая границы).
#Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

def my_func(prev_item, item):
    return prev_item * item

print(reduce(my_func, [item for item in range(100, 1001)]))
