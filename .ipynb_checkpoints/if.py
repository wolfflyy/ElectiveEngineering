a = int(input("give number here"))

if a % 2 == 0 and a % 5 == 0:
    print("FizzBuzz")
elif a % 5 == 0:
    print("Buzz")
elif a % 2 == 0:
    print("Fizz")
else:
    print("no bozo")