1. Brute Force — O(n²)

Generate every substring and check whether its characters are unique.

#code
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            freq = {}

            for j in range(i, n):
                if s[j] in freq:
                    break

                freq[s[j]] = 1

                length = j - i + 1

                if length > max_len:
                    max_len = length

        return max_len

I start a substring from every index and keep extending it until I encounter a duplicate character. Since a duplicate means the current substring is no longer valid, I stop and try the next starting position.

Complexity
Time: O(n²)
Space: O(n)




2. Sliding Window + Frequency Map — O(n)


# code
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        freq = {}
        low = 0
        max_len = 0

        for high in range(n):

            freq[s[high]] = freq.get(s[high], 0) + 1

            # Shrink while duplicate exists
            while (high - low + 1) > len(freq):
                freq[s[low]] -= 1

                if freq[s[low]] == 0:
                    del freq[s[low]]
                low += 1

            # Now window is valid
            curr_len = high - low + 1

            if curr_len > max_len:
                max_len = curr_len

        return max_len

Complexity:

Time: O(n)
Space: O(n)



3. Optimized Sliding Window — Last Seen Index

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


Complexity:

Time: O(n)
Space: O(n)



            

        
