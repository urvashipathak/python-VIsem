n= int(input("Enter n "))
m=int(input("Enter m "))

print()
for i in range(1,n):
    if (i%m==0):
        print(i,end=" and ")
        if(i%2==0):
            print("Number is Even")
        else:
            print("Number is Odd")
