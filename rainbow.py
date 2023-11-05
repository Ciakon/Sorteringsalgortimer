#https://www.particleincell.com/2014/colormap/
import math

def rainbow_map(f : float) -> list[int]:
    a = (1-f)/0.2
    X = math.floor(a)
    Y = math.floor(255*(a-X))

    ff = 255

    if X == 0:
        return [ff, Y, 0]
    if X == 1:
        return [ff - Y, ff, 0]
    if X == 2:
        return [0, ff, Y]
    if X == 3:
        return [0, ff - Y, ff]
    if X == 4:
        return [Y, 0, ff]
    if X == 5:
        return [ff, 0, ff]
    
