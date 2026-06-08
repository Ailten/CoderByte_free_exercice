
# Valid Number (hard).
# https://leetcode.com/problems/valid-number/description/

import re

def func(s: str) -> bool:

    integer_num = r'[-+]?[0-9]+'
    decimal_num = r'[-+]?([0-9]+[.][0-9]*|[0-9]+[.][0-9]+|[0-9]*[.][0-9]+)'
    exponent = r'[eE]' + integer_num
    if re.search('^' + integer_num + '(' + exponent + ')' + r'?$', s) != None:
        return True
    if re.search('^' + decimal_num + '(' + exponent + ')' + r'?$', s) != None:
        return True
    return False


i_size = 12
print('__________ part 1')  # expect True.

print('2'.ljust(i_size) + ' -> ' + str(func("2")))
print('0089'.ljust(i_size) + ' -> ' + str(func("0089")))
print('-0.1'.ljust(i_size) + ' -> ' + str(func("-0.1")))
print('+3.14'.ljust(i_size) + ' -> ' + str(func("+3.14")))
print('4.'.ljust(i_size) + ' -> ' + str(func("4.")))
print('-.9'.ljust(i_size) + ' -> ' + str(func("-.9")))
print('2e10'.ljust(i_size) + ' -> ' + str(func("2e10")))
print('-90E3'.ljust(i_size) + ' -> ' + str(func("-90E3")))
print('3e+7'.ljust(i_size) + ' -> ' + str(func("3e+7")))
print('+6e-1'.ljust(i_size) + ' -> ' + str(func("+6e-1")))
print('53.5e93'.ljust(i_size) + ' -> ' + str(func("53.5e93")))
print('-123.456e789'.ljust(i_size) + ' -> ' + str(func("-123.456e789")))

print('__________ part 2')  # excpect False.

print('abc'.ljust(i_size) + ' -> ' + str(func("abc")))
print('1a'.ljust(i_size) + ' -> ' + str(func("1a")))
print('1e'.ljust(i_size) + ' -> ' + str(func("1e")))
print('e3'.ljust(i_size) + ' -> ' + str(func("e3")))
print('99e2.5'.ljust(i_size) + ' -> ' + str(func("99e2.5")))
print('--6'.ljust(i_size) + ' -> ' + str(func("--6")))
print('-+3'.ljust(i_size) + ' -> ' + str(func("-+3")))
print('95a54e53'.ljust(i_size) + ' -> ' + str(func("95a54e53")))