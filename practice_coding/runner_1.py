runner_list_1 = list(map(str,input().split()))
runner_list_2 = list(map(str,input().split()))

runner_list = []

for i in runner_list_1:
    runner_list.append(i)
for i in runner_list_2:
    if i in runner_list:
        runner_list.remove(i)
print(runner_list[0])

