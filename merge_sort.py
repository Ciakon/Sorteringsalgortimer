import math

def merge_sort(arr : list[int]) -> list[list[list[int]], list[list[int]]]:
    states = []
    highlights = []
    merge_sort_part_2(arr, 0, len(arr), states, highlights)
    return [states, highlights]

def merge_sort_part_2(arr : list[int], start : int = 0, length : int = 0, states : list[list[int]] = [], highlights : list[list[int]]  = []) -> None:
    if length == 1:
        return
    
    merge_sort_part_2(arr, start, length//2, states, highlights)
    merge_sort_part_2(arr, start + length//2, math.ceil(length/2), states, highlights)

    left = arr[start:start + length//2]
    right = arr[start + length//2:start + length]

    merge(arr, left, right, start, states, highlights)

def merge(arr : list[int], L : list[int], R : list[int], start : int, states : list[list[int]] = [], highlights : list[list[int]]  = []) -> None: #merge sort part 3

    i = start + 0

    states.append(arr.copy())
    highlights.append([i])


    while len(L) and len(R):
        if L[0] < R[0]:
            arr[i] = L[0]
            L = L[1:]

            states.append(arr.copy())
            highlights.append([i])

        else:
            arr[i] = R[0]
            R = R[1:]

        i += 1
    
    if not len(L):
            for k in R:
                
                arr[i] = k
                i += 1

                states.append(arr.copy())
                highlights.append([i])

                
    
    else:
        for k in L:
            arr[i] = k
            i += 1

            states.append(arr.copy())
            highlights.append([i])