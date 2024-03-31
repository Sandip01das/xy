def range_search(arr, range_min, range_max):
    result = []
    for value in arr:
        if range_min <= value <= range_max:
            result.append(value)
    return result

# Example usage:
arr = [3, 7, 1, 12, 5, 8, 9, 10]
range_min = 5
range_max = 10
print("Values in range [5, 10]:", range_search(arr, range_min, range_max))

