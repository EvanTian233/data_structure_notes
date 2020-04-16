"""
678. Valid Parenthesis String
https://leetcode.com/problems/valid-parenthesis-string/

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:

Input: "()"
Output: True
Example 2:

Input: "(*)"
Output: True
Example 3:

Input: "(*))"
Output: True

"""

class Solution:
    def checkValidString(self, s):
            cmin = cmax = 0
            for i in s:
                if i == '(':
                    cmax += 1
                    cmin += 1
                if i == ')':
                    cmax -= 1
                    cmin = max(cmin - 1, 0)
                if i == '*':
                    cmax += 1
                    cmin = max(cmin - 1, 0)
                if cmax < 0:
                    return False
            return cmin == 0