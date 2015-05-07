from math import pow
import sys


def constantMultiplier(x0, cte, qty):

    arr = list()
    var = ""

    for number in range(1, qty + 1 ):
        result = calculateValues(cte, x0)
        arr.append(result)
        # var = str(calculateValues(cte, x0))
    # print var[2:6] if len(var)%2==0 else var[1:5]
    print arr

def calculateValues(cte, x0):
    return cte * x0

def main():
    x0 = int(sys.argv[1])
    cte = int(sys.argv[2])
    qty = int(sys.argv[3])
    constantMultiplier(x0, cte, qty)

if __name__ == "__main__":
    main()
