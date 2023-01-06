N = int(input())
num_1 = N // 2
num_2 = N % 2
if num_2 != 0:
    print(4 * 5**(num_1-1)*3)
elif num_2 == 0:
    print(4 * 5**(num_1-1))
