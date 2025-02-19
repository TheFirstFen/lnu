"""
Our neural nets will be made up of layers.
Each layer needs to pass its input forward 
and propagate gradients backward. For example:
a neural net might look like

inputs -> Linear -> Tanh -> Linear -> output
"""
from typing import Dict
import numpy as np

from net.tensor import Tensor

class Layer:
    def __init__(self) -> None:
        self.params: Dict[str, Tensor] = {}

    def forward(self, inputs: Tensor) -> Tensor:
        """
        Produce the output corresponding to these inputs
        """
        raise NotImplementedError
    
    def backward(self, grad: Tensor) -> Tensor:
        """
        Backpropagate this gradient through the layer
        """
        raise NotImplementedError
    
class Liner(Layer):
    """
    Computes output = inputs @ w + b
    """
    def __init__(self, input_size: int, output_size: int) -> None:
        # inputs will be (batch_sice, input_size)
        # outputs will be (batch_size, output_size)
        super.__init__()
        self.params["w"] = np.random.randn(input_size, output_size)
        self.params["b"] = np.random.randn(output_size)

    def forward(self, inputs: Tensor) -> Tensor:
        """
        Outputs = inputs @ w + b
        """
        self.input = inputs
        return inputs @ self.params["w"] + self.params["b"]
    
    def backward(self, grad: Tensor) -> Tensor:
        """
        if y = f(x) = a *b + c
        then dy/da = f'(x) * b
        and dy/db = f'(x) * a
        and dy/dc = f'(x)

        if y = f(x) and x = a @ b + c
        then dy/da = f'(x) @ b.T
        and dy/db = a.T @ f'(x)
        and dy/dc = f'(x)
        """

