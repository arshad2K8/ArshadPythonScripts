__author__ = 'arshad'


def main():
    print 'Inside main'

def getFinalAmountAfterCompounInterest(P, r, n, t):
    #P (1 + r/n) (nt)
    A = P * (1 + r/n) ** (n*t)
    return A

if __name__ == "__main__":
    print 'hello'
    main()

    #A = P (1 + r/n) (nt)
    #r = the annual interest rate (decimal)
    #n = the number of times that interest is compounded per year
    P = 150000
    r = 6.9/100 #9%
    n = 4
    t = 10
    print 'Final amount is', getFinalAmountAfterCompounInterest(P, r, n, t)


