from math import pow
import sys


def linealAlgorithm(a, x0, cte, N):
    lifeSpan = list()
    r = list()
    for number in range(1, N + 1):
        tempValue = ((a * x0 + cte) % N)
        lifeSpan.append(tempValue)
        r.append("%.3f" % (float(tempValue) / (N - 1)))
        x0 = tempValue
    return lifeSpan, r


def calculateValues(g, k):
    N = pow(2, g)
    a = 1 + 4 * k
    return N, a

def printTable(lifeSpan, r, a, x0, cte, N):
    print "x_0 = ", x0
    xRepeat = x0
    for iter in range(len(lifeSpan)):
        print "x_{0} = ({1}*{2}+{3})mod({4}) = {5}, r_{0} = {6}".format(iter+1, a, xRepeat,cte, N, lifeSpan[iter],  r[iter])
        # print "lifeSpan", lifeSpan[iter], "r(x)", r[iter]
        xRepeat = lifeSpan[iter]
def main():
    g = int(sys.argv[1])
    k = int(sys.argv[2])
    x0 = int(sys.argv[3])
    cte = int(sys.argv[4])
    N, a = calculateValues(g, k)
    N = int(N)
    a = int(a)

    lifeSpan, r = linealAlgorithm(a, x0, cte, N)
    printTable(lifeSpan, r, a, x0, cte, N)

if __name__ == "__main__":
    main()
