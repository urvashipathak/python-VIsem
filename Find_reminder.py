T = int(input())
while T > 0:
    A, B = map(int, input().split())
    print(A % B)
    T -= 1
