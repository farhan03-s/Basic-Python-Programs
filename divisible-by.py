num = int(input("Enter an integer: "))

if num % 5 == 0 and num % 11 == 0:
    print(num, "is divisible by both 5 and 11")
else:
    print(num, "is NOT divisible by both 5 and 11")
