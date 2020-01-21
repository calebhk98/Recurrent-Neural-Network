import random
def RecurrentNN(input=2, HN=3, output=1, seed=None):
    '''
    This should allow a new NN easily
    input=Num of inputs to handle
    HN=Num of hidden nodes
    Output=Num of endpoints
    seed=Random factor for reproducibility can use number or words
    '''
    if (seed==None):
        seed=random.uniform(0.0, 1000.0) 
    random.seed(seed)
    HNs=[[random.random()]]#An array of Hidden Nodes The first is the bais while the second is the weight
    for i in range(input):
        HNs[0].append(random.random())
    n=1
    for (n) in range(HN):
        testHN=[random.random()]
        for i in range(input):
            testHN.append(random.random())
        HNs.append(testHN)
    
    print("Made 1 NN with "+str(input)+" inputs, "+str(HN)+" Hidden nodes, and "+str(output)+" output nodes. Seed is "+str(seed))
    
    for (n) in range(HN):
        print("HN "+str(n)+" = "+str(HNs[n]))


print("Hi")
RecurrentNN()
RecurrentNN(3,2,5)
RecurrentNN(1,4,3,10)

RecurrentNN(1,4,3,"Hi")
