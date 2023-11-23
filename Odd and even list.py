input_list = [10, 501, 22, 37,100,999,87,351]
odd_list = []
even_list = []
for i in input_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(odd_list)
print(even_list)
