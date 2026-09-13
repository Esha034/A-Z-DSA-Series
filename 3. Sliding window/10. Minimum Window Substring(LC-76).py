#optimal solution-using freq map
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq = {}

        # Store required frequency of characters in t
        for ch in t:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        low = 0
        required = len(t)

        min_len = float("inf")
        start = 0

        for high in range(len(s)):

            # If s[high] is still required
            if s[high] in freq and freq[s[high]] > 0:
                required -= 1

            # Decrease frequency
            if s[high] in freq:
                freq[s[high]] -= 1

            # Window is valid
            while required == 0:

                curr_len = high - low + 1

                # Update minimum window
                if curr_len < min_len:
                    min_len = curr_len
                    start = low

                # Remove left character
                if s[low] in freq:
                    freq[s[low]] += 1

                    # We removed a required character
                    if freq[s[low]] > 0:
                        required += 1

                low += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]









#Optimal Solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m=len(s)
        n=len(t)

        if m<n:
            return ""
            
        # Frequency of characters required from t
        freq=[0]*128

        for ch in t:
            freq[ord(ch)]+=1

        low=0
        start=0
        required=n
        minlen=float("inf")

        for high in range(m):

            index=ord(s[high])

            if freq[index]>0:
                required-=1

            freq[index]-=1

            while required==0:

                currlen=high-low+1

                if currlen < minlen:
                    minlen = currlen
                    start = low
                # Remove s[low]
                index=ord(s[low])
                freq[index]+=1

                if freq[index]>0:
                    required+=1

                low+=1

        if minlen==float("inf"):
            return ""

        return s[start:start+minlen]


Complexity:

Time: O(m + n)
Building frequency: O(n)
Scanning s:O(m)
Where, Each character enters and leaves the window at most once.


Space: O(1)
The frequency array has fixed size 128:

        



        
