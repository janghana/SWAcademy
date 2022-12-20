arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

tmp_arr = [[] for _ in range(len(arr1)+len(arr2)+3)]
for i in range(len(arr1)):
    tmp_arr[i*2] = arr1[i]
for i in range(len(arr2)):
    tmp_arr[2*i + 1] = arr2[i]

result_char = ""
for i in tmp_arr:
    if isinstance(i, list):
        continue
    result_char += str(i)+" "

print(result_char)
'''
1 3 4 9 3 1 2 8 4 8
2 9 37 1 39 4 58 60
'''