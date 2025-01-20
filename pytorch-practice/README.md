# CIFAR-10 Image Classification with PyTorch

This project demonstrates a simple convolutional neural network (CNN) implementation to classify images from the CIFAR-10 dataset using PyTorch. The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 classes, with 6,000 images per class.

## Features

- **Dataset Preparation**: Downloads and prepares CIFAR-10 dataset for training and testing.
- **Model Architecture**: Implements a basic CNN model with two convolutional layers and three fully connected layers.
- **Training**: Trains the CNN using the SGD optimizer and CrossEntropy loss function.
- **Evaluation**: Visualizes sample inputs and evaluates model performance.

## Requirements

- Python 3.7 or higher
- PyTorch
- torchvision
- matplotlib
- numpy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cifar10-classification.git
   cd cifar10-classification

2. Install the required Python packages:
   ```bash
   pip install torch torchvision matplotlib numpy

## Running the Project
1. Dataset Loading: The script will automatically download the CIFAR-10 dataset and preprocess it.
2. Training: Run the training loop to train the model for 2 epochs. Training statistics are printed after every 2,000 mini-batches.
3. Saving the Model: After training, the model is saved to cifar_net.pth.
4. Visualization: The script includes utilities to visualize sample images and their corresponding predictions.

## Code Overview
- Dataset Preparation: Loads CIFAR-10 using torchvision.datasets.CIFAR10 and normalizes images.
- Model Definition: Net class defines the CNN architecture.
- Training Loop: Optimizes the network parameters using SGD and computes training loss.
- Utilities:
  - imshow: Helper function to visualize images.
  - Saving and loading the trained model.
 
## Sample visualization:
- Displays a grid of CIFAR-10 images with corresponding predicted labels.

## Future Work
- Implement a validation loop for real-time evaluation during training.
- Add data augmentation techniques for improved performance.
- Experiment with different optimizers and learning rate schedules.

## License
- This project is open-source and available under the MIT License.

