#My code

class Solution:
    def longestKSubstr(self, s, k):
        
        n=len(s)
        low,high=0,0
        freq={}
        res=-1
        
        for high in range(n):
                 
            if s[high] in freq:
                freq[s[high]]+=1
            else:
                freq[s[high]]=1
                    
                    
            if len(freq)==k:
                res=max(res,high-low+1)
                
            while len(freq)>k:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
                
        return res 


#optimal code

class Solution:
    def longestKSubstr(self, s, k):

        n = len(s)
        low = 0
        freq = {}
        res = -1

        for high in range(n):

            # Add incoming character
            if s[high] in freq:
                freq[s[high]] += 1
            else:
                freq[s[high]] = 1

            # Shrink if distinct characters exceed k
            while len(freq) > k:
                freq[s[low]] -= 1

                if freq[s[low]] == 0:
                    del freq[s[low]]

                low += 1

            # Window has exactly k distinct characters
            if len(freq) == k:
                length = high - low + 1

                if length > res:
                    res = length

        return res


Complexity:

Time: O(n) — each character enters and leaves the window at most once.
Space: O(k) — frequency map stores at most k distinct characters after shrinking.
