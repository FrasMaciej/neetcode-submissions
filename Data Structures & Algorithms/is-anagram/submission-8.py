class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        if len(dict1) != len(dict2):
            return false
        for i in s:
            if i in dict1.keys(): 
                dict1[i] = dict1[i] + 1
            else:
                dict1[i] = 1
        for i in t:
            if i in dict2.keys(): 
                dict2[i] = dict2[i] + 1
            else:
                dict2[i] = 1
        return dict1 == dict2

        