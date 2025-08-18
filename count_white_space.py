def count_white_space(word):
    count = 0
    for element in word:
        if ' ' == element:
            count += 1
        else:
            continue
    print(count)

def count_white_space2(word):
    print(word.count(' '))

count_white_space('l i s t e n    ')
count_white_space2('l i s t e n')