"""
791. Custom Sort String
https://leetcode.com/problems/custom-sort-string/

order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Example:
Input: 
order = "cba"
str = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.


"""




class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ans, cnt = [], collections.Counter(T)
        
        for c in S:
            if cnt[c]: ans.extend(c * cnt.pop(c))
        for c, v in cnt.items():
            ans.extend(c * v)
        return ''.join(ans)
        

