 # Kathleen Delany delan270
 #
 # I understand that this is a graded, individual examination that may not be
 # discussed with anyone. I also understand that obtaining solutions or
 # partial solutions from outside sources, or discussing any aspect of the exam
 # with anyone is academic misconduct and will result in failing the course.
 # I further certify that this program represents my own work and that none of
 # it was obtained from any source other than the material presented as part of the
 # course.

class Complex:
    def __init__(self, real = 0.0, imag = 0.0):
        self.__real = real
        self.__imag = imag

    def __repr__(self):
        if self.__imag == 0:
            return str(self.__real)
        elif self.__imag < 0:
            return str(self.__real) + ' - ' + str(self.__imag) + 'i'
        else:
            return str(self.__real) + ' + ' + str(self.__imag) + 'i'

    def __getReal__(self):
        return self.__real

    def __setReal__(self,real):
        self.__real = real

    def __getImag__(self):
        return self.__imag

    def __setImag__(self,imag):
        self.__imag = imag

    def __add__(self, complex2):
        new_real = self.__real + complex2.__real
        new_imag = self.__imag + complex2.__imag
        return Complex(new_real,new_imag)

    def __mul__(self, complex2):
        realSum1 = self.__real * complex2.__real
        realSum2 = - (self.__imag * complex2.__imag)
        imagSum1 = self.__real * complex2.__imag
        imagSum2 = self.__imag * complex2.__real
        realSum = realSum1 + realSum2
        imagSum = imagSum1 + imagSum2
        return Complex(realSum,imagSum)

    def __abs__(self):
        complexAbs = (self.__real ** 2) + (self.__imag ** 2)
        return complexAbs ** 2
