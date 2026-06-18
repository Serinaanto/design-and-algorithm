def binary_search(arr, low, high, target):
    while low<high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, high, target)

arr=[10,20,30,40,50,60,70]
print(binary_search([10,20,30,40,50,60,70], 0, len(arr)-1, 60))