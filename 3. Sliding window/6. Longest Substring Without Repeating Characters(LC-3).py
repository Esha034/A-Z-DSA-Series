class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        n=len(s)
        low,high=0,0
        freq={}
        maxlen=0
        for high in range(n):
            freq[s[high]]=freq.get(s[high],0)+1

            if len(freq)==(high-low+1):
                maxlen=max(maxlen,high-low+1)
           
            while len(freq)<(high-low+1):
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
        return maxlen 





            

        
