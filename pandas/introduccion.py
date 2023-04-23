import pandas as pd
import numpy as np

data=np.array([['','Col1','Col2'],['Fila1',11,22],['Fila2',33,44]])
table=pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:])
print(table)
print()

print("DataFrame: ")
df=pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print(df)
print()

print("Series : ")
series=pd.Series({"Argentina":"Buenos Aires"
                  ,"Chile":"Santiago de chile"
                  ,"Colombia":"Bogota"
                  ,"Peru":"Lima"
                  })
print(series)
