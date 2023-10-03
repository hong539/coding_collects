def mergeSort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1

    while i < len(left): 
        result.append(left[i]) 
        i += 1

    while j < len(right): 
        result.append(right[j]) 
        j += 1

    return result


if __name__ == "__main__":
    nums = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print("original:", nums)
    print("Sorted:", mergeSort(nums))