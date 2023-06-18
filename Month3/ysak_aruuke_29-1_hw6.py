def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def binary_search(element, lst):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == element:
            return mid
        elif lst[mid] < element:
            left = mid + 1
        else:
            right = mid - 1

    return -1


my_list = [5, 2, 9, 1, 7]

sorted_list = bubble_sort(my_list)
print(sorted_list)

index = binary_search(2, sorted_list)
print("Индекс элемента 2:", index)
