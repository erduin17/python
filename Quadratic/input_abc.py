from class_quadratic import *

def main():
    print("Input a,b and c from the equation ax^2+")
    #get Input
    a = float(input("Input a "))
    b = float(input("Input b "))
    c = float(input("Input c "))
    #end get inputs
    p1 = QuadraticEquation(1,0,-9)
    x1 = p1.x1()
    x2 = p1.x2()
    print ("discriminant = ",p1.discriminant())
    print("x1 = ",x1,"x2 = ",x2)

if __name__ == "__main__":
    main()
