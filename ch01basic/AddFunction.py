
def add(first, second):
    return first + second

number01 = 14
number02 = 5

result = add(number01, number02)  # positional argument
print('%d + %d = %d' % (number01, number02, result))

result = add(first=10, second=20)  # keyword argument
print('%d + %d = %d' % (10, 20, result))

result = add(100, 200)  # positional argument
print('%d + %d = %d' % (number01, number02, result))


