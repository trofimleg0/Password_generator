import string
from random import choice

# functions for requesting data from the user
def count():
    n = input('How many passwords do you need? Specify the number: ')
    while n.isdigit() == False:
        print('You need to enter a number!')
        n = input('How many passwords do you need? Specify the number: ')
    return int(n)

def is_long():
    l = input('Enter the password length: ')
    while l.isdigit() == False:
        print('You need to enter a number!')
        l = input('Enter the password length: ')
    return int(l)

def is_number():
    isn = input('Do you need the numbers 0123456789 in the password? Write "yes" or "no": ')
    while isn.lower() not in ['yes', 'no']:
        print('You need to enter "yes" or "no".')
        isn = input('Do you need the numbers 0123456789 in the password? Write "yes" or "no": ')
    return isn

def is_upper():
    isup = input('Do you need capital letters in the password? Write "yes" or "no": ')
    while isup.lower() not in ['yes', 'no']:
        print('You need to enter "yes" or "no".')
        isup = input('Do you need capital letters in the password? Write "yes" or "no": ')
    return isup

def is_lower():
    islw = input('Do you need lowercase letters in the password? Write "yes" or "no": ')
    while islw.lower() not in ['yes', 'no']:
        print('You need to enter "yes" or "no".')
        islw = input('Do you need lowercase letters in the password? Write "yes" or "no": ')
    return islw
    
def is_symbol():
    issmb = input('Do you need characters in the password? Write "yes" or "no": ')
    while issmb.lower() not in ['yes', 'no']:
        print('You need to enter "yes" or "no".')
        issmb = input('Do you need characters in the password? Write "yes" or "no": ')
    return issmb

def is_ambiguous():
    amb = input('Will there be ambiguous characters "il1Lo0O" in the password? Write "yes" or "no": ')
    while amb.lower() not in ['yes', 'no']:
        print('You need to enter "yes" or "no".')
        amb = input('Will there be ambiguous characters "il1Lo0O" in the password? Write "yes" or "no": ')
    return amb

# collect the characters selected by the user together
def gen_chars():
    chars = ''
    if isn == 'yes':
        chars += string.digits
    if isup == 'yes':
        chars += string.ascii_uppercase
    if islw == 'yes':
        chars += string.ascii_lowercase
    if issmb == 'yes':
        chars += string.punctuation
    if amb == 'no':
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')
    return chars
    
# making passwords
def build_password():
    for i in range(n):
        password = []
        for i in range(l):
            password.append(choice(chars))
        print(''.join(password))
        
# program start
n = count()
l = is_long()
isn = is_number()            
isup = is_upper()
islw = is_lower()
issmb = is_symbol()
amb = is_ambiguous()
chars = gen_chars()
build_password()