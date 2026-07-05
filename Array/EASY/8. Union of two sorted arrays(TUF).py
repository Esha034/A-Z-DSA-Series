Brute Force (Using Set)

#Idea
Since the union contains only distinct elements,
I can insert all elements from both arrays into a set to remove duplicates

Algorithm
a.Create an empty set.
b.Insert all elements of nums1 and nums2.
c.Convert the set into a list.
d.Sort it.
e. Return the list.
#code
```
class Solution:
    def findUnion(self, nums1, nums2):
        s =set()
        for num in nums1:
            s.add(num)
        for num in nums2:
            s.add(num)
        return sorted(list(s))
```
#Complexity
Time: O((n+m)log(n+m))
Inserting into the set takes O(n+m).
Sorting the unique elements takes O((n+m) log(n+m)).

Space: O(n+m)
The set stores all unique elements.





Optimal (Two Pointers)
#Idea 
Since both arrays are sorted, I compare the current elements of both arrays. 
I always add the smaller element to the answer and move that pointer. 
If both elements are equal, I add it only once and move both pointers.
This avoids duplicates and maintains sorted order.

Algorithm
a.Take two pointers:
i → nums1
j → nums2
b.Compare nums1[i] and nums2[j].
c.Add the smaller element (if not already added).
d.Move the corresponding pointer.
e.If both are equal:
-Add only once.
-Move both pointers.
f.After one array ends, add the remaining unique elements from the other array.

#code
class Solution:
    def unionArray(self, nums1, nums2):
        n=len(nums1)
        m=len(nums2)
        union=[]
        i=j=0
    
        while i<n and j<m:
            if nums1[i]<=nums2[j]:
                if not union or union[-1]!=nums1[i]:
                    union.append(nums1[i])
                i+=1
            else:
                if not union or union[-1]!=nums2[j]:
                    union.append(nums2[j])
                j+=1
        while i<n:
            if not union or union[-1]!=nums1[i]:
                union.append(nums1[i])
            i+=1
        while j<m:
            if not union or union[-1]!=nums2[j]:
                union.append(nums2[j])
            j+=1
            
        return union

#Complexity
Time: O(n + m)
Each pointer moves through its array only once.

Space: O(n + m)
The output (union array) stores all unique elements.



