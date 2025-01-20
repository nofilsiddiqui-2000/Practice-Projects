# MNIST Classification with PyTorch

Welcome to my project on MNIST classification! This project demonstrates how to build, train, and evaluate a neural network using PyTorch. The code is beginner-friendly and serves as an excellent introduction to PyTorch and deep learning.

---

## 🌟 Project Highlights
- **Dataset**: The [MNIST dataset](http://yann.lecun.com/exdb/mnist/) (Modified National Institute of Standards and Technology) is a classic benchmark dataset containing images of handwritten digits (0-9).
- **Framework**: The project leverages PyTorch for dataset handling, model creation, training, and evaluation.
- **Model Architecture**: 
  - A fully connected feedforward neural network.
  - 3 hidden layers with ReLU activation.
  - Output layer uses `log_softmax` for multi-class classification.
- **Optimizer**: Adam optimizer with a learning rate of 0.001.
- **Metrics**: Model accuracy is calculated to evaluate performance on the training data.

---

## 🚀 How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nofilsiddiqui-2000/Practice-Projects.git
   cd "Practice-Projects/MNIST Classification with Pytorch"


2. Install Dependencies:
Make sure you have Python and PyTorch installed. Then, install the required libraries:
pip install torch torchvision matplotlib


3. Run the Script:
Execute the code to train and evaluate the model: 
python mnist_classification.py

🛠 Prerequisites
Python 3.8 or higher
PyTorch 1.8.0 or higher
Matplotlib for visualizations
A basic understanding of PyTorch and machine learning concepts

📂 Repository Structure
MNIST-Classification-with-PyTorch/
├── mnist_classification.py  # Main script for training and evaluation
├── README.md                # Project description and usage guide


📊 Results
The model achieves approximately 95% training accuracy after 3 epochs.
The predictions and dataset are visualized for better understanding.

🛠 Future Improvements
Include testing on unseen data to evaluate generalization.
Experiment with Convolutional Neural Networks (CNNs) for improved accuracy.
Add a confusion matrix to analyze misclassifications.

🤝 Contributing
Feel free to fork this repository, submit pull requests, or suggest improvements! Let's learn and grow together. 😊



