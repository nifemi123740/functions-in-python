def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def divide(a,b):
    if b==0:
        print("Zero division error")
    else:
        return a / b

while True:
    print(f"1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
    choice=input("Enter your choice: ")
    if choice == '1':
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        result=add(a,b)
        print(f"The result is: {result}")
    elif choice == '2':
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        result=sub(a,b)
        print(f"The result is: {result}")
    elif choice == '3':
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        result=mult(a,b)
        print(f"The result is: {result}")
    elif choice == '4':
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        result=divide(a,b)
        print(f"The result is: {result}")
    elif choice=='5':
        print("Thank you and welcome again")
        break
    else:
        print("Enter a valid input")