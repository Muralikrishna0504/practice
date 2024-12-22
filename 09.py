# Write a program that will take user input of cost price and selling price and determines whether
# its a loss or a profit
def profit_check(cost,sold):
    if sold-cost>0:
        return f'you got profit of {sold-cost}$'
    else:
        return f'you got loss of {cost-sold}'
# print(profit_check(100,78))
# 11.	Write a program to find the simple interest when the value of principle,rate of interest
# and time period is given.
def simple_interest(p,t,r):
    return (p*t*r)/100
# print(simple_interest(100000,12,1.5))
# 12.Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk
# is 40Rs.
def cylinder_volume(radius,height):
    volume=3.14*radius**2*height
    cost=(volume/1000)*40
    return round(volume,2),round(volume/1000,3),round(cost,2)
# milk=cylinder_volume(4,10)
# print(f'volume of cylinder is {milk[0]} and cost of {milk[1]} litres milk is {milk[2]}Rs')
# 13.Write  a program that will tell whether the given number is divisible by 3 & 6.
def myfunction(n):
    three=False
    six=False
    if n%3==0:
        three=True
    if n%6==0:
        six=True
    if three and six:
        return f'{n} is divisible by both 3 and 6'
    elif not three and six:
        return f'{n} is divisible by 6 but not 3'
    elif not six and three:
        return f'{n} is divisible by 3 but not 6'
    else:
        return f'{n} is not divisible by 3 and 6'
print(myfunction(15))


