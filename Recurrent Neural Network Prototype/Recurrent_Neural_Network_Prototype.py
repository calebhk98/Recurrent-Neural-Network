import random
showHNData=True
def RecurrentNN(input=2, HN=[1,3], output=1, memoryCells=5, seed=None):
    '''
    This should allow a new NN easily
    input=Num of inputs to handle
    HN=[Number of layers, num of nodes in layer 1, num of nodes in layer 2...]
    Output=Num of endpoints
    memoryCells=Number of memory cells. <100 is suggested
    seed=Random factor for reproducibility can use number or words
    '''
    if (seed==None):
        seed=random.uniform(0.0, 1000.0) 
    random.seed(seed)#Creates a seed if none is selected

    Outputs=[]#An array of the outputs
    HNs=[]#An array of Hidden Nodes The first is the bais. The next input amounts are the weights. Then the next sumation (memoryCells)+memoryCells are memoryCells. This is repeated HN times
    n=0
    numOfHN=0
    for numOfHN in range(HN[0]):
        layerHN=[]#Host all the nodes of a single layer
        for (n) in range(HN[numOfHN+1]):
            testHN=[0,random.random()]#This gives all the HN a Value and a bais
            i=0
            for (i) in range(input):
                testHN.append(random.random())#This gives all the HNs a weight associated with each input
            MNs=[]#An array of Memory Nodes inside of each HN. The first is the bais. The next 1 is a weight. This then loops with the weights increases by 1 each loop
            m=0
            for (m) in range(memoryCells):
                previousData=round((numOfHN/HN[0]+(n/HN[numOfHN+1])*0.1),3)
                testMN=[0,random.random()]#This gives each memory cell a value and a bais
                for i in range(m+1):
                    testMN.append(random.random())#This gives each Memory cell a weight for the previous memory cells and the original node
                MNs.append(testMN)#Gives the memory cells their weights and Baises
                if(showHNData):
                    if(previousData<round((numOfHN/HN[0]+(n/HN[numOfHN+1])*0.1),3)):
                        print(str(round((numOfHN/HN[0]+(n/HN[numOfHN+1])*0.1),3)), end=" ")
            testHN.append(MNs)#This gives each HN their own Memory cells.
            
            layerHN.append(testHN)#This adds all the HN to an array to better keep track of them
        
        HNs.append(layerHN)#adds all of the hidden nodes to the HNs array
    print("\nMade 1 NN with "+str(input)+" inputs, "+str(HN)+" Hidden nodes ("+str(HN[0])+"layers). "+str(output)+" output nodes and "+str(memoryCells)+" memory cells. Seed is "+str(seed))
    if(showHNData):
        print("HN Data:")
        for numOfHN in range(HN[0]):#Prints the HN seperate by layer
            print("Layer "+str(numOfHN))
            for (n) in range(HN[numOfHN+1]):
                print("\nHN "+str(n)+" = " , end="")
                for i in range (input+2):#Prints the Baises and weights of all the HNs
                    print(str(HNs[numOfHN][n][i]), end=" ")
                i=0
        
                print( )#Puts the Memory cells on a new  line
                for m in range (memoryCells):#Prints the memory Cells of each HN
                    print("MC "+str(m)+": "+str(HNs[numOfHN][n][input+2][m]))#Prints the HN seperately




print("Hi")

RecurrentNN(2,[2,4,3],1,5,"Hi")
RecurrentNN()
RecurrentNN(3,[1,2],5)


