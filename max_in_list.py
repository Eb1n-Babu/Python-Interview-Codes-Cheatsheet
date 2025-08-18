def max_in_list(lst):
    sorted_lst = sorted(lst)
    max_value = sorted_lst[len(sorted_lst) - 1]
    return max_value



list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(max_in_list(list1))