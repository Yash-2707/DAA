def max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]
  
    elif high == low + 1:
        return (arr[low], arr[high]) if arr[low] > arr[high] else (arr[high], arr[low])
    else:
        mid = (low + high) // 2
        max1, min1 = max_min(arr, low, mid)
        max2, min2 = max_min(arr, mid + 1, high)
        
     
        return max(max1, max2), min(min1, min2)

def find_max_min(arr):
    if not arr:
        return None, None
    return max_min(arr, 0, len(arr) - 1)

arr = [3, 6, 2, 8, 1, 9, 4, 7, 5]
max_val, min_val = find_max_min(arr)
print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")
