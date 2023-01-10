N = int(input())

for _ in range(N):
    num, K_or_M = map(str, input().split())
    if K_or_M == 'K':
        if len(str(round(0.6300 * int(num),2)).split('.')[1]) == 1:
            print(str(round(0.6300 * int(num),2)).split('.')[0] + '.'+str(round(0.6300 * int(num),2)).split('.')[1])
        elif len(str(round(0.6300 * int(num),2)).split('.')[1]) >= 2:
            print(str(round(0.6300 * int(num),2)).split('.')[0] + '.'+str(round(0.6300 * int(num),2)).split('.')[1])
        else:
            print(round(0.6300 * int(num),1))
    else:
        if len(str(round(1.6 * int(num),2)).split('.')[1]) == 1:
            print(str(round(1.6 * int(num),2)).split('.')[0] + '.'+str(round(1.6 * int(num),2)).split('.')[1])
        elif len(str(round(1.6 * int(num),2)).split('.')[1]) >= 2:
            print(str(round(1.6 * int(num),2)).split('.')[0] + '.'+str(round(1.6 * int(num),2)).split('.')[1])
        else:
            print(round(1.6 * int(num),1))