"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
Note:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       d = {}
       d[0] = 1
       s = 0
       count = 0
       for i in range(len(nums)):
           s += nums[i]
           if s-k in d: # --- I
               count += d[s-k]
               # or return True
               # or return indicies

           # add sum to frq dict
           if s in d:
               d[s] += 1 # --- II
           else:
               d[s] = 1

       return count


   	   # COMMENT -- I
   	   # ---------------
   	   # Single scan. Given the current sum and the k, we check if (sum-k) existed as previous sum at an earlier stage ( aka smaller window size)
   	   # Keep expanding the sum while checking whether we have seen (sum - k) before
   	
       
       
       # COMMENT -- II
       # ---------------
       # It's possible that the freq of a sum could be greater than 1 only when the nums list conatins a zero
       # ex: nums = [1,2,3,0,4]
       # because sum will be the same for two consecutive iterations.
       # it's important to capture this edge case in order to return the correct number of subarrays that
       # add up to target.
       # if we are guaranteed that the list nums has no zeros, then we can replace the prefix dict with a prefix set
       