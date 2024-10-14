def min_max(arr, left, right):
    # Base case: when the subarray has only one element
    if left == right:
        return arr[left], arr[left]
    # Base case: when the subarray has two elements
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    
    # Find the middle index of the array
    mid = (left + right) // 2
    
    # Recursively find the min and max in the left and right halves
    min_left, max_left = min_max(arr, left, mid)
    min_right, max_right = min_max(arr, mid + 1, right)
    
    # Combine the results
    final_min = min(min_left, min_right)
    final_max = max(max_left, max_right)
    
    return final_min, final_max

def find_min_max(arr):
    if not arr:
        raise ValueError("Array is empty")
    return min_max(arr, 0, len(arr) - 1)

# Example usage
if __name__ == "__main__":
    n=int(input('Enter No. of eleements in array:'))
    array =[]
    for i in range(n):
        element=int(input())
        array.append(element)
    min_val, max_val = find_min_max(array)
    print(f"The minimum element in the array is: {min_val}")
    print(f"The maximum element in the array is: {max_val}")
