N = int(input())
while N > 0:
    a, b, c = map(int, input().split())
    if (a <= b and a >= c) or (a <= c and a >= b):
        print(a)
    elif (b <= a and b >= c) or (b <= c and b >= a):
        print(b)
    elif (c <= a and c >= b) or (c <= b and c >= a):
        print(c)
    N -= 1
