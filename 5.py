def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Пример использования
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 8

result = binary_search(arr, target)

if result == -1:
    print("Элемент не найден")
else:
    print(f"Индекс элемента: {result}")