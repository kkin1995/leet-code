class Solution:
    """
    You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

    Return the score of s.
    """

    def scoreOfString(self, s: str) -> int:
        len_s = len(s)
        sum_of_absolute_differences = 0
        for i in range(len_s - 1):
            abs_diff = abs(ord(s[i]) - ord(s[i + 1]))
            sum_of_absolute_differences += abs_diff
        return sum_of_absolute_differences
