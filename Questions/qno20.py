# Remove duplicate characters from a string.

text = input("enter a text :")

result = ""
for char in text:
    if char not in result:
        result = result+char

    
print("after removing duplication:",result)
        
    