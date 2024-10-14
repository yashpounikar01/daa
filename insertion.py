def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr  # Return the sorted array

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    element = int(input())
    arr.append(element)

# Sort the array
sorted_arr = insertion_sort(arr)

# Print the sorted array
print("Sorted array:", sorted_arr)
