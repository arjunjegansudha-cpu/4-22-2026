a=int(input("Enter cyclist speed for a:"))
b=int(input("Enter cyclist speed for b:"))
c=int(input("Enter cyclist speed for c:"))
avg=(a+b+c)/3
print("Average speed:", avg)

if avg>a and avg>b and avg>c:
    print("Average: %d is higher than all cyclist %d,%d,%d" %(avg,a,b,c))
    
elif avg>a and avg>b:
    print("Average: %d is higher than cyclist a:%d and, b:%d" %(avg,a,b))
elif avg>a and avg>c:
    print("Average: %d is higher than a:%d, c:%d" %(avg,a,c))
elif avg>b and avg>c:
    print("Average: %d is higher than b:%d, c:%d" %(avg,b,c))
    
elif avg>a:
    print("Average: %d is just higher than a:%d" %(avg,a))
elif avg>b:
    print("Average: %d is just higher than b:%d" %(avg,b))
elif avg>c:
    print("Average: %d is just higher than c:%d" %(avg,c))
else:
    print("Invalid input")