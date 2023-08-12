def binarySearch(tail, l, h, value):
    
    if value > tail[h]:
        return h+1
    while h>l:
        middle = (h+l)//2
            
        if tail[middle] == value:
            return middle
            
        if tail[middle] > value:
            h = middle
            
        else:
            l = middle + 1
        
    return h
    
class Solution:

    def longestSubsequence(self,a,n):

        tail = [0 for _ in range(n)]
        tail[0] = a[0]
        lastIndex = 0 
        
        for i in range(1,n):

            index = binarySearch( tail, 0, lastIndex, a[i] )
            tail[index] = a[i]
            lastIndex = max( lastIndex, index )

        return lastIndex+1