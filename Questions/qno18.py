# Reverse a string without slicing.

def rev_string(s):
    result = " "
    for char in s:
        result = char +result
    return result

print(rev_string("hello"))