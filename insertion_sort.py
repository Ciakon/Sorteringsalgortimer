def insertion_sort(arr : list[int]) -> list[list[list[int]], list[list[int]]]:
    states = []
    highlights = []

    n = len(arr)

    for i in range(1, n):
        j = i - 1

        states.append(arr.copy())
        highlights.append([j, i])

        while j >= 0 and arr[j] > arr[j + 1]:

            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            states.append(arr.copy())
            highlights.append([j, i])

            j -= 1
            
    return [states, highlights]