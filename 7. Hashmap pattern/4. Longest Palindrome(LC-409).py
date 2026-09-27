class Solution:
    def longestPalindrome(self, s: str) -> int:
       
        freq={}
        
        for ch in s:
            freq[ch]=freq.get(ch,0)+1

        len=0
        has_odd=False

        for ch in freq:
            if freq[ch]%2 ==0:
                len+=freq[ch]
            else:
                len+=(freq[ch]-1)
                has_odd=True
        if has_odd:
            len+=1
        return len

        
