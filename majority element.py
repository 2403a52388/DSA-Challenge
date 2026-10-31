nums = [7,0,0,1,7,7,2,7,7]
n = len(nums)
dici ={}
for i in range(n):
    if nums[i] not in dici:
        dici[nums[i]] = 1
    else:
        dici[nums[i]] += 1
    for key,value in dici.items():
        if value > n/2:
            print(key)
            
''''Language: Python
1. Approach
I used a dictionary to count the frequency of each element. Returned the element whose frequency is greater than n/2.
1.First, calculate the length of the array.
2.Create an empty dictionary to store the frequency of each element.
3.Traverse the array using a loop.
4.Count how many times each element appears.
5.Check whether the frequency of an element is greater than n // 2.
6.If the condition is true, return that element.

Why does this approach work:
A majority element is an element that appears more than half the size of the array.     
We use a dictionary to count the frequency of each element.
Whenever an element's frequency becomes greater than n // 2, we identify it as the majority element and print it.
Since the problem guarantees that a majority element exists, the algorithm will always find the answer.

Test case 1:
Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7] Output: 7 
Test case 2:
Input: nums = [1, 1, 1, 2, 1, 2] Output: 1
Additional edge case:
Input: nums = [5] Output: 5

Time Complexity: O(n)--We traverse the array only once.
Space Complexity: O(n)--Dictionary stores the frequency of elements.'''
            
        
