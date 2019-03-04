#! python3

from balanced_brackets import check_brackets

input1 = '{[]{()}}'
input2 = '[{}{}(]'
input3 = ']['
input4 = ''
input5 = '('
input6 = ']'

def test_check_brackets():
    assert check_brackets(input1) == 'balanced', 'input1 evaluated incorrectly'
    assert check_brackets(input2) == 'unbalanced', 'input2 evaluated incorrectly'
    assert check_brackets(input3) == 'unbalanced', 'input3 evaluated incorrectly'
    assert check_brackets(input4) == 'balanced', 'input4 evaluated incorrectly'
    assert check_brackets(input5) == 'unbalanced', 'input5 evaluated incorrectly'
    assert check_brackets(input6) == 'unbalanced', 'input6 evaluated incorrectly'