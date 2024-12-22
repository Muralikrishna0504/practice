# Write a program that will tell the number of dogs and chicken are there when the user will
# provide the value of total heads and legs.
def myfun(heads,legs):
    dogs=(legs-2*heads)//2
    chickens=heads-dogs
    return f'dogs:{dogs} and chickens:{chickens}'

print(myfun(2,6))

