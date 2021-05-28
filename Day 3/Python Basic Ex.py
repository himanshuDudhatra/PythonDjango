#q-1
print("1. Calculate average of 5 numbers.")
q = int(input("enter the first number "))
q1 = int(input("enter the second number "))
q2 = int(input("enter the third number "))
q3 = int(input("enter the forth number "))
q4 = int(input("enter the fifth number "))
avg = q+q1+q2+q3+q4
print(avg/5)

#q-2
print("\n")
print("2. Check whether number is even or odd.")
oddEven = int(input("enter your number "))
if((oddEven % 2) ==0):
    print("even")
else:
    print("odd")

#q-3
print("\n")
print("3. Take a year and check whether it is leap year or not")
year = int(input("enter year "))
if(( year % 4 ) == 0):
    if(( year % 100 ) == 0):
        if(( year % 400 ) == 0):
            print(year,(" is a leap year"))
        else:
             print(year,(" is not a leap year"))
    else:
         print(year,(" is a leap year"))
else:
     print(year,(" is not a leap year"))

#q-4
print("\n")
print("4. Take a number and check whether it is zero, positive or negative.")
numberNZP = int(input("enter a number "))
if(numberNZP > 0):
    print("number is positive")
elif (numberNZP < 0):
    print("number is nagitive")
else:
    print("number is zero")

#q-5
print("\n")
print("5. Take 2 numbers and display greatest number. (Also check equal number condition)")
n1 = int(input("enter a number1:"))
n2 = int(input("enter a number2:"))
if(n1 == n2):
    print("number is equal")
else:
   print(max(n1,n2),"is greater")

#q-6
print("\n")
print("6. Take a number and find factorial of that number.")
num = int(input("enter the number"))
i = 1
fact = 1
while num >= i:
    fact = fact*i
    i = i + 1

print("factorial of ",num,"is ",fact)

#q-7
print("\n")
print("7. Write a program to swap 2 numbers using third variable.")
s1 = int(input("first number "))
s2 = int(input("second number "))
print("before swap")
print(s1,s2)
temp = s1
s1=s2
s2=temp
print("after swap")
print(s1,s2)

#q-8
print("\n")
print("8. Take 2 numbers and find smallest number.")
n1 = int(input("enter number "))
n2 = int(input("enter number "))
print(min(n1,n2)," is smallest")

#q-9
print("\n")
print("9. Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.")
num = int(input("enter the number"))
if(num < 100):
    if((num % 2) ==0):
        print("even")
    else:
        print("odd")
else:
    print("your number is grater then 100")

#q-10
print("\n")
print("10. Take a number to print the square of a number if it is less than 10.")
num = int(input("enter the number"))
if(num < 10):
    print("number square is ",num * num)
else:
    print("enter number is grater then 10")

#q-11
print("\n")
print("11. Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .")
numberNZP = int(input("enter a number "))
if(numberNZP >= 0):
    if (numberNZP == 0):
        print("number is zero")
    else:
        print("number is positive")
else:
    print("number is nagitive")

#q-12
print("\n")
print("12. Take 3 numbers and find greatest number using nested IF….ELSE statement.")
n1 = int(input("enter 1 number"))
n2 = int(input("entter 2 number"))
n3 = int(input("entter 3 number"))
if(n1>n2):
    if(n1>n3):
        print(n1," is greatest")
    else:
        print(n3," is greatest")
else:
    if(n2>n3):
        print(n2," is greatest")
    else:
        print(n3," is greatest")

#q-13
print("\n")
print("13. Take 3 numbers and find smallest number using logical operator.")
a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number : '))
smallest = 0
if a < b and a < c :
    smallest = a
elif b < c : 
    smallest = b 
else : smallest = c
print(smallest, "is the smallest of three numbers.")

#q-14
print("\n")
print("14. Write a program to swap 2 numbers without taking third variable.")
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("first number is",a,"second number is",b)
a=a+b
b=a-b
a=a-b
print("swap")
print("first number is",a,"second number is",b)

#q-15
print("\n")
print("15. Take starting number and ending number from the user and print following series.")
q2= int(input("Enter starting number:"))
q1= int(input("Enter ending number:"))
for i in range(q2,q1-3,-3):
    print(i)