#!/usr/bin/env python3.6
import os
import sys
import datetime

global dictionary
global dict1
dictionary = {}
dict1 = {}


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


def partition(number, height):
    global miss
    if (number, height) in dictionary:
        return dictionary[(number, height)]
    if height == 1:
        ans = set()
        ans.add((number,))
        dictionary[(number, height)] = ans
        return ans
    answer = set()
    answer.add((number,))
    for x in range(1, number):
        for y in partition(number - x, height - 1):
            answer.add(tuple(sorted((x,) + y))[::-1])
    dictionary[(number, height)] = answer
    return answer


def NLCoefficient(lam, mu, nu, a, b, c):
    if (a + b + c) % 2 == 1:  # no possible combinations of alpha, beta, gamma can satisfy
        print("No")
        return 0
    d = (a + b - c) // 2
    e = (a - b + c) // 2
    f = (-a + b + c) // 2
    if d <= 0 or e <= 0 or f <= 0:
        print("NO")
        return 0
    sum = 0
    for alpha in partition(d, min(len(lam), len(mu))):
        for beta in partition(e, min(len(lam), len(nu))):
            if (lam, alpha, beta) in dict1:
                coef1 = dict1[(lam, alpha, beta)]
            else:
                coef1 = LRCoefficient(lam, alpha, beta)
                dict1[(lam, alpha, beta)] = coef1
            if coef1 != 0:
                for gamma in partition(f, min(len(nu), len(mu))):
                    if (mu, alpha, gamma) in dict1:
                        coef2 = dict1[(mu, alpha, gamma)]
                    else:
                        coef2 = LRCoefficient(mu, alpha, gamma)
                        dict1[(mu, alpha, gamma)] = coef2
                    if coef2 != 0:
                        if (nu, beta, gamma) in dict1:
                            coef3 = dict1[(nu, beta, gamma)]
                        else:
                            coef3 = LRCoefficient(nu, beta, gamma)
                            dict1[(nu, beta, gamma)] = coef3
                        sum += coef1 * coef2 * coef3
    return sum


if __name__ == '__main__':
    (lam, a), (mu, b), (nu, c) = parseInput(sys.argv[1])
    print(datetime.datetime.now())
    print(NLCoefficient(lam, mu, nu, a, b, c))
    print(datetime.datetime.now())

