# Given two integers a and b and a boolean variable flag.The task is to check the status and return accordingly
# return True: if a or b ->either one is non-negative and falg is false and if both a and b is non negative
# and flag is true then also return false.
# otherwise return False
def check_status(a,b,flag):
    if ((a>=0 or b>=0) and flag==False) or (a<0 and b<0 and flag==True):
        return True
    else:
        return False
c=check_status(-1,-1,True)
c1=check_status(1,1,True)
c2=check_status(-1,1,True)
c3=check_status(1,-1,True)
c4=check_status(-1,-1,False)
c5=check_status(1,1,False)
c6=check_status(-1,1,False)
c7=check_status(1,-1,False)
print('c:',c)
print('c1:',c1)
print('c2:',c2)
print('c3:',c3)
print('c4:',c4)
print('c5:',c5)
print('c6:',c6)
print('c7:',c7)

