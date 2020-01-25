import random
showHNData=False
showTraining=False
class RecurrentNN:
    '''
    This should allow a new NN easily
    input=Num of inputs to handle
    HN=[Number of layers, num of nodes in layer 1, num of nodes in layer 2...]
    Output=Num of endpoints
    memoryCells=Number of memory cells. <100 is suggested
    seed=Random factor for reproducibility can use number or words
    '''
    def __init__(self, input=2, HN=[1,3], output=1, memoryCells=5, seed=None):
        if (seed==None):
            seed=random.uniform(0.0, 1000.0) 
        random.seed(seed)#Creates a seed if none is selected
        self.numOfMemoryCells=memoryCells
        self.numOfOutputs=output
        self.numOfHiddenLayers=HN[0]

        self.Outputs=[]#An array of the outputs
        self.HNs=[]#An array of Hidden Nodes The first is the bais. The next input amounts are the weights. Then the next sumation (memoryCells)+memoryCells are memoryCells. This is repeated HN times
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
        
            self.HNs.append(layerHN)#adds all of the hidden nodes to the HNs array
        n=0
        for n in range(output):
                testOutput=[0,random.random()]#This gives all the Outputs a Value and a bais
                i=0
                for (i) in range(HN[HN[0]]):
                    testOutput.append(random.random())#This gives all the Outputs a weight associated with the last layer of the HN
                
            
                self.Outputs.append(testOutput)#This adds all the Outputs to an array to better keep track of them


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
                        print("MC "+str(m)+": "+str(HNs[numOfHN][n][input+2][m]))#Intializes each neural Network

    def train(self):
        n=0
        numOfHiddenLayers=self.numOfHiddenLayers
        numOfOutputs=self.numOfOutputs        
        lastHiddenLayer=self.HNs[numOfHiddenLayers-1]
        numOfMemoryCells=self.numOfMemoryCells
        if(showTraining):
            print("Outputs.length():" +str(len(self.Outputs)))
            print("HNs.length():" +str(len(self.HNs)))
            print("numOfHiddenLayers:" +str(numOfHiddenLayers) )    #Debugging
        for n in range(numOfOutputs):
            i=0
            if(showTraining):
                print("N:" +str(n))#Debugging

            for i in range(len(lastHiddenLayer)):
                self.Outputs[n][0]=self.HNs[numOfHiddenLayers-1][i][0]*self.Outputs[n][i+2]+self.Outputs[n][1]
                #Each output is updated by the previous Hidden layer nodes values multiplied by the weight and added the bias           
                if(showTraining):
                    print("HNs[HNs.length()]["+str(i)+"][0]:" +str(self.HNs[len(self.HNs)-1][i][0]))                
                    print("Outputs["+str(n)+"]["+str(i+2)+"]:" +str(self.Outputs[n][i+2]))#Debugging
                t=0#Finds the value for the output.
            i=0
            #self.HNs[layer][node][variable]=5
            self.HNs[0][0][0]=5
            self.HNs[0][1][0]=3
            for i in ((reversed(self.HNs[0]))):
                print("The value is "+str(i[0]))
            #for i in range(memoryCells):
             #   self.Outputs[n][0]=self.HNs[len(self.HNs)-1][i][0]*self.Outputs[n][i+2]+self.Outputs[n][1]
                #Each output is updated by the previous Hidden layer nodes values multiplied by the weight and added the bias           
            #    if(showTraining):
            #        print("HNs[HNs.length()]["+str(i)+"][0]:" +str(self.HNs[len(self.HNs)-1][i][0]))                
            #        print("Outputs["+str(n)+"]["+str(i+2)+"]:" +str(self.Outputs[n][i+2]))#Debugging
            #    t=0#Finds the value for the output.



                
                
            
        print("1 Layer done")






print("Hi")
n=RecurrentNN(2,[1,3],1,5,"Hi")
v=RecurrentNN()
#RecurrentNN(40000,[5,100,100,64,64,64],40000,45)

n.train()
v.train()