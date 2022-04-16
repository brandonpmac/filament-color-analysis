from curses import color_content
from inspect import Parameter
import pandas as pd
import os
import filamentAnalysisClass as fac
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

def main():
    dataFid = os.path.basename('./data.csv')    # Data Location

    with open(dataFid,'r') as f:
        colData = pd.read_csv(f,delimiter='\r')

    # Organizing data
    redData = fac.Filament(colData,"Red")
    blueData = fac.Filament(colData,"Blue")
    yellowData = fac.Filament(colData,"Yellow")
    greenData = fac.Filament(colData,"Green")

    # Formating Data
    colorDef = ['Red','Blue','Yellow','Green']
    colorMat = np.tile(np.repeat(colorDef,28),1)
    tempMat = np.tile(np.repeat([220,215,210,205,200,195,190],4),4)
    precisionMat = []
    for color in colorDef:
        for i in range(7):
            for j in range(4):
                if color == 'Red':
                    precisionMat.append(redData.std[i][j])
                elif color == 'Blue':
                    precisionMat.append(blueData.std[i][j])
                elif color == 'Yellow':
                    precisionMat.append(yellowData.std[i][j])
                elif color == 'Green':
                    precisionMat.append(greenData.std[i][j])


    # Creating Data Frame
    df = pd.DataFrame({
        'Color' : colorMat,
        'Temp' : tempMat,
        'Precision' : precisionMat
    })

    model = ols('Precision ~ C(Color) + C(Temp) + C(Color):C(Temp)',data=df).fit()
    sm.stats.anova_lm(model,typ = 2)


    return True


if __name__ == "__main__":
    print(main())
