##################################################
#Лабораторная работа №1 по дисциплине Логические основы интеллектуальных систем
#Выполнена студентками группы 121702 БГУИР Витковской Софией Игоревной и Мойсевич Александрой Вячеславовной
#Данный файл прендназначается для реализации алгоритмов упрощения формулы и определения принадлежности ее к классу КНФ
#27.03.2023 1.1 : исправлено: считывание \/ и /\, двойное отрицание

LETTERS = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
AND = '&'
OR = '|'
NOT = '!'
VALID_CHARACTERS = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',')', '(', '|', '!', '&']

#функция,преобразующая строку в список символов, убирает пробелы, совмещает - и >  в ->, 
def formula_to_list(formula):
    formula = check_variable_name(formula)
    formula = list(formula)
    i = 0
    while i < len(formula):
        if formula[i] == '-' and i != len(formula)- 1:
            if formula[i+1] =='>':
                formula[i] += '>'
                formula.pop(i+1)
                i -= 1
       
        if formula[i] == '/' and i != len(formula)- 1:
            if formula[i+1] =='\\':
                formula[i] = '&'
                formula.pop(i+1)
                i -= 1
        if formula[i] == '\\' and i != len(formula)- 1:
            if formula[i+1] =='/':
                formula[i] = '|'
                formula.pop(i+1)
                i -= 1
        if formula[i] == ' ':
            formula.pop(i)
            i -= 1
        i += 1
    

    if not(formula.count('&')) and not(formula.count('|')): 
        if formula.count('!')>1: return ''
        else : return formula
    return formula[1:len(formula)-1]

#функция, проверяющая имена переменных и если имя является буквой алфвита[натуральное число], то заменяющая его на букву алфавита
def check_variable_name(input_str):
    output = list(input_str)
    index = 0
    while index < len(output):
        c = output[index]
        if c.isupper():
            start_index = index + 1
            while start_index < len(output) and output[start_index].isdigit() and not (output[start_index] == '0' and start_index == index + 1):
                start_index += 1
            if start_index - index > 1:
                output[index:start_index] = [c]
        index += 1
    return ''.join(output)

#проверяет все импликанты пока они не закончатся
def checking_disjunction(expression):
    while(expression.count('(') != 0):
        start_ind = find_index(expression)
        end_ind = expression.index(')', start_ind, len(expression))
        if (end_ind - start_ind) == 4:
            result = binary_checking(expression[start_ind + 1:end_ind], OR)
            if result == '0': return False
            for i in range (0, end_ind - start_ind + 1, 1):
                expression.pop(start_ind)
            expression.insert(start_ind, result)
        elif (end_ind - start_ind) == 3:
            result = unary_checking(expression[start_ind + 1:end_ind])
            if result == '0': return False
            for i in range (0, end_ind - start_ind + 1, 1):
                expression.pop(start_ind)
            expression.insert(start_ind, result)
        else: return False
    return expression

#функция, проверяющая все символы на соответствие допусимым символам и решающая, какая из промежуточных проверок запускается
def checking(expression):
    if len(expression) == 0: return False
    if expression[len(expression) - 1] == '(' : return False
    for i in range (0, len(expression)-1, 1):
        if not(expression[i] in VALID_CHARACTERS): return False
    if expression.count(')') != expression.count('('): return False
    conj_checking_result = checking_disjunction(expression)
    if conj_checking_result: return checking_conjunction(conj_checking_result)
    else: return False 
    
#функция, проверяющая конъюнкции
def checking_conjunction(expression):
    length = len(expression)
    conjunction_amount = expression.count(AND)
    amount_of_pairs = int((length - 1)/2)
    if amount_of_pairs != conjunction_amount: return False
    else:
        for i in range(0, length - 1, 2):
            if not(expression[i] in LETTERS) or not(expression[i+1] == '&'): return False
        if not(expression[len(expression)-1] in LETTERS): return False
    return True

#функция поиска индекса последней открывающейся скобки
def find_index(expression):
    for index in range(len(expression) - 1, -1, -1):
        if expression[index] == '(': return index

#функция, проверяющая бинарные операции на соответствие виду <формула><бинарная связка><формула>
def binary_checking(expression, operation):
    if (expression[0] in LETTERS) and (expression[1] == operation) and (expression[2] in LETTERS):
        return 'A'
    else: return '0'

#функция, проверяющая отрицание на соответствие виду <отрицание><формула>
def unary_checking(expression):
    if (expression[0] == '!') and (expression[1] in LETTERS):
        return 'A'
    else: return '0'