nums = [1,0,2,1,0]
n = len(nums)
low = 0
mid = 0
high = n-1
while mid <= high:
    if nums[mid] == 0:
        nums[low],nums[mid] = nums[mid],nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        nums[mid],nums[high] = nums[high],nums[mid]
        high -= 1
print(nums) 

'''Language: Python
1. Approach
I used Three Pointers Approachto sort the array.
We use three pointers:
- low = 0  Position for 0s.
- mid = 0  Used to traverse the array.
- high = n - 1  Position for 2s.
Steps:
- If the current element is 0, swap it with the element at low and increment both low and mid.
- If the current element is 1, increment mid.
- If the current element is 2, swap it with the element at high and decrement high.
- Continue until mid becomes greater than high.

Why does this approach work:
We divide the array into three sections:
1. Elements before low contain only 0s.
2. Elements between low and mid - 1 contain only 1s.
3. Elements after high contain only 2s.
We examine each element using the mid pointer.
1.If it is 0, move it to the beginning.
2.If it is 1, leave it in the middle.
3.If it is 2, move it to the end.
By following these steps, all 0s come first, followed by 1s and then 2s.
The algorithm sorts the original array without creating another array

Test case 1:
Input: nums = [1, 0, 2, 1, 0] Output: [0, 0, 1, 1, 2]
Test case 2:
Input: nums = [0, 0, 1, 1, 1] Output: [0, 0, 1, 1, 1]

Time Complexity	O(n)	Each element is processed at most once.
Space Complexity	O(1)	Sorting is performed in the original array without extra arrays.
'''
        