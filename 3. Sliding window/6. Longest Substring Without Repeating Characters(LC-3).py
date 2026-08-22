#my code
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


#optimal code

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        low = 0
        max_len = 0

        for high in range(len(s)):

            if s[high] in last_seen:
                if last_seen[s[high]] >= low:
                    low = last_seen[s[high]] + 1

            last_seen[s[high]] = high

            length = high - low + 1

            if length > max_len:
                max_len = length

        return max_len





            

        
