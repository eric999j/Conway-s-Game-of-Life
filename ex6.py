#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 12:37:20 2019
"""
import ex5
'''
current_state[i-1][j-1]
current_state[i-1][j]
current_state[i-1][j+1]

current_state[i][j-1]
current_state[i][j+1]

current_state[i+1][j-1]
current_state[i+1][j]
current_state[i+1][j+1]
'''
def ex6func(current_state, symbol_dead, symbol_alive):
    #print(current_state, symbol_dead, symbol_alive)
    current_state=ex5.strToArray(current_state)
    #print(finalFieldMatrix)
    print(current_state)
    #print(len(current_state[0]))
    alive_cell=0
    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            #print("current"+str(i),str(j))
            if(current_state[i][j]==1):
                try:
                    if(current_state[i-1][j-1]):
                        alive_cell+=1
                    if(current_state[i-1][j]):
                        alive_cell+=1
                    if(current_state[i-1][j+1]):
                        alive_cell+=1
                    if(current_state[i][j-1]):
                        alive_cell+=1
                    if(current_state[i][j+1]):
                        alive_cell+=1
                    if(current_state[i+1][j-1]):
                        alive_cell+=1
                    if(current_state[i+1][j]):
                        alive_cell+=1
                    if(current_state[i+1][j+1]):
                        alive_cell+=1
                    #print("cell:"+str(alive_cell))                    
                except IndexError:
                    pass               
                if(alive_cell<2 or alive_cell>3):
                        current_state[i][j]=0
                        alive_cell=0
                if(alive_cell==2 or alive_cell==3):
                        alive_cell=0
            if(current_state[i][j]==0):
                try:
                    if(current_state[i-1][j-1]):
                        alive_cell+=1
                    if(current_state[i-1][j]):
                        alive_cell+=1
                    if(current_state[i-1][j+1]):
                        alive_cell+=1
                    if(current_state[i][j-1]):
                        alive_cell+=1
                    if(current_state[i][j+1]):
                        alive_cell+=1
                    if(current_state[i+1][j-1]):
                        alive_cell+=1
                    if(current_state[i+1][j]):
                        alive_cell+=1
                    if(current_state[i+1][j+1]):
                        alive_cell+=1
                    #print("cell:"+str(alive_cell))
                except IndexError:
                    pass 
                if(alive_cell==3):
                    current_state[i][j]=1
                    alive_cell=0
    print(current_state)
    print("Ex6 is done!")            
    return current_state
#n_iterations, symbol_dead, symbol_alive, seed = ex5func("example.txt")
#next_state = ex6func(seed, symbol_dead, symbol_alive)
#print(str(next_state).replace("],","],\n"))