# Write a program that will swap numbers
def swap_number(n1,n2):
    n1,n2=n2,n1
    return n1,n2
n1=10
n2=20
print(swap_number(n1,n2))

# 3.	Write a program to find the sum of first n numbers, where n will be provided by the user.
# Eg if the user provides n=10 the output should be 55.
def sum_of_numbers(n):
    if n==0:
        return n
    return n+sum_of_numbers(n-1)
print(sum_of_numbers(3))
# 4.	Write a program that can multiply 2 numbers provided by the user without using the * operator
def my_mult(a,b):
    if b==0:
        return 0
    elif b<0:
        return -(a-my_mult(a,b+1))
    else:
        return a+my_mult(a,b-1)
print(my_mult(-4,2))
