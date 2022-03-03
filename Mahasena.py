Num= int(input())
A = list(map(int, input().split()))[:N]
even = 0
odd = 0
for i in A:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
if even > odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
