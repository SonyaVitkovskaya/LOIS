##################################################
#Лабораторная работа №1 по дисциплине Логические основы интеллектуальных систем
#Выполнена студентками группы 121702 БГУИР Витковской Софией Игоревной и Мойсевич Александрой Вячеславовной
#Данный файл прендназначается для реализации алгоритмов упрощения формулы и определения принадлежности ее к классу КНФ
#27.03.2023 1.1 : исправлено: считывание \/ и /\, двойное отрицание
#28.03.2023 2.0 : исправлено: отрицание только атомарных формул
#30.03.2023 2.1 : исправлено: пробелы не удаляются

LETTERS = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
AND = '&'
OR = '|'
NOT = '!'
VALID_CHARACTERS = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',')', '(', '|', '!', '&']

#функция,преобразующая строку в список символов, убирает пробелы, упрощает символы операций 
def formula_to_list(formula):
    formula = check_variable_name(formula)
    formula = list(formula)
    i = 0
    while i < len(formula):
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
        i += 1
    return formula

#функция, проверяющая, чтобы формула содержала отрицания только атомарных формул
def negation_check(expression):
    for index in range(0, len(expression), 1):
        if index >= 1 and index < (len(expression)-2) and expression[index]=='!':
            if (expression[index-1] == '(') and (expression[index+1] in LETTERS) and expression[index+2]==')':
                index = expression.index('!', index, len(expression))
            else: return ''
    return expression

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
    start = len(expression) - 1
    while(expression.count('|') != 0 or expression.count('!') != 0):
        start_ind = find_index(expression, start)
        end_ind = expression.index(')', start_ind, len(expression))
        if (end_ind - start_ind) == 4:
            if expression[start_ind+2]=='&': 
                if start != 0:
                    start = start_ind - 1
                continue
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
        start = start_ind
    return expression

#функция, проверяющая все символы на соответствие допустимым символам и решающая, какая из промежуточных проверок запускается
def checking(expression):
    if len(expression) == 0: return False
    if expression.count('!')+ expression.count('|') + expression.count('&') != expression.count('('): return False
    if expression[len(expression) - 1] == '(' : return False
    for i in range (0, len(expression)-1, 1):
        if not(expression[i] in VALID_CHARACTERS): return False
    if expression.count(')') != expression.count('('): return False
    if negation_check(expression) == '': return False
    disj_checking_result = checking_disjunction(expression)
    if disj_checking_result != False: return checking_conjunction(disj_checking_result)
    else: return False 
    
#функция, проверяющая конъюнкции
def checking_conjunction(expression):
    start = len(expression) - 1
    while(expression.count('&') != 0):
        start_ind = find_index(expression, start)
        end_ind = expression.index(')', start_ind, len(expression))
        if (end_ind - start_ind) == 4:
            result = binary_checking(expression[start_ind + 1:end_ind], AND)
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
        start = start_ind
    if ''.join(expression) in LETTERS: return True
    else: return False


#функция поиска индекса последней открывающейся скобки
def find_index(expression, start):
    for index in range(start, -1, -1):
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