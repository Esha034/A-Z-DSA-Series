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
        
        n=len(s)
        low=0
        freq={}
        res=-1
        
        for high in range(n):
                 
            freq[s[high]]=freq.get(s[high],0)+1
            
            if len(freq)==k:
                res=max(res,high-low+1)
                
            while len(freq)>k:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
                
                
        return res 
    
