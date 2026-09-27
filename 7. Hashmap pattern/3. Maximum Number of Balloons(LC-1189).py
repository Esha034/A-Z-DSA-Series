class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        n=len(text)
        freq={}

        ans=float('inf')
        need={'b':1,'a':1,'l':2,'o':2,'n':1}

        for ch in text:
            freq[ch]=freq.get(ch,0)+1
        for ch in need:
            ans=min(ans,freq.get(ch,0)//need[ch])
        return ans
        



        
