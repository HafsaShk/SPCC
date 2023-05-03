import re
import pandas as pd
import numpy as np
import pprint

# Importing input file which is a C program
inputFile = open('exp8_lexical_input.txt', 'r')
inputString = inputFile.read(200)
# Splitting the file in words
token_list = re.split('[ ;()\n\t]', inputString)
# print(token_list)

# Defining Tokens
keyword = ['break', 'case', 'char', 'const', 'countinue', 'default', 'do', 'int', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
           'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
built_in_functions = ['clrscr', 'printf', 'scanf', 'getch', 'main']
operators = ['+', '-', '*', '/', '%', '==', '!=', '>', '<', '>=', '<=',
             '&&', '||', '!', '&', '|', '^', '~', '>>', '<<', '=', '+=', '-=', '*=']
specialsymbol = ['@', '#', '$', '_', '!']
separator = [',', ':', ';', '\n', '\t', '{', '}', '(', ')', '[', ']']

# To check if word is a number or not (precisely to check if word is float or not)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Dictionary to store various tokens found in input program
input_tokens = {
    'Keywords': [],
    'Operators': [],
    'Special Symbols': [],
    'Built-in Functions': [],
    'Header Files': [],
    'Constants': [],
    'Identifiers': []
}

# Creating dataframe for symbol table
symbol_table = pd.DataFrame(columns=['Variable Name', 'Type', 'Value'])

for i in range(0, len(token_list)):
    if token_list[i] in keyword:
        if token_list[i] not in input_tokens['Keywords']:
            input_tokens['Keywords'].append(token_list[i])
        continue
    if token_list[i] in operators:
        if token_list[i] not in input_tokens['Operators']:
            input_tokens['Operators'].append(token_list[i])
        continue
    if token_list[i] in specialsymbol:
        if token_list[i] not in input_tokens['Special Symbols']:
            input_tokens['Special Symbols'].append(token_list[i])
        continue
    if token_list[i] in built_in_functions:
        if token_list[i] not in input_tokens['Built-in Functions']:
            input_tokens['Built-in Functions'].append(token_list[i])
        continue
    if token_list[i] in separator:
        # print("Separator -->", token_list[i])
        continue
    if re.match(r'(#include*).*', token_list[i]):
        if token_list[i+1] not in input_tokens['Header Files']:
            input_tokens['Header Files'].append('#include ' + token_list[i+1])
        continue
    if is_number(token_list[i]):
        if token_list[i] not in input_tokens['Constants']:
            input_tokens['Constants'].append(token_list[i])
        continue
    if re.match(r"^[^\d\W]\w*\Z", token_list[i]):
        if token_list[i] not in input_tokens['Identifiers']:
            input_tokens['Identifiers'].append(token_list[i])
            if(token_list[i+1] == '='):
                symbol_table.loc[len(symbol_table.index)] = [token_list[i], token_list[i-1], token_list[i+2]]

print("\nTokens present in input program: \n")
pprint.pprint(input_tokens)

# Rearranging index
symbol_table.index = symbol_table.index + 1
# Naming the index column
symbol_table.index.name = 'Sr No'

# Exporting Symbol table to csv
symbol_table.to_csv('symbol_table.csv')
