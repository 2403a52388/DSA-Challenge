nums = [2,4,5,-1,-3,-4]
n = len(nums)
result = [0]*n
pos = 0
neg = 1
for i in range(n):
    if nums[i] > 0:
        result[pos] = nums[i]
        pos += 2
    else:
        result[neg] = nums[i]
        neg += 2
print(result) 

nums = [1, -1, -3, -4, 2, 3]
n = len(nums)
result = [0]*n
pos = 0
neg = 1
for i in range(n):
    if nums[i] > 0:
        result[pos] = nums[i]
        pos += 2
    else:
        result[neg] = nums[i]
        neg += 2
print(result)

'''Language: Python
1. Approach
I used the Two Pointers / Indexing Approach to rearrange the positive and negative elements.
1.First, create a new empty array of the same size as the input array.
2.Initialize two index positions:
   pos = 0 for positive elements.
   neg = 1 for negative elements.
3.Traverse the original array using a loop.
4.If the current element is positive, place it at the positive index and increase pos by 2.
5.If the current element is negative, place it at the negative index and increase neg by 2.
6.Finally, print the rearranged array.

Why does this approach work:
We use separate index positions for positive and negative elements.
1.Even indexes (0, 2, 4...) store positive elements.
2.Odd indexes (1, 3, 5...) store negative elements.
Since we traverse the original array from left to right, the relative order of positive elements and negative elements is maintained.
so, the resulting array starts with a positive element and alternates between positive and negative elements.
Test case 1:
Input: nums = [2, 4, 5, -1, -3, -4] Output: [2, -1, 4, -3, 5, -4] 
Test case 2:
Input: nums = [1, -1, -3, -4, 2, 3] Output: [1, -1, 2, -3, 3, -4]
Additional edge case:
nums = [5, -2] Output: [5, -2]

Time Complexity: O(n)--We traverse the input array once.
Space Complexity: O(n)--We create a new array of size n'''
