def vowel_removal(a):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for i in a:
        if i in vowel_list:
            new_string = a.replace(i, "")
            return new_string


input_string = input("enter the string: ")
string_without_vowel = vowel_removal(input_string)
print(string_without_vowel)