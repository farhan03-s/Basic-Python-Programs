num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter your choice: "))
if choice==1:
    print("Addition of two numbers:",num1+num2)
elif choice==2:
    print("Subtraction of two numbers:",num1-num2)
elif choice==3:
    print("Multiplication of two numbers:",num1*num2)
elif choice==4:
    print("Division of two numbers:",num1/num2)
else:
    print("Invalid choice")
