import pygame, time, random
from pygame.locals import *

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from bogo_sort import bogo_sort
from rainbow import rainbow_map
from factors import factors, closest

from typing import Callable

running = True

def setup() -> None:
    global Window_width, Window_height, display, clock, title_map, stop

    Window_width = 1600
    Window_height = 800
    
    pygame.init()
    display = pygame.display.set_mode((Window_width, Window_height), RESIZABLE)
    
    clock = pygame.time.Clock()

    title_map = {bubble_sort : "Bubble sort", selection_sort : "Selection sort", insertion_sort : "Insertion sort", merge_sort : "Merge sort", bogo_sort : "Bogo sort"}

    stop = False
    
def text(text : str, x : int, y : int, size : int, color : str | tuple[int] = (160,160,160), center_text : bool = False) -> None:
    font = pygame.font.SysFont("Comic Sans MS", size)
    text_surface = font.render(text, True, color)

    if center_text:
        text_rect = text_surface.get_rect(center=(x, y))
        display.blit(text_surface, text_rect)

    else:
        display.blit(text_surface, (x, y))

def bar_show(arr : list[int], highlight : list[int] = []) -> None:

    width = Window_width // len(arr) 
    
    background_color = "black"
    default_color = "white"
    highlight_colors = ["red", "blue", "yellow"]

    display.fill(background_color)

    for x in range(len(arr)):
        rect_color = default_color
        
        if x in highlight:
            rect_color = highlight_colors[highlight.index(x)]
    
        h = (arr[x] / max(arr)) * Window_height

        rect = (x*width, Window_height - h, width, h)

        pygame.draw.rect(display, rect_color, rect)



def rainbow_show(arr : list[int], highlight : list[int] = []) -> None:
    n = len(arr)
    
    for x in range(n):
        width = Window_width // n

        color = rainbow_map(arr[x]/n)

        rect = (x*width, 0, width, Window_height)
        pygame.draw.rect(display, color, rect)

        if x in highlight:
            rect = (x*width, 0, width, width)
            pygame.draw.rect(display, "black", rect)

def box_show(arr : list[int], highlight : list[int] = [], previous_arr : list[int] = []) -> None:
    background_color = "black"
    default_color = "white"
    highlight_colors = ["red", "blue", "yellow"]
    text_color = "black"
    swap_color = "green"

    n = len(arr)
    spacing = (1 * Window_width / 3) // (n + 1)
    width = (2 * Window_width / 3) // n
    height = width
    
    #check if array changed
    swap = []

    for i in range(len(arr)):

        if len(previous_arr) == 0:
            break

        if arr[i] != previous_arr[i]:
            swap.append(i)

    if len(swap) == 2:
        box_swap(previous_arr, swap[0], swap[1], n, spacing, width, height, text_color, background_color, swap_color)
        return
    
    display.fill(background_color)

    for i in range(n):
        num = str(arr[i])

        color = default_color

        x = spacing + i * (width + spacing)

        y = (Window_height / 2) - height/2

        rect = (x, y, width, height)

        if i in highlight:

            color = highlight_colors[highlight.index(i)]

            pygame.draw.rect(display, color, rect)
        else:
            pygame.draw.rect(display, color, rect)

        text(num, x + width/2, y + height/2, int(width / 2), text_color, True)
        fontSize = int((Window_width)/60)
        text(f"Algorithim: {title}", 0, 0, fontSize)

