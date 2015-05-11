from math import pow
import sys

def multiplication(a, x0, m, N):
    m = int(m)
    N = int(N)
    xList = list()
    r = list()
    for iter in range(N):
        x = (a * x0)%m
        xList.append(x)
        r.append((x/float(m-1)))
        x0 = x
    return xList, r

def printTable(xList, r, x0, a, m):
    print "x_0 = ", x0
    for iter in range(len(xList)):
        print "x_{0} = ({1}*{2})mod({3}) = {4}, r_{0} = {5}".format(iter+1, a, x0 ,int(m), xList[iter],  r[iter])
        x0 = xList[iter]

def main():
    x0 = int(sys.argv[1])
    k = int(sys.argv[2])
    g = int(sys.argv[3])
    a = 5 + 8*k
    m = pow(2, g)
    N = m/4
    xList, r = multiplication(a, x0, m, N)
    printTable(xList, r, x0, a, m)

if __name__ == "__main__":
    main()
