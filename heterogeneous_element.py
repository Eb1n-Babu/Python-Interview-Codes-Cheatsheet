def heterogeneous_element(list_1):
    list_2 = []
    for item in list_1:
        if type(item) == int:
            list_2.append(item)
    print(list_2)



hetero_list = [
    25, "alpha", 3.14, False, None,
    {"id": 1}, [1, 2], (3, 4), {5, 6}, b"bytes",
    complex(2, 3), "beta", 0, True, 99.99,
    -42, "gamma", {"nested": ["list", 123]}, 7.7,
    "delta", range(5), frozenset([8, 9]), bytearray(b"data"),
    lambda x: x * 2, Exception("demo error")
]
heterogeneous_element(hetero_list)