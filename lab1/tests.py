##################################################
#Лабораторная работа №1 по дисциплине Логические основы интеллектуальных систем
#Выполнена студентками группы 121702 БГУИР Витковской Софией Игоревной и Мойсевич Александрой Вячеславовной
#Данный файл реализует функции для тестирования программы проверки на принадлежность формулы к классу КНФ
#27.03.2023 1.1 исправлено: считывание \/ и /\

from defs import checking
from defs import formula_to_list

#тесты, предполагающие, что введенная формула является КНФ
def expect_true(formula):
    answer = checking(formula_to_list(formula))
    if answer: print( f'formula: {formula}, the program returned: {answer}, test passed')
    else: print( f'formula: {formula}, the program returned: {answer}, test failed')

#тесты, предполагающие, что введенная формула не является КНФ
def expect_false(formula):
    answer = checking(formula_to_list(formula))
    if not(answer): print( f'formula: {formula}, the program returned: {answer}, test passed')
    else: print( f'formula: {formula}, the program returned: {answer}, test failed')

def start_tests():
    expect_true('A')
    expect_true('(!A)')
    expect_false('(A)')
    expect_false('!A')
    expect_false('1')
    expect_false('0')
    expect_false('.L')
    expect_true('(A/\\((B\\/C)\\/D))')
    expect_false('A/\\B')
    expect_true('(A/\\B)')
    expect_false('()()')
    expect_false('((A->B)/\\(C\\/D))')
    expect_false('((A\\/B)/\\(C~D))')
    expect_false('(1/\\2)')
    expect_true('(A12/\\D)')
    expect_true('(A345/\\(((B34\\/C123)\\/D43)/\\(B34\\/((C123\\/M3)\\/N4))))')
    expect_false('(A345/\\((B0\\/C)\\/D))')
    expect_false('(!1/\\B)')
    expect_false(' ')
    expect_false('')
    expect_false('((\\/)/\\(\\/))')
    expect_false('(A/\\(B\\/C1)')
    expect_false('((!A)\\/(B/\\(!C))')
    expect_false('(((!C)\\/(A\\/ B))/\\((((!B)\\/(!C))\\/(!D))\\/A)\\/(A\\/((!C)\\/(!D))))')
    expect_true('((((!C)\\/(A\\/B))/\\((((!B)\\/(!C))\\/(!D))\\/A))/\\(A\\/((!C)\\/(!D))))')
    expect_true('(((!C)\\/(A\\/B))/\\((!B)\\/(A\\/((!C)\\/(!D)))))')
    expect_false('((!A)/\\(B\\/(!C))/\\)')
    expect_false('((!A)\\/(!B))/\\((B\\/(!C))\\/))')
    expect_false('((A\\/B)(C\\/D))')
    
start_tests()