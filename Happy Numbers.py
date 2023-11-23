# A number is a happy number when the sum of the squares of the digits is equal to 1
input_list = [10, 501, 22, 37, 100, 999, 87, 351]
# An empty list is declared to store the happy numbers from the given list.
happy_list = []
for i in input_list:
    x = i
    while x >= 10:
        sum_of_digits = 0
        while x > 0:
            rem = x % 10
            sum_of_digits += rem ** 2
            x = x//10
        if sum_of_digits == 1:
            happy_list.append(i)
print(happy_list)
length_of_happy_list = len(happy_list)
print(f"The count of happy numbers in the list is {length_of_happy_list}")







