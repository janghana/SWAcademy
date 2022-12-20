input()
p_l = list(map(int ,input().split()))
input()
l_l = list(map(int, input().split()))

result = []
for i in p_l:
    max_val = 10000
    for j in l_l:
        if max_val > abs(i-j):
            max_val = abs(i-j)
    result.append(max_val)

result.sort()
print(result[-1])

