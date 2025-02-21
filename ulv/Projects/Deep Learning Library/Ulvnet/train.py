"""
Here's a fuction that can train a neural net
"""

from Ulvnet.tensor import Tensor
from Ulvnet.nn import NeuralNet
from Ulvnet.loss import Loss, MSE
from Ulvnet.optim import Optimizer, SGD
from Ulvnet.data import DataIterator, BatchIterator

def train(net: NeuralNet, 
          inputs: Tensor,
          targets: Tensor,
          num_epochs: int = 5000,
          iterator: DataIterator = BatchIterator(),
          loss: Loss = MSE(),
          optimizer: Optimizer = SGD()) -> None:
    for epoch in range(num_epochs):
        epoch_loss = 0.0
        for batch in iterator(inputs, targets):
            predicted = net.forward(batch.inputs)
            epoch_loss += loss.loss(predicted, batch.targets)
            grad = loss.grad(predicted, batch.targets)
            net.backward(grad)
            optimizer.step(net)
        print(epoch, epoch_loss)