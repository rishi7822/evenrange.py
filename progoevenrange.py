start = int(input("enter the range: "))
end = int(input("enter the end:"))

for i in range(start,end+1):
    
    #checking even
    if i %2 == 0:
        print(i,end = " ")