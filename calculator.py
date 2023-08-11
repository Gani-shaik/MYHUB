print("Mini Caculator")
num1=float(input("Enter first number = "))
num2=float(input("Enter second number = "))
print("Press 1 for add")
print("Press 2 for sub")
print("Press 3 for mul")
print("Press 4 for div")
choice = int(input("Enter your choice from 1-4 = "))
if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(njum1-num2)
elif choice == 3:
    print(num1*num2)
elif choice == 4:
    print(num1/num2)
else:
    print("unknown number")        