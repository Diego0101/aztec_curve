# AZTEC 1.0
#    aztec(data)
#    Reorders data through AZTEC space-filling curve.
#       INPUTS> data: data to be reordered  it should be 4^2n length.
#       OUTPUTS>outputData: data reordered with Aztec curve
#               aztecInd: vector with aztec indexes
#  Example1: outputData, aztecInd = aztec(np.r_[0:16])
# Author(s): Diego Ayala (https://github.com/Diego0101)
# Paper: https://www.researchgate.net/publication/362386088_Aztec_curve_proposal_for_a_new_space-filling_curve
# Most of algorithm from: https://arxiv.org/abs/2207.14345v1
# Published in Github through GNU GENERAL PUBLIC LICENSE
import numpy as np
import matplotlib.pyplot as plt
def aztec(data):

    
    a1 = -1.5 - 1.5j;a2 = -1.5 - 0.5j;a3 =   -1.5 + 0.5j;a4 = -1.5 + 1.5j; # Generate point sequence
    a5 = -0.5 - 1.5j;a6 = -0.5 - 0.5j;a7 = -0.5 + 0.5j;a8 = -0.5 + 1.5j;
    u = 0; #geometry=0;
    

   
    order = int(np.log2(data.size) / np.log2(16))
    rowNumel = int(np.sqrt(data.size))
    for k in range(order):
        v = -1j * np.flip(u)
        u = np.array([v+a1,v+a2,v+a3,u+a4,u+a8,u-a5,u-a1,-v-a2,-u-a3,-u-a7,v-a6,-v+a7,-v+a6,-v+a5,u-a8,u-a4])/4
        u=u.flatten()
        width=pow(4,k+1)
        u=np.reshape(u,(width,width))
    newCol = np.real(u)
    newRow = np.imag(u)
    newCol = rowNumel * newCol + rowNumel / 2 + 0.5
    newRow = rowNumel * newRow + rowNumel / 2 + 0.5
    aztecInd = ((newCol - 1) * rowNumel + newRow-1).flatten().astype(int)

    outputData=data.flatten()
    outputData=outputData[aztecInd]
    outputData=np.reshape(outputData,(width,width))
    u=u.flatten()
    D=plt.plot(np.real(u), np.imag(u))
    return outputData, aztecInd


# Example usage
#data = np.random.randint(0, 10, (16, 16))
data = np.r_[0:256]
outputData, aztecInd = aztec(data)
print("Input data:") , print(data)
print("Output data:") , print(outputData)
#print("Aztec indices:"), print(aztecInd)
plt.show() 

# Copyright (c) 2019-2099 Diego Ayala
