#WPP to print patter #pattern19
n=int(input("Enter number of rows: "))
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(j+1,end=" ")
    print()