def box_swap(arr : list[int], a : int, b : int, n : int, spacing : int, width : int, height : int, text_color : str | tuple[int], background_color : str | tuple[int], swap_color : str | tuple[int]) -> None:

    swapping = True
    stage = "start"

    while swapping and running and not stop:
        window()

        display.fill(background_color)
        #draw unswapped boxes
        for i in range(n):
            num = str(arr[i])

            color = "white"

            x = spacing + i * (width + spacing)
            y = (Window_height / 2) - height/2
            rect = (x, y, width, height)

            if i == a and stage == "start":
                a_x = x
                a_y = y
                a_x_start = a_x
                a_y_start = a_y
                a_num = num
                continue
                
            if i == b and stage == "start":
                b_x = x
                b_y = y
                b_x_start = b_x
                b_y_start = b_y
                b_num = num
                stage = "up"
                continue
            
            if i == a or i == b:
                continue

            
            pygame.draw.rect(display, color, rect)
            text(num, x + width/2, y + height/2, int(width / 2), text_color, True)

        
        
        #swap animaiton

        rect = (a_x, a_y, width, height)
        pygame.draw.rect(display, swap_color, rect)
        text(a_num, a_x + width/2, a_y + height/2, int(width / 2), text_color, True)

        rect = (b_x, b_y, width, height)
        pygame.draw.rect(display, swap_color, rect)
        text(b_num, b_x + width/2, b_y + height/2, int(width / 2), text_color, True)

    
        speed = ((width + spacing) * (b - a) + 2*(y - Window_height/5)) / 100

        speed *= fps/10

        if stage == "up":
            if a_y > Window_height/5:
                a_y -= speed
                b_y -= speed
            else:
                stage = "swap"

        # a is always left
        if stage == "swap":
            if a_x < b_x_start:
                a_x += speed
                b_x -= speed
            else:
                stage = "down"

                #smoothen animation
                a_x = b_x_start
                b_x = a_x_start


        if stage == "down":
            if a_y < a_y_start:
                a_y += speed
                b_y += speed
            else:
                swapping = False

        fontSize = int((Window_width)/60)
        text(f"Algorithim: {title}", 0, 0, fontSize)
        pygame.display.flip()

def animate(arr : list[int], visualisation : Callable = bar_show, algorithim : Callable = bubble_sort) -> None:
    global running

    random.shuffle(arr)

    time_start = time.perf_counter()
    states, highlights = algorithim(arr)
    time_taken = time.perf_counter() - time_start

    i = 0
    delay = 0
    
    time_start_visual = time.perf_counter()
    

    while True:
            clock.tick(fps)
            if not running:
                return
            
            window()
            
            if i < len(states):
                state, highlight = states[i], highlights[i]

                if visualisation == box_show and i > 0 and algorithim != bogo_sort:
                    # box_show doesn't work on merge_sort
                    if algorithim == merge_sort:
                        visualisation = bar_show
                    else:
                        # add previous state if using box_show
                        visualisation(state, highlight, states[i - 1])
                else:
                    visualisation(state, highlight)

                i += 1

            # when animation is done
            else:
                visualisation(states[-1], [])

                if not delay:
                    time_taken_visual = time.perf_counter() - time_start_visual
                    delay = time.perf_counter()
                    
                if time.perf_counter() - delay >= 5:
                    # stop = True
                    break
                
                fontSize = int((Window_width)/60)
                text(f'Time taken (visualization): {str(time_taken_visual)} seconds', 0, fontSize*2, fontSize)
                text(f'Time taken: {str(time_taken)} seconds', 0, fontSize*3, fontSize)
            
            fontSize = int((Window_width)/60)

            text(f"Algorithim: {title}", 0, 0, fontSize)
            
            pygame.display.flip()

#allows resizing, quitting, and other input during animation
def window() -> None:
    global running, Window_width, Window_height, display, title, algorithim, current_array, stop, visualization_algorithim
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Window_width, Window_height = pygame.display.get_window_size()

def animation_setup() -> None:
    
    pygame.quit()

    global current_array, current_sorting_algorithim, current_visualization_algorithim, fps

    algorithim_map = {'1' : bubble_sort, '2' : selection_sort, '3' : insertion_sort, '4' : merge_sort, '5' : bogo_sort}
    print("Choose sorting algorithim preset (1: bubble sort, 2: selection sort, 3: insertion sort, 4: merge sort, 5: bogo sort)")
    algorithim_input = input()

    current_sorting_algorithim = algorithim_map[algorithim_input]

    visualization_map = {bubble_sort : bar_show, selection_sort : box_show, insertion_sort : box_show, merge_sort : rainbow_show, bogo_sort : box_show}
    current_visualization_algorithim = visualization_map[current_sorting_algorithim]


    length_map = {bubble_sort : 20, 
                  selection_sort : 20,
                  insertion_sort : 10,
                  merge_sort : closest(500, factors(Window_width)),
                  bogo_sort : 5
                  }
    
    array_length = length_map[current_sorting_algorithim]

    current_array = list(range(1, array_length + 1))

    fps_map = {bubble_sort : 8, selection_sort : 10, insertion_sort : 5, merge_sort : 100, bogo_sort : 2}

    fps = fps_map[current_sorting_algorithim]

    setup()

setup()
pygame.quit()

while running:

    animation_setup()
    title = title_map[current_sorting_algorithim]

    animate(current_array, current_visualization_algorithim, current_sorting_algorithim)

    stop = False

pygame.quit()
