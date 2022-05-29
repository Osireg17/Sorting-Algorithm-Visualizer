from Colours import *
import time

def insertion_sort(ele, drawData, timeTick):
    for i in range(1,len(ele)):
        anchor = ele[i] # Your anchor is the element that your currently dealing with
        j = i - 1 # this is the element on the left
        while j >= 0 and anchor < ele[j]:
            ele[j+1] = ele[j] # swapping the elements from left to right
            j = j - 1
        ele[j + 1] = anchor # assign the next element within the sorted list as the anchor
        drawData(ele, [YELLOW if x == j or x == i else BLUE for x in range(len(ele))])
        time.sleep(timeTick)
    drawData(ele, [BLUE for x in range(len(ele))])
