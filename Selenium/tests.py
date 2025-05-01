# # Take user input for the number of elements in the list
# n = int(input("Enter the number of elements in the list: "))
#
# # Initialize an empty list to store user input
# user_list = []
#
# # Use a for loop to iterate over the range of numbers from 0 to n-1
# for i in range(n):
#     # Take user input for each element and convert it to an integer
#     element = int(input(f"ebter "))
#     # Append the element to the user list
#     user_list.append(element)
#
# # Print the resulting list
# print("User input list:", user_list)
a = input('enter you elements with spaces')
user_list = [int(i) for i in a.split()]
print(user_list)