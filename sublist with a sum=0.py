def sum_of_sublist(list1):
    sublist = []
    for i in range(0, len(list1)):
        for j in range(i+1, len(list1)):
            sublist.append(list1[i:j])

    for elem in sublist:
        if sum(elem) == 0:
            return elem


input_list = [4, 2, -3, 1, 6]
result = sum_of_sublist(input_list)
print(f" The sublist whose sum is zero is {result}")

