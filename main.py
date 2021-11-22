from int_processing import int_process
from string_processing import string_process


a = 11
b = 22
c = 33
ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
strings = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')
res_int = int_process(ints)
string_res = string_process(strings)
print(res_int + '\n' + string_res)
print('\n')
