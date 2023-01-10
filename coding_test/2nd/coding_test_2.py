num_list = list(map(int, input().split()))
target = []
for i in range(1,len(num_list)):
    num_list.sort()
    target.append(num_list[i] + num_list[i-1])
    num_list[i] = num_list[i] + num_list[i-1]
print(sum(target))
