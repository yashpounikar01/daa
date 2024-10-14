def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

# Predefined array
array = [10, 23, 45, 70, 11, 15]
print(array)

# Taking input from user
target = int(input("Enter the target element to search for: "))

# Performing linear search
result = linear_search(array, target)

# Displaying the result
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")
