import time
from Colours import *

def selectionSort(seq, drawData, timeTick):
  n = len(seq)
  for i in range(n-1):
    #assuming that the ith element is the smallest element
    smallIndex = i
    #Determine if any other element contains a smaller value
    for j in range(i+1,n):
      if seq[j] < seq[smallIndex]:
        smallIndex = j
    #swap the ith value and smallIndex value only if the smallest value is
    #not already in its proper position.
    if smallIndex != i:
      temp = seq[i]
      seq[i] = seq[smallIndex]
      seq[smallIndex] = temp
    drawData(seq, [YELLOW if x == smallIndex or x == i else BLUE for x in range(len(seq))])
    time.sleep(timeTick)
  drawData(seq, [BLUE for x in range(len(seq))])

# The run time for this code is  O(n^2)