class Solution:
    def findPages(self, arr, k):
        n=len(arr)
        if n<k:
            return -1
            
        def is_possible(mid):
            students = 1
            current_pages = 0
            for pages in arr:
                if current_pages + pages <= mid:
                    current_pages += pages
                else:
                    students += 1
                    current_pages = pages
            return students <= k

        low, high = max(arr), sum(arr)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                ans = mid
                high = mid - 1  # Try to find a smaller maximum
            else:
                low = mid + 1   # Increase the limit

        return ans
