input_list = [10, 501, 22, 37, 100, 999, 87, 351]
# This empty list is created to store prime numbers from the given list
prime_list = []
# List is iterated and inner loop iterates in the range starting from 2 to the element in the list to verify prime.
for i in input_list:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_list.append(i)
print(prime_list)

length = len(prime_list)
print(f"count of prime numbers in the list is {length}")




