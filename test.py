import torch

# Assuming you have an original tensor of shape (16, 100)
original_tensor = torch.rand(2, 3)  # Example: Filled with random numbers for demonstration

# To achieve a new shape of (48, 100) by repeating the content 3 times (for a total of 3 repetitions):
repeated_tensor = original_tensor.repeat(3, 1)

# Verifying the shape of the resulting tensor
print(repeated_tensor.shape)  # Should print torch.Size([48, 100])

print(original_tensor)
print(repeated_tensor)