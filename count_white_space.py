def count_white_space(word):
    count = 0
    for element in word:
        if ' ' == element:
            count += 1
        else:
            continue
    print(count)

count_white_space('l i s t e n    ')