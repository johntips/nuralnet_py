#coding: utf-8
import neuralNetwork
import saveLogger

########  initial params ####

# inputlayer ,hiddenlayer, outputlayer, learning_rate, epoch
input_nodes = 784
hidden_nodes = 100
output_nodes = 10
learning_rate = 0.1
epock = 5
# array data
finalscore = []
finalscore_array = []

########  main logic  #######

nuralnetwork_instance = neuralNetwork.create(input_nodes,hidden_nodes,output_nodes,learning_rate)
set_train_data()
set_test_data()
get_score()
#log = saveLogger.save_params(date,input_nodes,hidden_nodes,output_nodes,learning_rate,epoch,score)

########  output view #######

print(score)

########  methods    ########

def set_train_data():

    training_data_file = open("mnist_data/mnist_train.csv",'r')
    training_data_list = training_data_file.readlines()
    training_data_file.close()

    for epoch in range(epochs):
        for record in training_date_list:
            arranged_values = record.split(',')

            #scaling,shift
            inputs = (numpy.asfarray(arranged_values[1:] / 255.0 *0.99 +0.01 ))
            #creationg targets
            targets = numpy.zeros(output_nodes) + 0.01
            #label handling
            targets[int(all_values[0] = 0.99
            #call train method
            nuralnetwork_instance.train(inputs, targets)

            pass
        pass

def set_test_data():

    test_data_file = open("mnist_data/mnist_test.csv", 'r')
    test_data_list = test_data_file.readlines()
    test_data_file.close()

    for record in test_data_list:
        arranged_values = record.split(',')

        #CORRECT LABEL is top
        correct_label = int(arranged_values[0])
        #scaling, shift
        inputs = numpy.asfarray(arranged_values[1:) / 255.0 *0.99) + 0.01

        #REFER TO NETWORK
        outputs = nuralnetwork_instance.query(inputs)
        label = numpy.argmax(outputs)
        # True = 1 False = 0 
        # ADD in list

    if( label == correct_label):
        finalscore.append(1)
    else:
        finalscore.append(0)
        pass
    pass

def get_score:
    finalscore_array = numpy.asarray(finalscore)
    print("perfomance score is =", finalscore_array.sum() / finalscore_array.size)