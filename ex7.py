#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 19:59:41 2019

"""
import ex5,ex6
filePath = 'example.txt'
def ex7func(filePath):
    n_iterations, symbol_dead, symbol_alive, seed = ex5func(filePath)
    n_iterations=int(n_iterations)
    next_state=ex5.strToArray(seed)
    for i in range(n_iterations):
        next_state = ex6func(next_state,symbol_dead, symbol_alive)
        print(next_state)
    print("Ex7 is done!")
ex7func("example.txt")