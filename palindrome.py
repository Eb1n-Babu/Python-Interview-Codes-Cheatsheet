def palindrome(word):
    word = word.lower().replace(' ', '')
    reverse = word[::-1]
    reverse = reverse.lower().replace(' ', '')
    if word == reverse:
        return True
    else:
        return False

print(palindrome('malayalam'))