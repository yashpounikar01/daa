def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Predefined sorted array
array = [10, 15, 23, 45, 70, 85]
print(array)
# Taking input from user
target = int(input("Enter the target element to search for: "))

# Performing binary search
result = binary_search(array, target)

# Displaying the result
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")
