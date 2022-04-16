import os
import pandas as pd
import numpy as np
import statistics

class Filament():

    def __init__(self,colData, color:str):
        self.color = color  # Defining colors
        # Filtering Data
        self.test1 = self.findData(colData, self.color, "1")    # Selecting Data for Test 1
        self.test2 = self.findData(colData, self.color, "2")    # Selecting Data for Test 1
        self.test3 = self.findData(colData, self.color, "3")    # Selecting Data for Test 1

        self.formatedData, self.std = self.formatData(self.test1,self.test2,self.test3)

    def findData(self,colData,color:str,test:str):
        fdData = []
        for i in range(len(colData)):
            # Searching for Red and then the test number
            if color in colData.values[i][0]:
                if test in colData.values[i+1][0]:
                    for j in range(7):
                        filterData = colData.values[j+i+2][0].split(",")
                        filterData.pop(0)
                        fdData.append(filterData)

                    return fdData
    
    def formatData(self,test1,test2,test3):
        data = []
        std = []
        # assigns the dimensions and their 
        for i in range(7):
            newline = []
            newStd = []
            for j in range(4):
                newline.append([int(numeric_string) for numeric_string in [test1[i][j],test2[i][j],test3[i][j]]])
                newStd.append(statistics.stdev(newline[j]))
            data.append(newline)
            std.append(newStd)
        return data, std

    def calcStd(self,data):
        pass



def main():
    dataFid = os.path.basename('./data.csv')    # Data Location

    with open(dataFid,'r') as f:
        colData = pd.read_csv(f,delimiter='\r')

    redData = Filament(colData, "Red")
    print(redData)

if __name__ == "__main__":
    main()