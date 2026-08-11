# Given an unsorted array of size n, use selection sort to sort the array arr[] in increasing order.
# Input: arr = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
# Explanation: After sorting the array in increasing order using selection sort, we get 1 3 4 7 9.
from typing import List

class Solution:
    def selectionSort(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for i in range(n):
            min_idx = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr
