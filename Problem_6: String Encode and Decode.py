"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for s in strs:
            encoded += str(len(s))+"#"+s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i<len(s):
            j=s.find("#",i)
            length=int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            i=j+1+length
        return decoded



# Example usage
sol = Solution()
encoded = sol.encode(["hheyy", "world"])
print(f"Encoded: {encoded}")
decoded = sol.decode(encoded)
print(f"Decoded: {decoded}")