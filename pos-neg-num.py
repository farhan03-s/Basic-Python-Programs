n = int(input("Enter a positive integer: "))

sum_natural = n * (n + 1) // 2
sum_even = n * (n + 1)

sum_odd = n * n

print("Sum of first", n, "natural numbers:", sum_natural)
print("Sum of first", n, "even numbers:", sum_even)
print("Sum of first", n, "odd numbers:", sum_odd)
