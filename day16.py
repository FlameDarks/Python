import numpy as np

def createData():
    data=np.load("gdp.npz",allow_pickle=True)
    print(data["values"])
createData()