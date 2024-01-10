for i in range(1,100+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        i = i + 1
    elif i % 3 == 0:
        print("Fizz")
        i = i + 1
    elif i % 5 == 0:
        print("Buzz")
        i = i + 1
    else:
        print(i)
    