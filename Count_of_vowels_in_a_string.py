user_input=input("Enter the string: ")
vowel_list=['a','e','i','o','u']
# count of each vowels in a given string
count_of_a=user_input.count('a')
count_of_e=user_input.count('e')
count_of_i=user_input.count('i')
count_of_o=user_input.count('o')
count_of_u=user_input.count('u')
# To find the total count of all the vowels in a given string
vowel_count=0
for i in user_input:
   if i in vowel_list:
       vowel_count+=1
print(f"total no of occurences of a  in the {user_input} is {count_of_a}")
print(f"total no of occurences of e  in the {user_input} is {count_of_e}")
print(f"total no of occurences of i  in the {user_input} is {count_of_i}")
print(f"total no of occurences of o in the  {user_input} is {count_of_o}")
print(f"total no of occurences of u  in the {user_input} is {count_of_u}")
print(f"The total number of vowel in the    {user_input} is {vowel_count}")