# 10.Write a program to print all the unique combinations of 1,2,3 and 4
def combinations():
    lst=[]
    for i in range(1,5):
        lst.append(int(str(i) + str(i + 1)))
        lst.append(int(str(i + 1) + str(i)))
    return lst
# print(combinations())
def hcf(a,b,remainder=None):# my approach
    if remainder==0:
        return a
    if a>b:
        remainder=a%b
        return hcf(b,remainder,remainder)
# print(hcf(4,2))

def hcf1(a,b):
    if b==0:
        return a
    return hcf1(b,a%b)
print(hcf1(56,98))
def lcm(a,b):
    hcf=hcf1(a,b)
    lcm=(a*b)//hcf
    return lcm
print(lcm(12,18))
def prime_numbers():
    prime_list=[]
    for i in range(2,25):
        prime=True
        for j in range(2,i//2+1):
            if i%j==0:
                prime=False
                break
        if prime:
            prime_list.append(i)
    return prime_list
print(prime_numbers())
