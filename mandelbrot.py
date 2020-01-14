 # Kathleen Delany delan270
 #
 # I understand that this is a graded, individual examination that may not be
 # discussed with anyone. I also understand that obtaining solutions or
 # partial solutions from outside sources, or discussing any aspect of the exam
 # with anyone is academic misconduct and will result in failing the course.
 # I further certify that this program represents my own work and that none of
 # it was obtained from any source other than the material presented as part of the
 # course.

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
