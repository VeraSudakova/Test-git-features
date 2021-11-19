def int_process(ints_tuple):
    res = ""
    for i in range(0, (len(ints_tuple) // 2)):
        res += str(ints_tuple[i]) + str(ints_tuple[len(ints_tuple) - 1 - i]) + " "
    res += str(ints_tuple[i+1])
    return res
