#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/game-of-life/
Created on Sat Feb  2 20:42:39 2019
n_iterations: 10
gamefield:
"
                               
                               
          oo                   
          oo                   
            oo                 
            oo                 
                         o     
                         o     
                         o     
                               
                               
                               
                               
"

The config file can have other arbitrary entries.
symbol_dead: " "
symbol_alive: "o"
"""
import os
import configparser
import itertools
filePath = 'example.txt'
config = configparser.ConfigParser()
#if file not existed generate a config file
gamefield=[[0,0,0,0,0,0],
           [1,1,0,0,0,0],
           [1,1,0,0,0,0],
           [0,0,1,1,0,0],
           [0,0,1,1,0,0],
           [0,0,0,0,0,1]]
fieldMatrix=[[]]
temp=[]
def generateAFile():
    config['DEFAULT'] = {
            'n_iterations':'10',
            'gamefield':'\"'+str(gamefield)+'\"',
            'symbol_dead':'\"0\"',
            'symbol_alive':'\"1\"',
            'seed':str(gamefield).replace("],","],\n")
          }
    with open(filePath, 'w') as configfile:
        config.write(configfile)
def strToArray(matrix):
    MatrixX=0
    for number in matrix:
        if number =='0':
            fieldMatrix[MatrixX].append(0)
        elif number =='1':
            fieldMatrix[MatrixX].append(1)
        elif number == ']':
            fieldMatrix.append([])
            MatrixX+=1
    #delete empty arrays
    finalFieldMatrix = [x for x in fieldMatrix if x]
    #print(finalFieldMatrix)
    return finalFieldMatrix
    #check 2d array cell number
def checkConfigure(config):
    #Check fields are valid
    for key in config['DEFAULT']:
        if key in ['n_iterations','gamefield','symbol_dead','symbol_alive','seed']:
            continue
        else:
             print("field invalid")
             raise(ValueError)
    #gamefield:check 0 and 1
    matrix = config['DEFAULT']['gamefield']
    if '0' not in set(itertools.chain(*matrix)):
        print("gamefield must have 0")
        raise(ValueError)
    elif '1' not in set(itertools.chain(*matrix)):
        print("gamefield must have 1")
        raise(ValueError)
    #gamefield:transform string to 2d array
    finalFieldMatrix=strToArray(matrix)
    print(finalFieldMatrix)
    '''
    for i in range(len(finalFieldMatrix)):
        temp.append(len(finalFieldMatrix[i]))
        #print(temp)
    for j in temp:
        if temp[0]!=j:
            print("gamefield contains invalid symbols")
            raise(ValueError)
    '''
    #every things are great ,print keys
    for key in config['DEFAULT']: print(key)
def ex5func(filePath):
    if not os.path.isfile('./'+filePath):
        generateAFile()
        print("GameField has been generated,please execute again")
        raise(FileNotFoundError)
    else:
        print("File existed.")
    #if file is exist load file
    config.read(filePath)
    
    #print(config['DEFAULT']['gamefield'])
    checkConfigure(config)
    
    print("Ex5 is done!")
    #valid file
    return (config['DEFAULT']['n_iterations'], config['DEFAULT']['symbol_dead'], config['DEFAULT']['symbol_alive'] , config['DEFAULT']['seed'])
# run ex5
#n_iterations, symbol_dead, symbol_alive, seed = ex5func("example.txt")
#print(n_iterations, symbol_dead, symbol_alive, seed)