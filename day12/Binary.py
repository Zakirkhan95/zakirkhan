
#python program to impliment Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2 
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            high = mid - 1
        
        else:
            low = mid + 1
    
    return -1

arr = [12, 20, 12,20, 27, 34, 64, 90]
target = 20

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
