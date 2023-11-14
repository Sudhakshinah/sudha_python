def frequent_occurring_character(string):
    dict1 = {}

    for i in string:
        count1 = string.count(i)
        dict1[i] = count1

    frequent_occurrence = max(dict1, key=dict1.get)
    return frequent_occurrence


input_string = input("Enter the string: ")
result = frequent_occurring_character(input_string)
print(result)


