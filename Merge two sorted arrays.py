nums1 = [-5, -2, 4, 5, 0, 0, 0]
nums2 = [-3, 1, 8]
m = 4
n = 3
i = m - 1
j = n - 1
k = m + n - 1
while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1
print(nums1)

'''Language: Python
1. Approach
I used the Three Pointers Approach (Merging from the End) to merge two sorted arrays without using extra space.
We use three pointers:
i = m - 1 Points to the last valid element of nums1.
j = n - 1 Points to the last element of nums2.
k = m + n - 1 Points to the last position of nums1.
Steps:
1.Compare the elements at nums1[i] and nums2[j].
2.Place the larger element at position k in nums1.
3.Decrease the corresponding pointer.
4.Decrease k after every insertion.
5.Continue until all elements of nums2 are inserted into nums1.

Why does this approach work:
Both arrays are already sorted in ascending order.
We start comparing elements from the end of both arrays because the largest element should be placed at the last position.
1.If the element in nums1 is larger, place it at the end of nums1.
2.Otherwise, place the element from nums2 at the end.
3.Continue comparing and placing elements until all elements are merged.
We start from the end to avoid overwriting the valid elements already present in nums1.
so, the final array will be sorted in ascending order without creating another array

Test case 1:
Input: nums1 = [-5, -2, 4, 5, 0, 0, 0]; nums2 = [-3, 1, 8] Output: [-5, -3, -2, 1, 4, 5, 8]
Test case 2: 
Input: nums1 = [0, 2, 7, 8, 0, 0, 0]; nums2 = [-7, -3, -1] Output: [-7, -3, -1, 0, 2, 7, 8]
Time Complexity	O(m + n)	Each element is processed at most once.
Space Complexity	O(1)	No additional array is created.'''
