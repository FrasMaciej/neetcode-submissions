class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty"   
        strs_buffer = []

        for s in strs:
            strs_buffer.append(str(len(s)))
            strs_buffer.append(",")
            strs_buffer.append(s) 

        print(strs_buffer)
        combined_strs = "".join(strs_buffer)
        return combined_strs

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []

        strs_len = []
        strs = []
        i = 0
        next_str_len = 0
        cur = ""
        while i < len(s):
            if s[i] != ",":
                cur += s[i]
                i += 1
            else:
                next_str_len = int(cur)
                if next_str_len != 0:
                    strs.append(s[i + 1 : i + 1 + next_str_len])
                else: 
                    strs.append("")
                i += next_str_len + 1
                cur = ""

        return strs
        # Problem: how to encode list of strs so it can be correctly decoded?
        # Idea: count len of each string. And what next?
        # add some delimeter? so I know how many characters to consider?
        # for: ["Hello", "World"] it would be:
        # 5,Hello,5,World
        # for: [",,3,4", "111,"] it would be: -> seems to be fine for any ASCII character
        # 5,,,3,4,4,111,,

        # What for Input: strs = ["Hello", "", "", "", "World"] ??
        # "5,Hello,0,0,0,5,World"

