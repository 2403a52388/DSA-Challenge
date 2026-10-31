nums = [1,2,5,3,1,2]
n = len(nums)
for i in range(n):
    count = 0
    for j in range(i+1,n):
        if nums[i] >nums[j]:
            count += 1
    if count == n-i-1:
        print(nums[i])
        
'''Language: Python
1. Approach
I used the Nested Loop Approach to find the leader elements in an array.
1.First, traverse the array using the outer loop.
2.For each element, compare it with all the elements on its right side using the inner loop.
3.If the current element is greater than every element on its right, it is a leader.
4.Print the leader element.
5.The last element is always a leader because there are no elements on its right.

Why does this approach work:
For every element, we check all the elements present on its right side.
If the current element is greater than all the right-side elements, the count will be equal to the total number of elements on its right.
so the element is identified as a leader.

Test case 1:
Input: nums = [1, 2, 5, 3, 1, 2] Output: [5, 3, 2] 
Test case 2:
Input: nums = [-3, 4, 5, 1, -4, -5] Output: [5, 1, -4, -5] 
Additional edge case:
Input: nums = [5]
Expected output: [5]

Time Complexity: O(n²)--Two nested loops are used.
Space Complexity: O(1)--Only a few extra variables are used.'''
    