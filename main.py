from tkinter import *

from tkinter import ttk
import random
from colors import *

# Importing algorithms
from algorithms.bubbleSort import bubble_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort
from algorithms.countingSort import counting_sort

# Main window
window = Tk()
window.title("TANGO")
window.geometry("860x540")
window.resizable(False,False)
window.config(bg="#EBF5FB")

algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort',
             'Counting Sort']
speed_list = ['Fast', 'Medium', 'Slow']


# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 835
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
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        # #canvas.create_text(x0+2,y0,anchor= SW ,text=str(data[i]),
        #      font=("new roman" ,15, "italic"),fill="orange")

    window.update_idletasks()


# Randomly generate array
# size=0
def generate():
    global data

    size_vallue =int(sizevalue.get())

    data = []
    for i in range(size_vallue):
        data.append( random.randint(1, 150))

    drawData(data, [BLUE for x in range(len(data))])


# def set_speed():
#     if speed_menu.get() == 'Slow':
#         return 0.03
#     elif speed_menu.get() == 'Medium':
#         return 0.01
#     else:
#         return 0.0000000000001


def sort():
    global data
    timeTick = speed_menu.get()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data) - 1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort(data, drawData, timeTick)
    else:
        counting_sort(data, drawData, timeTick)


# User interface #
UI_frame = Frame(window, width=560, height=100, bg="#AED6F1")
UI_frame.grid(row=0, column=0, padx=5, pady=10)

l1 = Label(UI_frame, text="Algorithm: ", bg='#AED6F1')
l1.place(x=15, y=5)

algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list,)
algo_menu .place(x=88, y=5)
algo_menu.current(2)

l2 = Label(UI_frame, text="Sorting Speed: ", bg='#AED6F1')
l2.place(x=257, y=5)

speed_menu = Scale(UI_frame, from_=0.0, to=3, resolution=0.1, orient=HORIZONTAL,digits=2,width=11,
bg="#AED6F1",length=200,fg="#273746")
speed_menu.place(x=345, y=5)



canvas = Canvas(window, width=835, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

# buttons
# value = int(DoubleVar())
#
# def get_size():
#     return value
# def update():
#     size=get_size()
# ,variable=value,command=update


l3 = Label(UI_frame, text="Size Value: ", bg='#AED6F1')
l3.place(x=270, y=60)

sizevalue= Scale(UI_frame, from_=0, to=300, resolution=1, orient=HORIZONTAL,
bg="#AED6F1",length=200,fg="#273746",width=15)
sizevalue.place(x=345, y=50)
# l3.place(x=60, y=20)



b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY,width=10)

b1.place(x=23, y=54)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY,width=13)
b3.place(x=23*5, y=54)

window.mainloop()
