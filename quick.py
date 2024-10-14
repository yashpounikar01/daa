def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        
        # Recursively apply quick_sort to the sub-arrays
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # Choose the pivot element, here we choose the last element in the array
    pivot = arr[high]
    i = low - 1
    
    # Rearrange the array by placing elements less than the pivot before the pivot
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place the pivot element in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    sample_array = []
    for i in range(n):
        element = int(input())
        sample_array.append(element)
    print("Original array:", sample_array)
    quick_sort(sample_array, 0, len(sample_array) - 1)
    print("Sorted array:", sample_array)
