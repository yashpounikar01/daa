def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
                arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    element = int(input())
    arr.append(element)

# Sort the array
sorted_arr = selection_sort(arr)

# Print the sorted array
print("Sorted array:", sorted_arr)

