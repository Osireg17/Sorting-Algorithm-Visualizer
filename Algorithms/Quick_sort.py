from Colours import *
import time

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end, drawData, timeTick):
    if start < end:
        pi = partition(elements, start, end, drawData, timeTick)
        quick_sort(elements, start, pi-1, drawData, timeTick)
        quick_sort(elements, pi+1, end,drawData, timeTick)

        drawData(elements, [PURPLE if x >= start and x < pi else YELLOW if x == pi
        else DARK_BLUE if x > pi and x <= end else BLUE for x in range(len(elements))])
        time.sleep(timeTick)
    drawData(elements, [BLUE for x in range(len(elements))])



def partition(elements, start, end, drawData, timeTick):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end
