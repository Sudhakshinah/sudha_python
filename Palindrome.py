def palindrome_function(actual_string):
    reversed_string = actual_string[::-1]
    if actual_string == reversed_string:
        print("True")
    else:
        print("False")


user_input = input("Enter the string: ")
palindrome_function(user_input)

