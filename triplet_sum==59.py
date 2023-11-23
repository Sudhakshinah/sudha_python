def triplets_59(list1):

    # Declare the empty list to append the triplets

    triplets = []

    # to find the first element of the triplet

    for i in range(0, len(list1)-2):

        # To find the second element of the triplet

        for j in range(i+1, len(list1)-1):

            # To find the third element of the triplet

            for k in range(j+1, len(list1)):

                # condition check to verify if the sum of the triplets is equal to 59

                if list1[i]+list1[j]+list1[k] == 59:
                    triplets.append([list1[i], list1[j], list1[k]])
                    return triplets


input_list = [10, 20, 30, 9]
triplet_list = triplets_59(input_list)
print(f"The triplet from the given list where the sum =59 is {triplet_list}")