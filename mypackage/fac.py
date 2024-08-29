#!/usr/bin/python3
def fac(n):
    if n == 1 or n == 0:
        return n
    return fac(n-1)*n
