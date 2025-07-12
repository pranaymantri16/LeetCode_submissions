class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        result = ""
        num &= 0xFFFFFFFF
        
        while num != 0:
            digit = num & 0xF
            result = hex_chars[digit] + result
            num >>= 4
        
        return result
