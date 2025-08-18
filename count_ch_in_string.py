def count_ch_in_string(string):
    count = 0
    enter = input("enter the character to count :")
    if len(enter) > 1:
        print("only one character allowed")
    if len(enter) == 1:
        if enter in string:
            count += 1
        print(count)


if __name__ == '__main__':
    try:
        count_ch_in_string("hellodd2dfdffeeeee")
    except TypeError:
        print("Type error")


