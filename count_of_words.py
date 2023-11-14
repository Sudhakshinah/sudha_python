# the function splits the given string and count the number of words using len method
def count_of_words(s1):
    split_string = s1.split()
    word_count = len(split_string)
    return word_count


string1 = input("Enter the string: ")
total_no_words = count_of_words(string1)
print(total_no_words)