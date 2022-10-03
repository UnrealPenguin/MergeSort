from Shapes.createShape import createShape

# Creates a square at x1 x2 y1 y2 coordinates
# x1 is Left  x2 is Right
# y1 is Top y2 is Bottom
class createSquare(createShape):
    def __init__(self, canvas, x1, y1, x2, y2):
        super().__init__(canvas, x1, y1, x2, y2)

    def makeSquare(self):
        self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="black", tags="square")

    # returns the furthest point of the square
    def getFurthestPt(self):
        return self.x2

    # returns the length of a side
    def getLength(self):
        return self.x2-self.x1

    # returns the total area of the square
    def getArea(self):
        return (self.x2-self.x1)*(self.y2-self.y1)
