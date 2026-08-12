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

# Given an unsorted array of size n, use selection sort to sort the array arr[] in decreasing order.
# Input: arr = [1,3,5,2,4,6,8,7,9]
# Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]
# Explanation: After sorting the array in increasing order using selection sort, we get 9, 8, 7, 6, 5, 4, 3, 2, 1

arr=[1,3,5,2,4,6,8,7,9]
def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min_idx = i;
        for j in range(i + 1, n):
            if arr[j] > arr[min_idx]:
                min_idx = j;
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr
print(selection_sort(arr))

# Find the Minimum
# input=arr=[12, 5, 8, 3, 10]
# expectedoutput=[3, 5, 8, 12, 10]
arr=[12, 5, 8, 3, 10]
def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min_idx = i;
        for j in range(i + 1, n-1):
            if arr[j] < arr[min_idx]:
                min_idx = j;
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr
print(selection_sort(arr))

#count the swaps
arr = [4, 3, 2, 1]

def selection_sort(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            count += 1

    return arr, count

print(selection_sort(arr))

