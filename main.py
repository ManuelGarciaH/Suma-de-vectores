from math import *

class Vector:
    __y = 0
    __x = 0
    __m = 0
    __theta = 0

    def __init__(self, m, t):
        self.__m = m
        self.__theta = t
        self.__x = round(m * cos(radians(t)), 1)
        self.__y = round(m * sin(radians(t)), 1)

    def setX(self, x):
        self.__x = x

    def getX(self):
        return self.__x

    def setY(self, y):
        self.__y = y

    def getY(self):
        return self.__y

    def setM(self, m):
        self.__m = m

    def getM(self):
        return self.__m

    def setTheta(self, t):
        self.__theta = t

    def getTheta(self):
        return self.__theta


def sumaVectores(vector1, vector2) -> None:
    xR = vector1.getX() + vector2.getX()
    yR = vector1.getY() + vector2.getY()
    mR = round(sqrt(pow(xR, 2) + pow(yR, 2)), 1)
    thetaR = round(degrees(atan(yR / xR)), 1)
    print("Sumatoria de X resultante: ", xR)
    print("Sumatoria de Y resultante: ", yR)
    print("M resultante: ", mR)
    print("Theta resultante: ", thetaR)


def main() -> None:
    m1=80
    theta1=70
    m2=60
    theta2=20
    print("Valor de M del primer vector: ", m1)
    print("Valor de theta del primer vector: ", theta1)
    print("Valor de M del segundo vector: ", m2)
    print("Valor de theta del segundo vector: ", theta2)
    vector1 = Vector(m1, theta1)
    vector2 = Vector(m2, theta2)
    sumaVectores(vector1, vector2)


main()
