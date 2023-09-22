def BubbleSort(arr):
    n = len(arr)
    swap = False
    for x in range(n-1):
        for y in range (0, n-x-1):
            if arr[y] > arr[y+1]:
                swap = True
                arr[y], arr[y+1] = arr[y+1], arr[y]
        if not swap:
            return

arr = [43, 87, 45, 36, 90, 28]

BubbleSort(arr)

print("The new array is:")
print(arr)