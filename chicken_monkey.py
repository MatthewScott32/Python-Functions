numbers = range(101)

for n in numbers:
    
    if n % 5 == 0 and n % 7 == 0:
        print(n, 'chickenmonkey')

    elif n % 5 == 0:
        print(n, 'chicken')

    elif n % 7 == 0:
        print(n, 'monkey')

    else:
        print(n)