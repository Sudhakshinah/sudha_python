def count_unique_characters(string):
    set1 = set()
    for i in string:
        set1.add(i)
    print(len(set1))


input_string = input("Enter the string: ")
count_unique_characters(input_string)

