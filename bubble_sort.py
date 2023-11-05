def bubble_sort(arr : list[int]) -> list[list[list[int]], list[list[int]]]:
    n = len(arr)

    states = []
    highlights = []

    for i in range(n):
        sorted = False

        for j in range(n - i - 1):

            states.append(arr.copy())
            highlights.append([j, j + 1])

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                
                sorted = False
            
        if (sorted):
            return [states, highlights]
    return [states, highlights]