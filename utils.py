# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:57:59 2020

@author: eloy.chang
"""

def sqrt(n, tol = 1):
    left = 0
    right = n
    ready = False
    while not ready:
        middle = (right + left) / 2
        rootCandidate = middle * middle
        if rootCandidate == n:
            return middle
        elif rootCandidate < n:
            left = middle
        else:
            right = middle
        ready = (right - left) < tol
    return (right + left) / 2
