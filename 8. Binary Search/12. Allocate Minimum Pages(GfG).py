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
































Intuition:


I will solve this problem using binary search on the answer.

First, I check whether the number of books is less than the number of students. If it is, I return -1 because every student must receive at least one book.

The minimum possible maximum page count is the largest book's page count, and the maximum possible value is the sum of all pages.

I use a helper function called `is_possible` to check whether all books can be allocated contiguously within a given page limit. I greedily assign books to the current student until adding another book would exceed the limit. Then I assign that book to a new student.

If the number of students required is at most k, the limit is feasible, so I save the answer and search for a smaller limit. Otherwise, I increase the limit.

When binary search finishes, I return the smallest feasible answer.

The time complexity is O(n log(S − M + 1)), where S is the total number of pages and M is the maximum page count. The auxiliary space complexity is O(1).
