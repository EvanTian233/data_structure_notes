"""
167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers
        l, r = 0, len(numbers)-1
        while l<r:
            cur_sum = numbers[l]+numbers[r]
            if cur_sum == target:
                return [l+1,r+1]
            elif cur_sum < target:
                l += 1
            else:
                r -= 1
    
    
        return [-1,-1]