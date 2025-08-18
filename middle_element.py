def middle_element(list_):
    if len(list_) % 2 == 0:
        x = len(list_) // 2
        print(list_[x - 1], list_[x])
    if len(list_) % 2 != 0:
        x = len(list_) // 2
        print(list_[x])


list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]
middle_element(list_)