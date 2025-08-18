def count_special_char(string):
    count = 0
    sp = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for char in string:
        if char in sp:
            count += 1
        else:
            continue
    print(count)

count_special_char("hello world!#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
