def anagram(str1, str2):
    str1 = str1.lower().replace(' ', '')
    str2 = str2.lower().replace(' ', '')
    if len(str1) == len(str2) and sorted(str1) == sorted(str2):
        return True
    else:
        return False

print(anagram('listen', 'Silent'))
