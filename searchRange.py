def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = [-1, -1]
    result[0] = findStartingIndex(nums, target)
    result[1] = findEndingIndex(nums, target)
    return result


def findStartingIndex(nums, target):
    index = -1
    L, R = 0, len(nums) - 1

    while L <= R:
        mid = L + (R-L)//2
        if nums[mid] == target:
            index = mid
            R = mid - 1
        elif nums[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    return index


def findEndingIndex(nums, target):
    index = -1
    L, R = 0, len(nums) - 1

    while L <= R:
        mid = L + (R-L)//2
        if nums[mid] == target:
            index = mid
            L = mid + 1
        elif nums[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    return index


print(searchRange([5, 7, 7, 8, 8, 10], 7))
print(searchRange([5], 5))
