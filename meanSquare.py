from math import pow
import sys

def squares(x0, qty):
    x = x0
    xList = list()
    yList = list()
    numToSquare = list()
    for iteration in range(qty):
        numToSquare.append(int(x))
        y = pow(float(x),2)
        y = int(y)
        yList.append(y)
        x = getSquares(y)
        xList.append(x)
    # print xList, yList, numToSquare
    return xList, yList, numToSquare

def getSquares(result):
    result = str(result)
    if len(result)%2 != 0:
        if len(result)==5:
            return result[0:4]
        else:
            return result[1:5]
    else:
        if len(result)==8:
            return result[2:6]
        else:
            return result[1:5]

def printTable(yList, xList, numToSquare):
    for iter in range(len(yList)):
        print "y_{0} = {1}^2 = {2}, \t X_{0} = {3}, r_{4} = {5} ".format(iter, numToSquare[iter], xList[iter],yList[iter], iter+1, ( float(yList[iter])/10000) )

def main():
    x0 = int(sys.argv[1])
    qty = int(sys.argv[2])
    xList, yList, numToSquare = squares(x0, qty)
    printTable(xList, yList, numToSquare)


if __name__ == "__main__":
    main()
