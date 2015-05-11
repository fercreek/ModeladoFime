from math import pow
import sys

def multSeeds(x0,x1,qty):
    xList = list()
    yList = list()
    seed1 = list()
    seed2 = list()

    for iteration in range(qty):
        seed1.append(x0)
        seed2.append(x1)
        y = x0*x1
        yList.append(y)
        x = int(getMiddleValues(y))
        xList.append(x)
        x0 = x1
        x1 = x

    return xList, yList, seed1, seed2

def getMiddleValues(result):
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

def printTable(xList, yList, seed1, seed2):
    for iter in range(len(yList)):
        # print "y_{0} = {1}^2 = {2}, \t X_{0} = {3}, r_{4} = {5} ".format(iter, numToSquare[iter], xList[iter],yList[iter], iter+1, ( float(yList[iter])/10000) )
        print "y_{0} = ({1}) * ({2}) = {3} x_{4} = {5}, r_{4} = {6}".format(iter,seed1[iter], seed2[iter], yList[iter], iter+1,xList[iter], ( float(xList[iter])/10000) )

def main():
    x0 = int(sys.argv[1])
    x1 = int(sys.argv[2])
    qty = int(sys.argv[3])
    xList, yList, seed1, seed2 = multSeeds(x0,x1,qty)
    printTable(xList, yList, seed1, seed2)

if __name__ == "__main__":
    main()
