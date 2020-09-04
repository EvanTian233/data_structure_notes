"""
763. Partition Labels
https://leetcode.com/problems/partition-labels/

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

"""


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        right_most = {c: i for i, c in enumerate(S)}
        left, right = 0, 0
        
        result = []
        for i, letter in enumerate(S):
            
            right = max(right, rightmost[letter])
            
            if i == right:
                result += [right-left+1]
                left = i+1
                
        return result
                
            