def linear_search(arr, target):
    for idx, value in enumerate(arr):
        if value == target:
            return idx
    return -1

print(linear_search([10, 20, 30, 40, 50], 40))