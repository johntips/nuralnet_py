import numpy
import scipy.special

#import matplotlib.pyplot
#%matplotlib inline

class create:
    
    #i .init
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # input, hidden, output nodes
        self.i_nodes  = inputnodes
        self.h_nodes = hiddennodes
        self.o_nodes = outputnodes
        
        #1.settings  link weight matrix
        
        ## weight1(hidden * input) , 
        self.weight_hiddenToInput = numpy.random.normal(0.0, pow(self.h_nodes, -0.5),(self.h_nodes, self.i_nodes))
        ## weight2(output * hidden)
        self.weight_outputToHidden = numpy.random.nomal(0.0, pow(self.o_nodes, -0.5), (self.o_nodes, self.h_nodes))

        #2.settings  learning rate
        self.learningrate = learningrate
        
        #3. activation function = sigmoid function
        #CAN FIX OTHER ACTIVATION FUNCTIONS
        self.activation_function = lambda x:scipy.special.expit(x)
        pass
         
    #ii. train data method
    def train(self, inputs_list, targets_list):
        #fix list to matrix
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        
        #calculate Tohidden inputs 
        hidden_inputs = numpy.dot(self.weight_hiddenToInput, inputs)
        #get outputs  by activationfunction that jointed hidden layers
        hidden_outputs= self.activation_function(hidden_inputs)
        
        #calculate toOutput 
        finish_inputs = numpy.dot(self.weight_outputToHidden, hidden_outputs)
        #get outpus by activationfunction that jointed output layers
        finish_outputs = self.activation_function(finish_inputs)
        
        # output errors = targets - final_outputs
        output_errors = targets - final_outputs
        
        # separete hidden layer errors by link weight 
        hidden_errors = numpy.dot(self.weight_outputToHidden, output_errors)
        
        #update link weight between inputlayer and hiddenlayer
        self.weight_hiddenToInput += self.learningrate * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
         #update link weight between hiddenlayer and outputlayer
        self.weight_outputToHidden += self.leaingrate * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        
        pass

    #refer to neuralnetwork
    def query(self, inputs_list):

        #convert list to matrix
        inputs = numpy.array(inputs_list, ndmin=2).T

        #calculate hiddeninputs
        hidden_inputs = numpy.dot(self.weight_hiddenToInput, inputs)
        #put jointed hidden_outputs by activationfunction
        hidden_outputs = self.activation_function(hidden_inputs)

        #calculate outputs
        finish_inputs = numpy.dot(self.weight_outputToHidden, hidden_outputs)
        #put jointed finish_outputs by activationfunction
        finish_outputs = self.activation_function(finish_inputs)
        
        return finish_outputs