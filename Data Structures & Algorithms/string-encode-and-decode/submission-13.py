class Solution:

    def encode(self, strs: List[str]) -> str:  
        strs_buffer = []
        for s in strs:
            strs_buffer.append(str(len(s)))
            strs_buffer.append(",")
            strs_buffer.append(s) 

        combined_strs = "".join(strs_buffer)
        return combined_strs

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        next_str_chars_len = 0

        while i < len(s):
            if s[i] != ",":
                next_str_chars_len += 1
                i += 1
            else:
                next_str_len = int(s[i - next_str_chars_len : i])
                strs.append(s[i + 1 : i + 1 + next_str_len])
                i += next_str_len + 1
                next_str_chars_len = 0

        return strs

