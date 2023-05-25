def Binary_Search(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start:end + 1])))
        step = step + 1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

element = 7
array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]

print("Searching for {} in {}".format(element, array))
print("Index of {}: {}".format(element, Binary_Search(array, element)))


def bubbleSort(arr):
    n = len(arr)

    for num in range(n - 1):
        for j in range(0, n - num - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


list = [5, 2, 8, 1, 3, 6, 9, 0, 4]
bubbleSort(list)

print(f"Bubble sort: {list}")


def selection_sort(array):
    for i in range(0, len(array) - 1):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]


list2 = [5, 2, 8, 1, 3, 6, 9, 0, 4]
selection_sort(list2)

print(f"selection sort: {list2}")