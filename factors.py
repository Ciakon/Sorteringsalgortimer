def factors(n : int) -> list[int]:
    factors = []
    for i in range(1, n + 1):
       if n % i == 0:
           factors.append(i)
    
    return factors

def closest(n : int, arr : list[int]) -> int:
    distances = []

    for i in arr:
        distances.append(abs(n - i))
    
    for i in range(len(distances)):
        if distances[i] == min(distances):
            return arr[i]