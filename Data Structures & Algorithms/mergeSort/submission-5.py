# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)
    
    def mergeSortHelper(self, pairs: List[Pair], s:int, e:int) -> List[Pair]:
        m = (s + e)//2
        # if there is only one pair in the arr return the pair
        if e - s + 1 <= 1:               
            return pairs

        # Sort the left half
        self.mergeSortHelper(pairs, s, m)

        # Sort the right half
        self.mergeSortHelper(pairs, m + 1, e)

        # Merge sorted halfs
        self.merge(pairs, s, m, e)
        
        return pairs

    def merge(self, arr: List[Pair], s:int,m:int, e:int) -> None:
        #here we are splitting up left and right and combining them
        L = arr[s: m+1]
        R = arr[m+1:e+1]
        #incrementing vars
        i = 0
        j = 0
        k = s
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i] # we are making a new array with sorted values
                i += 1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1


            
            

        

