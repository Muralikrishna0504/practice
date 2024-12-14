# Given a number n.The number n can be positive or negative.if n is negative then print numbers from
# n to 0 by adding 1 to it. if number is positive then print numbers from n-1 to 0 by subracting 1 from it.
# if n is 0 then return already a Zero
def myfun(n):
    if n<0:
        while n<1:
            print(n,end=' ')
            n=n+1
        print()
    elif n>0:
        while n>-1:
            print(n,end=' ')
            n=n-1
        print()
    else:
        print('already a Zero')
myfun(10)
myfun(-10)
myfun(0)
