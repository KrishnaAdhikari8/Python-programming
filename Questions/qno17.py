# Check whether a string is palindrome

string = input("enter the string to cheak the palindrome or not ? ")
rev_string = string[::-1]
if string == rev_string:
    print("pallindrome")
else:
    print("not pallindrome")