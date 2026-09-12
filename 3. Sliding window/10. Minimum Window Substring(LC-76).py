class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if m < n:
            return ""

        # Frequency of characters required from t
        freq = [0] * 128

        for ch in t:
            freq[ord(ch)] += 1

        low = 0
        required = n

        min_len = m + 1
        start = 0

        for high in range(m):

            # Add s[high] to the window
            index = ord(s[high])

            # This character was still required
            if freq[index] > 0:
                required -= 1

            freq[index] -= 1

            # Window contains all characters of t
            while required == 0:

                curr_len = high - low + 1

                if curr_len < min_len:
                    min_len = curr_len
                    start = low

                # Remove s[low]
                index = ord(s[low])
                freq[index] += 1

                # We have now lost a required character
                if freq[index] > 0:
                    required += 1

                low += 1

        if min_len == m + 1:
            return ""

        return s[start:start + min_len]







        
        
