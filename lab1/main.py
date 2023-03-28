##################################################
#Лабораторная работа №1 по дисциплине Логические основы интеллектуальных систем
#Выполнена студентками группы 121702 БГУИР Витковской Софией Игоревной и Мойсевич Александрой Вячеславовной
#Данный файл реализует функцию ручного тестирования программы проверки на принадлежность формулы к классу КНФ
#27.03.2023 1.0

from defs import formula_to_list
from defs import checking

def start():
    print('Enter your formula, please')
    formula = input()
    if(formula == 'exit'): exit(0)

    formula = formula_to_list(formula)
    if checking(formula):
        print('is CNF')
    else:
        print('is not a CNF')
    return True

while(start()):
    continue