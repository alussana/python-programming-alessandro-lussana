import math

class Neuron:
    '''
    Construct a Neuron with a list of weights and a |threshold|
    '''
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

class Layer:
    '''
    Construct a Layer with a list of Neuron objects
    '''
    def __init__(self, neurons):
        self.neurons = neurons
    
    def dimensions(self):
        '''
        Return the number of neurons in the Layer
        '''
        n = len(self.neurons)
        return(n)
    
    def feedLayer(self, activation):
        '''
        Compute the output z for each neuron given a list of activation inputs
        '''
        transfer = []
        for n in range(len(self.neurons)):
            a = 0
            for w in range(len(self.neurons[n].weights)):
                e = self.neurons[n].weights[w] * activation[w]
                a = a + e
            a = a - self.neurons[n].threshold
            z = sigmoid(a)
            transfer.append(z)
        
        return(transfer)

class Network:
    '''
    Costruct a Network using a list of Layer objects 
    '''
    def __init__(self, layers):
        self.layers = layers

    def dimensions(self):
        '''
        Return the number of neurons in each Layer of the Network
        '''
        l = []
        for i in range(len(self.layers)):
            l.append(self.layers[i].dimensions())
        return(l)

    def feedNetwork(self, activation):
        l = len(self.dimensions())
        out = []
        for i in range(l):
            activation = self.layers[i].feedLayer(activation)
            out.append(activation)
        return(out)
        
def sigmoid(x):
    y = 1 / (1 + math.exp(-x))
    return(y)

if __name__ == '__main__':
    ## test XOR
    #w1_1 = [0.7, 0.7]
    #t1_1 = 0.5
    #w1_2 = [0.3, 0.3]
    #t1_2 = 0.5
    #w2_1 = [0.7, -0.7]
    #t2_1 = 0.5
    #n1_1 = Neuron(w1_1, t1_1)
    #n1_2 = Neuron(w1_2, t1_2)
    #n2_1 = Neuron(w2_1, t2_1)
    #layer1 = Layer([n1_1, n1_2])
    #layer2 = Layer([n2_1])   
    #net = Network([layer1, layer2])
    #print(net.feedNetwork([0, 1]))
    #print(net.feedNetwork([1, 0]))
    #print(net.feedNetwork([1, 1]))
    #print(net.feedNetwork([0, 0]))
    
    ## test OR
    w1_1 = [0.659, 0.659]
    t1_1 = 0.164
    n1_1 = Neuron(w1_1, t1_1)
    layer1 = Layer([n1_1])
    net = Network([layer1])
    print(net.feedNetwork([1, 0]))
    print(net.feedNetwork([0, 1]))
    print(net.feedNetwork([0, 0]))
    print(net.feedNetwork([1, 1]))