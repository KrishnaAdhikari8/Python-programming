# A generator is a special function that returns values one at a time using the yield keyword.
def count():
    for i in range(1, 6):
        yield i

g = count()

for num in g:
    print(num)