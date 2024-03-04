def find_mn_sum_diff(nums, m, n):
    if m <= 0 or n <= 0 or m > len(nums) or n > len(nums):
        return "Invalid input"
    nums.sort()
    nth_min = nums[n-1]
    mth_max = nums[m-1]
    sum_mn = nth_min + mth_max
    diff_mn = nth_min - mth_max
    return mth_max, nth_min, sum_mn, diff_mn
nums = [1, 5, 2, 8, 3, 9, 4, 7, 6]
m, n = 3, 5
print(find_mn_sum_diff(nums, m, n))
