"""
844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

"""

class BackspaceCompare:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # Use a stack
        def buildString(S):
            ans = []
            for c in S:
                if c!= '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return buildString(S) == buildString(T)

    
    