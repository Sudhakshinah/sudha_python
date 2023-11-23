def sum_last_first(num):
 #   convert to string to use indexing to retrieve the number
    number_string = str(num)
 # Get the last  and the first digit  using indexing
    first_digit = number_string[0]
    last_digit = number_string[-1]
    sum_of_last_first = int(first_digit)+int(last_digit)
    return sum_of_last_first


user_input = int(input("Enter the number: "))
final_sum = sum_last_first(user_input)
print(f"The sum of first and last digit of the given number is {final_sum}")