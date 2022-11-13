# 1
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

# 2
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))
# 3
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))
# 4
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))
# 5
print("Anna has {} apples and {} peaches".format(4, 2))
# 6
print("Anna has {0} apples and {1} peaches".format(3, 5))
# 7
print("Anna has {apl} apples and {pchs} peaches".format(apl=5, pchs=8))
# 8
print("Anna has {a} apples and {p} peaches".format(a="_" * 5, p="_" * 3))
# 9
a = 5
b = 7
print(f"Anna has {a} apples and {b} peaches")
# 10
print("Anna has %s apples" % a)

# 11
dict_a = {"apples": 5, "peaches": 9}
print("Anna has {} apples and {} peaches".format(dict_a["apples"], dict_a["peaches"]))

# 12
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num)
    else:
        lst.append(num ** 4)
print(lst)

lst = [num if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)
# 13
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)

list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print(list_comprehension)
# 14
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d)
# 15
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d)
# 16
dict_comprehension = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
print(dict_comprehension)

dict_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3
print(dict_comprehension)

# 17
dict_comprehension = {x: x ** 3 if x ** 3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)

dict_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3
    else:
        dict_comprehension[x] = x
print(dict_comprehension)


# 18
def foo(x, y):
    if x < y:
        return x
    else:
        return y
foo = lambda x, y: x if x < y else y

# 19
foo = lambda x, y, z: z if y < x and x > z else y

def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
#20
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
#21
print(sorted(lst_to_sort, reverse=True))
# 22.
lst_multiply = list(map(lambda x: x *2, lst_to_sort))
print(lst_multiply)
# 23
list_A = [2, 3, 4]
for i in list_A:
    lst_A_new = list(map(lambda x: x * i, lst_to_sort))
    print(lst_A_new)

list_B = [5, 6, 7]
for j in list_B:
    list_B_new = list(map(lambda x: x * j, lst_to_sort))
    print(list_B_new)

#24
lst_2 = list(filter(lambda num: num % 2 == 1, lst_to_sort))
print(lst_2)

# 25
b = range(-10, 10)
lst_negative = list(filter(lambda num: num < 0, b))
print(lst_negative)

# 26
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
list_common = list(filter(lambda x: x in list_1, list_2))
print(list_common)
