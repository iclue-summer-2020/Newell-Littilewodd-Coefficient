import os
import sys


def parToString(par):
    res = ""
    for x in par:
        res = res + str(x) + " "
    return res


def LRCoefficient(par1, par2, par3):
    cmd = "lrcalc lrcoef " + parToString(par1) + "- " + parToString(par2) + "- " + parToString(par3)
    result = os.popen(cmd)
    return int(result.read())


def parsePartition(str):
    arg = str.split(" ")
    par = ()
    cnt = 0
    for x in arg:
        cnt += int(x)
        par = par + (int(x),)
    return par, cnt


def parseInput(filename):
    file = open(filename)
    str1 = file.read()
    strings = str1.split("\n")
    lam = parsePartition(strings[0])
    mu = parsePartition(strings[1])
    nu = parsePartition(strings[2])
    return lam, mu, nu


def partition(number):
    answer = set()
    answer.add((number,))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x,) + y))[::-1])
    return answer


def NLCoefficient(lam, mu, nu, a, b, c):
    if (a + b + c) % 2 == 1:  # no possible combinations of alpha, beta, gamma can satisfy
        print("No possible combination since the sum of the three partitions is odd")
        return 0
    d = (a + b - c) // 2
    e = (a - b + c) // 2
    f = (-a + b + c) // 2
    if d <= 0 or e <= 0 or f <= 0:
        print("No possible combination since one partition is larger than the sum of others")
        return 0
    sum = 0
    for alpha in partition(d):
        for beta in partition(e):
            coef1 = LRCoefficient(lam, alpha, beta)
            if coef1 != 0:
                for gamma in partition(f):
                    coef2 = LRCoefficient(mu, alpha, gamma)
                    if coef2 != 0:
                        coef3 = LRCoefficient(nu, beta, gamma)
                        sum += coef1 * coef2 * coef3
    return sum


(lam, a), (mu, b), (nu, c) = parseInput(sys.argv[1])
print(NLCoefficient(lam, mu, nu, a, b, c))

