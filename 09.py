# Write a program that will take user input of cost price and selling price and determines whether
# its a loss or a profit
def profit_check(cost,sold):
    if sold-cost>0:
        return f'you got profit of {sold-cost}$'
    else:
        return f'you got loss of {cost-sold}'
print(profit_check(100,78))