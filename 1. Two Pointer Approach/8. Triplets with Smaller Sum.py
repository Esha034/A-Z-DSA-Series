Optimal approach- 2 pointer



#Idea:
First, I sort the array because sorting allows me to use two pointers and determine how the sum changes when I move either pointer.

I fix the first element using i, then initialize j immediately after i and k at the last position.
For every fixed i, I try to find all pairs (j, k) whose total with arr[i] is less than the given sum.

Case 1: total >= sum

if total >= sum:
    k -= 1

If the current sum is greater than or equal to the target, the triplet is invalid. 
Since the array is sorted, I decrease k to use a smaller value and reduce the sum.

Case 2: total < sum

else:
    count += (k - j)
    j += 1

When total < target, dont count only the current triplet. 
Because the array is sorted, all positions between j+1 and k are also valid.
Therefore, add k-j at once.




    
#code

class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        n=len(arr)
        count=0
        
        for i in range(n-2):
            j=i+1
            k=n-1
            
            while j<k:
                total=arr[i]+arr[j]+arr[k]
                if total>=sum:
                    k-=1
                    
                else:
                    count+=(k-j )
                    j+=1
                    
        return count


#Complexity

Time: O(n2)
Space: O(1)
