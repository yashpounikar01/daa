def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Find the middle point of the array
    mid = len(arr) // 2
    
    # Recursively sort the two halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    
    # Merge the arrays while both have elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # If there are remaining elements in left array
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    
    # If there are remaining elements in right array
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    
    return sorted_array

# Example usage
if __name__ == "__main__":
    n=int(input('Enter No. of elements in array:'))
    array = []
    for i in range(n):
        element=int(input())
        array.append(element)
    sorted_array = merge_sort(array)
    print(f"The sorted array is: {sorted_array}")
