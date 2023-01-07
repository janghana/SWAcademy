arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []
cnt = abs(len(arr1) - len(arr2))

if len(arr1) > len(arr2):
    for i in range(len(arr2)):
        result.append(arr1[i])
        result.append(arr2[i])
    result.extend(arr1[len(arr2):])

elif len(arr1) <= len(arr2):
    for i in range(len(arr1)):
        result.append(arr1[i])
        result.append(arr2[i])
    result.extend(arr2[len(arr1):])
print(*result)
