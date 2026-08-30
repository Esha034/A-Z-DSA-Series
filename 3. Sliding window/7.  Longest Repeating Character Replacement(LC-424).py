1. Brute Force — O(n² × 26) → effectively O(n²)

For every possible substring, count its characters and determine how many replacements are required.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            freq = {}

            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1

                max_freq = 0

                for char in freq:
                    if freq[char] > max_freq:
                        max_freq = freq[char]

                window_len = j - i + 1
                replacements = window_len - max_freq

                if replacements <= k:
                    if window_len > max_len:
                        max_len = window_len

        return max_len
Intuition:

I generate every possible substring, maintain its character frequencies, and find the most frequent character. 
The remaining characters need to be replaced, so if window_length - max_frequency <= k, the substring is valid."

Complexity
Time: O(26 × n²) → O(n²) because alphabet size is fixed
Space: O(26) → O(1)














2. Sliding Window + Frequency Map — O(n) 


#code
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









3. Sliding Window + Array Frequency — O(n) 

Since the problem explicitly says:

s consists of only uppercase English letters.

There are only 26 possible characters.

So instead of a dictionary, we can use an array of size 26.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26

        low = 0
        max_freq = 0
        max_len = 0

        for high in range(len(s)):

            index = ord(s[high]) - ord('A')
            freq[index] += 1

            if freq[index] > max_freq:
                max_freq = freq[index]

            while (high - low + 1) - max_freq > k:

                index = ord(s[low]) - ord('A')
                freq[index] -= 1

                low += 1

            curr_len = high - low + 1

            if curr_len > max_len:
                max_len = curr_len

        return max_len



Intuition:

Because the input contains only uppercase English letters, I can use a fixed array of size 26 instead of a hash map.
The sliding-window logic remains the same, but the frequency lookup is constant time with a smaller fixed memory footprint.

Complexity
Time: O(n)
Space: O(1) — exactly 26 entries.

