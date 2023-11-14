# Anagram is a when the letters of one word is rearranged to form another word
def anagram_strings(string1, string2):
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    if sorted_string1 == sorted_string2:
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")


s1 = input("Enter the string1: ")
s2 = input("Enter the string2: ")
anagram_strings(s1, s2)

