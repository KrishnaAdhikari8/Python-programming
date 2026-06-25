# List Comprehension is a concise way to create lists in Python using a single line of code.
# List Comprehension Examples in One Program

# 1. Squares of numbers
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

# 2. Even numbers
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even Numbers:", even_numbers)

# 3. Odd numbers
odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print("Odd Numbers:", odd_numbers)

# 4. Convert strings to uppercase
words = ["python", "java", "c++"]
upper_words = [word.upper() for word in words]
print("Uppercase Words:", upper_words)

# 5. Length of each word
lengths = [len(word) for word in words]
print("Word Lengths:", lengths)

# 6. Create list of characters from a string
chars = [ch for ch in "Python"]
print("Characters:", chars)

# 7. Numbers divisible by 3
div_by_3 = [x for x in range(1, 31) if x % 3 == 0]
print("Divisible by 3:", div_by_3)

# 8. Nested List Comprehension (Matrix)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Matrix:")
for row in matrix:
    print(row)
