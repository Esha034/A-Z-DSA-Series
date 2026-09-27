class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n=len(ransomNote)
        m=len(magazine)
        need={}
        have={}
        
        for ch in ransomNote:
            need[ch]=need.get(ch,0)+1
        for ch in magazine:
            have[ch]=have.get(ch,0)+1
        for ch in need:
            if need[ch]>have.get(ch,0):
                return False
        return True
                
        
        
