import random

def bogo_sort(arr : list[int]) -> list[list[list[int]], list[list[int]]]:
    states = []
    highlights = []

    running = True
    while running:
        running = False
        random.shuffle(arr)

        for i in range(len(arr) -1):

            states.append(arr.copy())
            highlights.append([i, i + 1])

            if arr[i] > arr[i + 1]:

                running = True
                break

    return [states, highlights]
