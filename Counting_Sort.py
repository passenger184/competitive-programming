def countingSort(arr):
    resu = [0] * 100
    for i in range(len(arr)):
        resu[arr[i]] += 1
        
    return resu
