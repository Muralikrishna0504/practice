# 5.Write a program that can find the factorial of a given number provided by the user.
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
# print(fact(5))
# 6.Write a program to print the first 25 odd numbers
def odd_numbers(n=1):
    print(n,end=' ')
    if n==25:
        return 25
    return odd_numbers(n+2)
# odd_numbers()
print()
# 7.Write a program to print whether a given number is prime number or not
def prime_number(n): # iterative approach
    prime=True
    for i in range(2,n//2+1):
        if n%i==0:
            prime=False
            break
    return prime
# print(prime_number(11))
#recursive_approach
# 8.Print all the armstrong numbers in the range of 100 to 1000
def armstrong_number():
    lst=[]
    for i in range(100,1001):
        sum=0
        for j in str(i):
            sum+=int(j)**3
        if sum==i:
            lst.append(i)
    return lst
print(armstrong_number())
def armstrong_recursive(lst=[],start=100):
    if start>1000:
        return lst
    sum=0
    for i in str(start):
        sum+=int(i)**3
    if sum==start:
        lst.append(start)
    return armstrong_recursive(lst,start+1)
print(armstrong_recursive())