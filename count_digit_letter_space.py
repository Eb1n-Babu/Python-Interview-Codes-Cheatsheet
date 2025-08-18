import re


def count_digit_letter_space(s):
    a = '1234567890'
    b = 'abcdefghijklmnopqrstuvwxyz'
    c = b.upper()
    d = ' '
    count_a = 0
    count_b = 0
    count_d = 0
    for elements in s:
        if elements in a:
            count_a += 1
        if elements in b or c:
            count_b += 1
        if elements in d:
            count_d += 1
    print("Numbers     = :", count_a)
    print("character   = :", count_b)
    print("white space = :", count_d)

count_digit_letter_space('l i s t e n    ')
count_digit_letter_space('leidduiduidiuhe3eun   ')

def count_digit_letter_space1(s):
    digits = re.sub('[^0-9]', '', s)
    alphabet = re.sub('[^a-zA-Z]', '', s)
    white_space = re.findall(' ',s)
    digits1 = re.findall('[0-9]',s)
    print(len(digits))
    print(len(alphabet))
    print(len(white_space))
    print(len(digits1))

count_digit_letter_space1('l i s t e n  42356gegrg     ')

