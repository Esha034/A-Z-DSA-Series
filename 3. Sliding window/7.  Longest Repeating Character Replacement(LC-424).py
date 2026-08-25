class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n=len(s)
        low,high=0,0
        freq={}
        max_freq=0
        max_len=0
        for high in range(n):
            freq[s[high]]=freq.get(s[high],0)+1

            if freq[s[high]]>max_freq:
                max_freq=freq[s[high]]
            
            while ((high-low+1)-max_freq)>k:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
            
            if high-low+1> max_len:
                max_len=high-low+1
        return max_len
        
