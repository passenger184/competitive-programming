def insertionSort1(n, arr):
    temp = arr[-1]
    for i in range(n):
        if temp < arr[n - 2 -i]:
            arr[n - 1 - i] = arr[n - 2 -i]
            if i == n - 1:
                arr[n - 1 - i] = temp
                print(' '.join(map(str, arr)))
                break
            print(' '.join(map(str, arr)))
        else:
            arr[n - 1 - i] = temp
            print(' '.join(map(str, arr)))
            break    
