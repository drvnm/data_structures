# binary search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        print(left, right, mid, arr[mid])
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:

            right = mid - 1
        else:
            left = mid + 1

    return -1


# print(binary_search([i for i in range(12)], 11))


def linear_search(arr, target):
    index = 0
    for i in arr:
        if arr[index] == target:
            return index, True
        index += 1
    return False


# lin = [i for i in range(12)]
# print(lin)
# print(linear_search(lin, 11))


# bubble sort
def bubble_sort(arr):
    sorted = True
    while sorted:
        sorted = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                temp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = temp
                sorted = True

    return arr


# print(bubble_sort([1, -4, 6, -4]))

# selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_pos = i
        for j in range(i, len(arr)):
            if arr[min_pos] > arr[j]:
                min_pos = j
        temp = arr[i]
        arr[i] = arr[min_pos]
        arr[min_pos] = temp
    return arr


print(selection_sort([0, 1, 0, 4, 2]))
