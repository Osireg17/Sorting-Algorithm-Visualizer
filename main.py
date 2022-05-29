from tkinter import *
from tkinter import ttk
from Colours import *
import random
from Algorithms.Merge_sort import mergeSortRecursive
from Algorithms.Bubble_Sort import bubbleSort
from Algorithms.Quick_sort import quick_sort
from Algorithms.Insertion_Sort import insertion_sort
from Algorithms.Selection_Sort import selectionSort

window = Tk()

window.title("Sorting Algorithms")
window.maxsize(1000, 700)

window.config(bg=WHITE)

algorithm_names = StringVar()
list_algorithms = ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Insertion Sort', 'Selection Sort']

speed_name  = StringVar()
list_speed = ['Fast', 'Medium', 'Slow']

data = [] # this list is filled with random values everytime you hit generate new array

def drawData(data, color):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]
    
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])

    window.update_idletasks()
    
    

def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])

def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

def sort():
    global data
    timeTick = set_speed()

    if algorithm_menu.get() == 'Bubble Sort':
        bubbleSort(data, drawData, timeTick)

    elif algorithm_menu.get() == 'Merge Sort':
        mergeSortRecursive(data, 0, len(data) - 1, drawData, timeTick)

    elif algorithm_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawData, timeTick)

    elif algorithm_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)

    elif algorithm_menu.get() == 'Selection Sort':
        selectionSort(data, drawData, timeTick)


UserInterface = Frame(window, width=900, height=300, bg=WHITE)
UserInterface.grid(row=0, column=0, padx=10, pady=5)

label1 = Label(UserInterface, text="Sorting Algorithms: ", bg=WHITE)
label1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algorithm_menu = ttk.Combobox(UserInterface, textvariable=algorithm_names, values=list_algorithms)
algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
algorithm_menu.current(0)

label1 = Label(UserInterface, text="Sorting Speed: ", bg=WHITE)
label1.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UserInterface, textvariable=speed_name, values=list_speed)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

b1 = Button(UserInterface, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

b2 = Button(UserInterface, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b2.grid(row=2, column=0, padx=5, pady=5)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()