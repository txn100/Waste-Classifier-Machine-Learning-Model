
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)
![TensorFlow Badge](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=fff&style=flat)
![Keras Badge](https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=fff&style=flat)
![JavaScript Badge](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000&style=flat)
![HTML5 Badge](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=fff&style=flat)
![CSS3 Badge](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=fff&style=flat)

# Waste Classification Project https://waste-management-model.pacifictrout.com

This project focuses on the classification of waste into two categories: Organic (O) and Recyclable (R). The classification is done using a deep learning model built with TensorFlow and Keras.

## Table of Contents

- [Background](#background)
- [Model Architecture](#model-architecture)
- [Optimizations](#optimizations)
- [Evaluation](#evaluation)
- [Usage](#usage)
- [Contribution](#contribution)

## Background

In today's world, waste management is becoming increasingly important. Differentiating between organic and recyclable waste is a foundational step in waste management processes. This project aims to automate the classification process using deep learning.

## Model Architecture

The model is built using the **Keras** library on top of **TensorFlow**. The architecture involves:

- **Three Convolutional Layers**: To extract features from the images.
  - Activation function used: *ReLU* (Rectified Linear Unit)
  - MaxPooling is used after each convolutional layer to reduce spatial dimensions.
  
- **Dense Fully Connected Layers**: To perform classification based on the features extracted by the convolutional layers.
  - Dropout is used for regularization to prevent overfitting.
  
- **Sigmoid Activation Function**: As this is a binary classification problem, a sigmoid activation function is used in the output layer.

## Optimizations

- **ImageDataGenerator**: Used for data augmentation to artificially increase the size of the training set and introduce variance.
- **Dropout Layers**: Introduced to prevent overfitting and improve model generalization.
- **RMSprop Optimizer**: Chosen for its adaptive learning rate properties, which aids faster convergence.

## Evaluation

The model was trained on a dataset containing thousands of labeled images. It achieved an accuracy of **93.269%** on the training set and **91.43%** on the test set. While these numbers are promising, continuous evaluation and tuning are crucial for further improvements.

## Usage

To use this model, simply:

1. Clone the repository.
2. Ensure you have the required libraries installed.
3. Run the flask app and upload an image for classification.


## Data Sources
A big thank you to the contributors of the datasets that made this project possible.

Waste Classification Data: This dataset was instrumental for training my waste classification model. You can find and explore the dataset in detail on Kaggle. (https://www.kaggle.com/datasets/techsash/waste-classification-data)
## Contribution

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

---



