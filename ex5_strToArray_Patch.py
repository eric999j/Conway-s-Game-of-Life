'''
程式區段
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
參考
import json 
s="[1,2,3]"
l=json.loads(s)
print(l)
'''
import json 
def strToArray(matrix):
    return json.loads(matrix)
