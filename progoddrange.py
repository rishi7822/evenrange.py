start = int(input("enter the start:"))
end = int(input("Enter the end:"))

for i in range(start,end +1):

    #checking
    if i % 2!=0:
        print(i,end=" ")