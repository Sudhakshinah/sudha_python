def non_repeating(l1):

# Iterate through the list and when the count of the element is 1 it returns that element

    for i in l1:
        if l1.count(i) == 1:
            return i

# Take the input from user for the size of the list and the elements


size = int(input("Enter the size of the integer list: "))
li = []
for i in range(0, size):
    list1 = input("Enter the elements: ")
    li.append(list1)

# Function call

output = non_repeating(li)
print(f" The first non repeating element in the integer list is {output}")




