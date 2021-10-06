import torch
from torch import nn
from torch import tensor

x_data = tensor([[1.0], [2.0], [3.0]])
y_data = tensor([[2.0], [4.0], [6.0]])
hours_of_study = 4.0

# Steps to create a Neural Network
# Step 1: Design the Model using classes
# Step 2: Define a loss function and optimizer
# Step 3: Train your model

class Model(nn.Module):
    def __init__(self):
        """
        In the constructor we instantiate two nn.Linear module
        """
        # Initializing the Model with the class
        super(Model, self).__init__()
        # torch.nn.Linear applies a Linear transformation. The first parameter is the size of each input sample. The second is the size of the output sample
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        """
        In the forward function we accept a Variable of input data and we must return
        a Variable of output data. We can use Modules defined in the constructor as
        well as arbitrary operators on Variables.
        """
        y_pred = self.linear(x)
        return y_pred


# Our model
model = Model()

# Construct our loss function and an Optimizer. The call to model.parameters()
# in the SGD constructor will contain the learnable parameters of the two
# nn.Linear modules which are members of the model.
loss_function = torch.nn.MSELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Other optimizers: torch.optim.Adagrad, torch.optim.Adam, torch.optim.Adamax, torch.optim.ASGD, torch.optim.LBFGS, torch.optim.RMSprop, torch.optim.Rprop, torch.optim.SGD

# Training loop
for epoch in range(500):
    # 1) Forward pass: Compute predicted y by passing x to the model
    y_pred = model(x_data)

    # 2) Compute and print loss
    # Both y_pred and y_data are tensors
    loss = loss_function(y_pred, y_data)
    print(f'Epoch: {epoch} | Loss: {loss.item()} ')

    # Zero gradients, perform a backward pass, and update the weights.
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


# What we are trying to do is predict the score if we have x hours of study
hour_var = tensor([[hours_of_study]])
y_pred = model(hour_var)
print("Prediction (after training)",  hours_of_study, model(hour_var).data[0][0].item())