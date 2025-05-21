
def binary_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

def find_row_by_last_element(matrix, target):
        low, high = 0, len(matrix) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][-1] >= target:
                result = mid  
                high = mid - 1
            else:
                low = mid + 1
        return result

def check(matrix,target):
    row = find_row_by_last_element(matrix, target)
    if row == -1:
        return False
    return binary_search(matrix[row], target)
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(check(matrix,target))