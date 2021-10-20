def binarySearch(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

    R = len(nums) - 1
    L = 0
    if len(nums) == 1 and nums[0] == target:
        return 0
    while (R-L) > 1:

        mid = (R+L)//2
        if nums[mid] == target:
            return mid
        elif nums[R] == target:
            return R
        elif nums[L] == target:
            return L
        elif nums[mid] < target:
            L = mid
        elif nums[mid] > target:
            R = mid

    return -1


print(binarySearch([2, 5], 5))
