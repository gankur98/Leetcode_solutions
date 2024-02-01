'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # The sorted() function returns a sorted list of the specified iterable object.
        sortedS = sorted(s)
        sortedT = sorted(t)

        return sortedS == sortedT