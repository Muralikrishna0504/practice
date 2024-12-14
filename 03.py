# Three ages will be given as input then find the oldest one
def age_check(a,b,c):
    older=a if c<a>=b else b if a<b>=c else c if b<c>=a else 'All are at the same age'
    return older
print(age_check(40,50,40))