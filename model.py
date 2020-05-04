from Layers import create_data, Layer_Dense
from Activations import Activation_ReLU, Activation_Softmax

# Create Dataset
# dimensions of the inputs is (100, 2)
X, y = create_data(100, 3)

# Create Dense layer with 2 input features and 3 output values
# first dense layer, 2 inputs (each sample has 2 featues), 3 outputs
dense1 = Layer_Dense(2, 3)

# Create a ReLU activation (to be used with dense layer)
activation1 = Activation_ReLU()

# Create a second Dense layer with 3 input features (as we take output
# of previous layer here) and 3 output values
dense2 = Layer_Dense(3, 3)  # second dense layer, 3 inputs, 3 outputs

# Create a Softmax activation (to be used with Dense layer)
activation2 = Activation_Softmax()

# Make a forward pass of our training data through this layer
# the outputs are of the dimension (100, 3) [dot((100, 2), (2, 3))]
dense1.forward(X)

# Fwd pass through the actv function, takes output from previous layer
# dimension of output from the ReLU is (100, 3)
activation1.forward(dense1.output)

# Make a forward pass through second dense layer - takes the output
# of the first activation function as the inputs
# dimension of output from this layer is (100, 3)
dense2.forward(activation1.output)

# Make a forward pass through the activation function - takes
# the output of the previous layer
activation2.forward(dense2.output)

# Outputs of the first few samples
print(activation2.output[:5])