def countSwaps(a):
    count = 0
    for i in range(len(a)):
        temp = 0
        for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                count += 1
            else:
                temp += 1
                if temp == len(a) - 1:
                    print(f"Array is sorted in {count} swaps.")
                    print(f"First Element: {a[0]}")
                    print(f"Last Element: {a[len(a) - 1]}")
                    return
