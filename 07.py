# Write a program that will tell whether the number entered by the user is odd or even.
def odd_or_even(n):
    if n&1==1:
        return 'odd'
    else:
        return 'even'
# print(odd_or_even(13))

# Write a program that will tell whether the given year is a leap year or not.
def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
# print(leap_year(1964))

#recursion approach:
def leap_year_check(year,check=0):
    if check==0:
        if year%4==0:
            return leap_year_check(year,1)
        else:
            return False
    if check==1:
        if year%100==0:
            return leap_year_check(year,check=2)
        else:
            return True
    if check==2:
        if year%400==0:
            return True
        else:
            return False

print(leap_year_check(1985))

