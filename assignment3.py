'''
#1write a program to print the first 10 number
num = int(input("enter the number:"))
for num in range(1,11):
    print(num)

#2write a program to print the first 100 number
num1 = int(input("enter the number:"))
for num1 in range(1,101):
    print(num1)

#3write a program to print the first ten , 3 digit numbers
num2 = int(input("enter the 3 digit numbers:")) 
for num2 in range(100,111): 
    print(num2)

#4write a program to print even number 1-100
even_num = int(input("enter the 1-100 number to print even numbers:"))
for even_num in range(1,101):
    if even_num%2==0:
        print("print even numbers:",even_num)
    else:
        print(end="")

#5write a program to print odd numbers
odd_num = int(input("enter the 1-50 number to print odd numbers:"))
for odd_num in range(1,51):
    if odd_num%2==0:
        print(end=" ")
    else:
        print("print odd no:", odd_num)

#6write a program to print reverse from 100-1
n = int(input("enter the number:"))
for n in range(100,0,-1):
    print(n,end=" ")

#7write a program to print a table of 12
num = int(input("enter the number:"))
for num in range(1,11):
    result = 12 * num
    print(result)

#8write a program to print a table of 12 in reverse order
num = int(input("enter the number:"))
for num in range(10,0,-1):
    result = 12 * num
    print(result)

#9write a program to print the sum of the first 10 numbers
result=int(input("enter the numbers:"))
for i in range(1,11):
    result +=i
    print(result)
'''
#10write a program to print the product of the first 10 numbers 
product=int(input("enter the number:"))
for i in range(1,11):
    product *= i
    print(product)

