# Remove duplicates from a list.
my_list = [1, 2, 2, 3, 1, 4, 5, 5]
unique_list = list(dict.fromkeys(my_list))
print("Original List:", my_list)
print("List without duplicates:", unique_list)