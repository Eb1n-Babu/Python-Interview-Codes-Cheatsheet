import re


def remove_whitespace(s):
    return s.replace(" ", "")

def remove_whitespaces1(s):
    r = re.sub(r" ", "", s)
    return r


print(remove_whitespace("diuuhdudiudueuj     "))
print(remove_whitespaces1("diuuh  dudiudueuj     "))
