 # Kathleen Delany 

from complex import Complex

class Mandelbrot:
    def __init__(self,startVal, limit = 50):
        self.__limit = limit
        self.__colormap = ["black","red", "yellow", "green", "blue", "purple"]
        self.__cardinality = 0
        n = startVal
        for i in range(self.__limit):
            if abs(startVal) <= 2:
                startVal = (startVal * startVal) + n
                self.__cardinality += 1

    def __get_color__(self):
        if self.__cardinality == self.__limit:
            return self.__colormap[0]
        if self.__cardinality < 50 and self.__cardinality >= 41:
            return self.__colormap[1]
        if self.__cardinality <= 40 and self.__cardinality >= 31:
            return self.__colormap[2]
        if self.__cardinality <= 30 and self.__cardinality >= 21:
            return self.__colormap[3]
        if self.__cardinality <= 20 and self.__cardinality >= 11:
            return self.__colormap[4]
        if self.__cardinality <= 10 and self.__cardinality >= 0:
            return self.__colormap[5]
