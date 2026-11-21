Using Recursive Binary Search:

Since the array is sorted, the first thing that comes to apply is binary search, but the problem here is that we don’t know the size of the array.

So in order to find the position of the key, first we find bounds and then apply a binary search algorithm. Let the low be pointing to the 1st element and the high pointing to the 2nd element of the array, Now compare the key with the high index element.

if it is greater than the high index element then copy the high index in the low index and double the high index. 
if it is smaller, then apply binary search on high and low indices found.
low and high will follow following kind of pattern:

l = 0, h = 1
l = 1, h = 2
l = 2, h = 4
l = 4, h = 8
So we can observe that over range is doubling every turn so it will take at most log(k) time.







  
#Code
  
# Binary search function to find the position of the element in a the bound
def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        return binary_search(arr, mid + 1, r, x)
    return -1

# Function to find the bounds in the infinite-size array (represented as a list)
def find_pos(arr, key):
    l = 0
    h = 1

    # Find high to do binary search
    while h < len(arr) and arr[h] < key:
        # Store previous high
        l = h
        # Double high index
        h = 2 * h

    # Clamp high if it goes out of array bounds
    if h >= len(arr):
        h = len(arr) - 1

    # At this point, we have updated low and high
    # indices, thus use binary search between them
    return binary_search(arr, l, h, key)

if __name__ == '__main__':
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    k = 170
    ans = find_pos(arr, k)
    print(ans)
  

Time Complexity: 
O(log p), where p is the index of the target key. The algorithm first doubles the search range (O(log p)), then performs binary search in that range (O(log p)), giving an overall complexity of O(log p).
Auxiliary Space:
O(log p), due to the recursive calls of the binary search.
  
