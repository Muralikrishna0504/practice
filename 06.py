# 1.Write a programme that will give the sum of three digits
def three_digit_sum(a):
    if a==0:
        return 0
    return a%10+three_digit_sum(a//10)
print(three_digit_sum(345))

# 2. write a programme for reversing the 4digit number and check the reverse is True
def reverse_digit(n):
    if n==0:
        return ''
    reversed=str(n%10)+str(reverse_digit(n//10))
    return reversed

print(reverse_digit(1234))
