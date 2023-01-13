import math
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    if a * b == a * b / math.gcd(a, b):
        print("Perfect")
    else:
        print("Not even close")
