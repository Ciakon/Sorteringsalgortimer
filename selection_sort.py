def selection_sort(arr : list[int]) -> list[list[list[int]], list[list[int]]]:
    states = []
    highlights = []

    n = len(arr)

    for i in range(n - 1):
        min_i = i

        for j in range(i + 1, n):

            states.append(arr.copy())
            highlights.append([j, i, min_i])
            
            if arr[j] < arr[min_i]:
                min_i = j

                
        
        arr[i], arr[min_i] = arr[min_i], arr[i]
        states.append(arr.copy())
        highlights.append([i])

        

    return [states, highlights]