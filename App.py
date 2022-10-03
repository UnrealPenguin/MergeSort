from tkinter import *
import random
from Shapes.createSquare import createSquare
import Constants as c
import time

class App:
    def __init__(self, parent, width ,height):
        self.parent = parent ### parent is root
        self.container = Frame(parent)
        self.container.pack()
        
        self.canvas = Canvas(self.container, width=width, height=height, bg="white")
        self.canvas.pack(side = BOTTOM)

        self.buttonGen = Button(self.container)
        self.buttonGen.configure(text="Generate Shapes")
        self.buttonGen.pack(side = LEFT)
        self.buttonGen.bind("<Button-1>", self.buttonGenClick)

        self.buttonMS = Button(self.container)
        self.buttonMS.configure(text="MergeSort")
        self.buttonMS.pack(side = LEFT)
        self.buttonMS.bind("<Button-1>", self.buttonMSClick)

        self.shapesArray = []
        self.shapesArea = {}

    #
    def buttonMSClick(self, event):
        # remove current squares
        self.canvas.delete("square")

        test = [4,2,1,3]
        print(self.mergeSort(test))
        # sort merge is working, work on displaying it now...
        # test = self.mergeSort(self.shapesArea)
        # print(test[0])
            
    # Generates shapes
    def buttonGenClick(self, event):

        # deletes the previous array and squares if clicking again
        if(len(self.shapesArray) > 0):
            self.shapesArray = []
            self.shapesArea = {}
            self.canvas.delete("square")

        for i in range(0, 5):
            rng = random.randint(10, 100)

            try:
                # creates a square of random size at (x + previous squares length + 20 pixels margin)
                self.shapesArray.append(createSquare(app.getCanvas(), rng+(self.shapesArray[i-1].getFurthestPt()), c.START_Y, rng*2+(self.shapesArray[i-1].getFurthestPt()), c.START_Y+rng))
            except IndexError:
                self.shapesArray.append(createSquare(app.getCanvas(), c.START_X, c.START_Y, c.START_X+rng, c.START_Y+rng))

            self.shapesArray[i].makeSquare() 
            # stores each shapes area in an array
            self.shapesArea[(self.shapesArray[i].getArea())] = self.shapesArray[i].getCoor()
            # (self.shapesArray[i].getArea())

       
        # print(self.shapesArea)
         # get element from dict with index 
        # print(list(self.shapesArea.values())[0])


    # returns a sorted Array with N Log(N) time complexity
    def mergeSort(self, _array):
        if(len(_array) < 2):
            # when array is down to one elements or less return the array
            return _array[:] 
        else:
            middle = len(_array)//2
            left = self.mergeSort(_array[:middle])
            right = self.mergeSort(_array[middle:])
            
            # for i in range(len(left)):
            #     x1, y1, x2, y2 = self.shapesArray[i].getCoor()
            #     print(x1, y1, x2, y2)
            #     createSquare(app.getCanvas(), x1+i*100, y1+100, x2+i*100, y2+100).makeSquare()
            #     time.sleep(1)
            
            # for j in range(len(right)):
            #     x1, y1, x2, y2 = self.shapesArray[i].getCoor()
            #     print(x1, y1, x2, y2)
            #     createSquare(app.getCanvas(), x1+i*100, y1+100, x2+i*100, y2+100).makeSquare()
            #     time.sleep(1)

            return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        # while i or j is smaller than lenth of left or right, means there are still elements to append
        # i and j represents which index of the array we should be checking against
        while i < len(left) and j < len(right):
            # check which sublist has smallest element
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        #  no more elements on the right to append
        while i < len(left):
            result.append(left[i])
            i += 1
        #  no more elements on the left to append
        while j < len(right):
            result.append(right[j])
            j += 1

        return result






    # returns the canvas
    def getCanvas(self):
        return self.canvas



root = Tk()
root.title("MergeSort Algo visualizer")

app = App(root, c.WIDTH, c.HEIGHT)


root.mainloop()