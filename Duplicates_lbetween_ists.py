def duplicate_list(l1, l2, l3):

    # list is converted to set using set function to use intersection method

    set1 = set(l1)
    set2 = set(l2)
    set3 = set(l3)

    # Intersection between set1 and set2

    common1 = set1.intersection(set2)

    # Intersection between result and set3

    common2 = common1.intersection(set3)
    return list(common2)


list1 = [1, 3, 5, 7, 9, 12]
list2 = [5, 12, 15, 8, 2, 14]
list3 = [5, 12, 17, 1, 5, 19]
output = duplicate_list(list1, list2, list3)
print(f"The duplicate element between the 3 list is {output}")
