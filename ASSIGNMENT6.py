#Q.1-Create a function to calculate the area of a sphere by taking radius from user.
def area(r):
    area=4*(3.14)*r*r
    return(area)
r=int(input("enter radius"))
print(area(r))

#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. [An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number.
def perfect(a,b):
    for i in range(a,b):
        sum=0
        for j in range(1,i):
            if (i%j==0):
                sum=sum+j
        if (sum==i):
            print(i,end=' ')

perfect(1,1000)
print()

#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
def multiply(num):
    for i in range(1,11):
        print(num, "*", i, "=", (num* i))

num=int(input("enter ur number"))
multiply(num)


#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def power(a,b):
    if b == 1:
        return a
    else:
        return a*power(a,b-1)

a = int(input("enter number"))
b = int(input("enter power of that number"))
print(power(a,b))
