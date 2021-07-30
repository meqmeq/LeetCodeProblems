def rob(nums):
    """
        :type nums: List[int]
        :rtype: int
        """
    if len(nums) == 1:
        return nums[0]
    arr = [0] * len(nums)

    arr[0] = nums[0]
    arr[1] = nums[1]

    for i in range(2, len(arr)):
        arr[i] = max(arr[0:i-1]) + nums[i]

    if arr[len(arr) - 1] >= arr[len(arr) - 2]:
        return arr[len(arr) - 1]
    else:
        return arr[len(arr) - 2]


print(rob([1, 2, 3, 1]))
