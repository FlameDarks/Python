import numpy
def createData():
    data=numpy.load("gdp.npz",allow_pickle=True)
    print(data["values"])
createData()