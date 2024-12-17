# Write a program to find the euclidean distance between two coordinates.
def euclidian_distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
print(euclidian_distance(1,4,2,3))
def triangle_check(angle1,angle2,angle3):
    if angle1==0 or angle2==0 or angle3==0:
        return False
    if angle1+angle2+angle3==180:
        return True
    else:
        return False
print(triangle_check(90,70,20))
