from math import pow
import sys

def linealAlgorithm(a, x0, cte, N ):
    lifeSpan = list()
    r = list()
    for number in range(1,N+1):
        tempValue = ((a*x0+cte)%N)
        lifeSpan.append(tempValue)
        r.append("%.3f" % (float(tempValue)/(N-1)))
        x0 = tempValue
    for value in range(len(lifeSpan)):
        print "lifeSpan", lifeSpan[value], "r(x)", r[value]

def calculateValues(g, k ):
    N = pow(2,g)
    a = 1 + 4*k
    return N,a

def main():
    g = int(sys.argv[1])
    k = int(sys.argv[2])
    x0= int(sys.argv[3])
    cte = int(sys.argv[4])   
    N,a = calculateValues(g, k)
    N = int(N)
    a = int(a)

    linealAlgorithm(a, x0, cte, N)

if __name__ == "__main__": 
    main()



