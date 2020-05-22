asdfasdfasfs

number = int(input('Enter a number: '))
x = range(1, number + 1)

divisor_list = []

for i in x:
    if (number % i) == 0:
        divisor_list.append(i)

print(divisor_list)
