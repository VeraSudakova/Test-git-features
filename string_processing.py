def string_process(strings_tuple):
    res = str()
    for i in range(0, (len(strings_tuple) // 2)):
        res += strings_tuple[i] + strings_tuple[len(strings_tuple) -1 - i] + " "
    res += strings_tuple[i+1]
    return res
