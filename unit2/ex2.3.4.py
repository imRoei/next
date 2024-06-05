class pixel:
    def __init__(self,x=0,y=0, r=0, g=0, b=0):
        self._x = x
        self._y = y
        self._red = r
        self._green = g
        self._blue = b

    def set_coords(self, x, y):
        self._x = x
        self._y = y
    
    def set_grayscale(self):
        gray = self._red+self._green+self._blue
        self._red = gray
        self._green = gray
        self._blue = gray

    def print_pixel_info(self):
        print("X:"+self._x, "Y: "+self._y,", Color("+ self._red+", ", self._green+", ", self._blue,")")
    