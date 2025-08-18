def count_vowels(string):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in string:
        if ch not in vowels:
            count += 1
        else:
            continue
    print(count)

count_vowels("hellodd2dfdffeeeee")


