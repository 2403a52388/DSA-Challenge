nums = [2, 3, 5, -2, 7, -4]
current_sum = nums[0]
max_sum = nums[0]
for i in range(1, len(nums)):
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(max_sum, current_sum)
print(max_sum)

'''Language: Python
1. Approach
I used Kadane's Algorithm to find the maximum sum of a contiguous subarray.
1.First, initialize two variables: current_sum and max_sum with the first element of the array.
2.Traverse the array from the second element.
3.Add the current element to current_sum.
4.If starting a new subarray with the current element gives a larger sum, update current_sum.
5.Update max_sum whenever current_sum becomes greater than max_sum.
6.Finally, return max_sum.

Why does this approach work:
Kadane's Algorithm works by checking whether it is better to:
- Continue the existing subarray by adding the current element.
- Start a new subarray from the current element.
We choose whichever gives the larger sum.We also update max_sum whenever we find a larger subarray sum.
This ensures that we find the maximum sum of a non-empty contiguous subarray.

Test case 1:
Input: nums = [2, 3, 5, -2, 7, -4] Output: 15
Test case 2:
Input: nums = [-2, -3, -7, -2, -10, -4] Output: -2

Time Complexity	O(n)	We traverse the array only once.
Space Complexity	O(1)	We use only two extra variables.'''
