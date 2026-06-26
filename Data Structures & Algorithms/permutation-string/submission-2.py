class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        substr_dict = {}
        window_dict = {}
        l = 0

        for i in range(len(s1)):
            substr_dict[s1[i]] = substr_dict.get(s1[i], 0) + 1
            window_dict[s2[i]] = window_dict.get(s2[i], 0) + 1

        if substr_dict == window_dict:
            return True

        for r in range(len(s1), len(s2)):
            window_dict[s2[l]] = window_dict.get(s2[l], 0) - 1
            window_dict[s2[r]] = window_dict.get(s2[r], 0) + 1
            if window_dict[s2[l]] == 0:
                del window_dict[s2[l]]

            if substr_dict == window_dict:
                return True 

            l += 1

        return False

        # Input
        # s1 and s2 are lowercase letters only

        # Return
        # True -> s2 has a permutation of s1 (When permutation of s1 exists as a substring of s2)
        # False -> s2 does not have a permutation of s1

        # Edge case:
        # len(s1) > len(s2)

        # Time complexity boundaries:
        # BF: O(m*n) 

        # Improvements:
        # use set to track number of characters in current window