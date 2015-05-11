from math import pow
import sys


def constantMultiplier(x0, cte, qty):
    yList = list()
    xList = list()
    x = x0
    xList.append(x)
    for number in range(1, qty + 1 ):
        result = calculateValues(cte, x)
        yList.append(result)
        xTemp = (getX(result))
        xList.append(xTemp)
        x = xTemp
    return yList, xList

def calculateValues(cte, x0):
    return cte * int(x0)

def getX(result):
    result = str(result)
    return result[2:6] if len(result)%2==0 else result[1:5]

def changeValues(cte, xTemp):
    return cte * int(xTemp)

def printTable(yList, xList, cte):
    for iter in range(len(yList)):
        print "y_{0} = {1} * {2} = {3}, X_{4} = {5}, r_{4} = {6}".format(iter, cte, xList[iter], yList[iter], iter+1, xList[iter+1], float(xList[iter+1])/10000 )

def main():
    x0 = int(sys.argv[1])
    cte = int(sys.argv[2])
    qty = int(sys.argv[3])
    yList, xList = constantMultiplier(x0, cte, qty)
    printTable(yList, xList, cte)

if __name__ == "__main__":
    main()
