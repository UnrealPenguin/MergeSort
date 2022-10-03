from tkinter import *
import random
from typing import overload
from Shapes.createSquare import createSquare
import Constants as c

class App:
    def __init__(self, parent, width ,height):
        self.parent = parent ### parent is root
        self.container = Frame(parent)
        self.container.pack()

        self.parent.title("MergeSort Algo")

        self.canvas = Canvas(self.container, width=width, height=height, bg="white")
        self.canvas.pack(side = BOTTOM)

        self.labelCount = Label(self.container, text = "Number of shapes")
        self.labelCount.pack(side=LEFT)
        self.desiredCount = Entry(self.container)
        self.desiredCount.pack(side=LEFT)
        

        self.buttonGen = Button(self.container)
        self.buttonGen.configure(text="Generate Shapes")
        self.buttonGen.pack(side = LEFT)
        self.buttonGen.bind("<Button-1>", self.buttonGenClick)

        self.buttonMS = Button(self.container)
        self.buttonMS.configure(text="MergeSort")
        self.buttonMS.pack(side = LEFT)
        self.buttonMS.bind("<Button-1>", self.buttonMSClick)

        self.shapesArray = []
        self.shapesArea = []

    # Displays the whole merge sort process
    def buttonMSClick(self, event):
        sortedArray = self.mergeSort(self.shapesArea)
        self.displaySorted(sortedArray)
            
    # Generates shapes
    def buttonGenClick(self, event):

        # deletes the previous array and squares if clicking again
        if(len(self.shapesArray) > 0):
            self.shapesArray = []
            self.shapesArea = []
            self.canvas.delete("square")

        self.initialDisplay()

    # Initial displaying of shapes
    def initialDisplay(self):

        # if no amount or something else is given default to 5
        if (self.desiredCount.get() is None):
            toGenerate = 5 
        else:
            try:
                if(int(self.desiredCount.get())> 20):
                    # Max of 20 or else very likely to extend beyond the window size
                    toGenerate = 20
                else:
                    toGenerate = int(self.desiredCount.get())
            except ValueError:
                toGenerate = 5 

            
        for i in range(0, toGenerate):
            rng = random.randint(5, 100)

            try:
                # creates a square of random size at (x + previous squares length + margin)
                self.shapesArray.append(createSquare(app.getCanvas(), self.shapesArray[i-1].getFurthestPt()+c.MARGIN, c.START_Y-rng, rng+self.shapesArray[i-1].getFurthestPt()+c.MARGIN, c.START_Y))
            except IndexError:
                self.shapesArray.append(createSquare(app.getCanvas(), c.START_X, c.START_Y-rng, c.START_X+rng, c.START_Y))            

            self.shapesArray[i].makeSquare() 
            # stores each shapes area in an array
            self.shapesArea.append({"Area":(self.shapesArray[i].getArea()), "edgeLength":self.shapesArray[i].getLength()})       

    # display shapes during the merge sort operation
    def displaySorted(self, _array):
        tempArray = []

        for i in range(len(_array)):
            if(i==0):
                tempArray.append(createSquare(app.getCanvas(),  
                                                c.START_X, 
                                                c.START_Y+c.Y_OFFSET, 
                                                c.START_X+_array[i]["edgeLength"], 
                                                c.START_Y+c.Y_OFFSET - _array[i]["edgeLength"]))
            else:
                tempArray.append(createSquare(app.getCanvas(),   
                                                c.MARGIN + tempArray[i-1].getFurthestPt(), 
                                                c.START_Y+c.Y_OFFSET, 
                                                c.MARGIN+ _array[i]["edgeLength"] + tempArray[i-1].getFurthestPt(), 
                                                c.START_Y+c.Y_OFFSET-_array[i]["edgeLength"]))
        
            tempArray[i].makeSquare()


    # returns a sorted Array with N Log(N) time complexity
    def mergeSort(self, _array):

        if(len(_array) < 2):
            # when array is down to one elements or less return the array
            return _array[:] 
        else:
            middle = len(_array)//2
            left = self.mergeSort(_array[:middle])
            right = self.mergeSort(_array[middle:])

            return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        # while i or j is smaller than lenth of left or right, means there are still elements to append
        # i and j represents which index of the array we should be checking against
        while i < len(left) and j < len(right):
            # check which sublist has smallest element
            if left[i]["Area"] < right[j]["Area"]:
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
app = App(root, c.WIDTH, c.HEIGHT)


root.mainloop()