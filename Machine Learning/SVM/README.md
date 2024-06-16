# Support Vector Machines (SVM)

## Overview
Support Vector Machines (SVM) are a set of supervised learning methods used for classification, regression, and outliers detection. The advantages of support vector machines are:
•  Effective in high dimensional spaces.

•  Still effective in cases where the number of dimensions is greater than the number of samples.

•  Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

•  Versatile: different Kernel functions can be specified for the decision function.


## How SVM Works
SVM constructs a hyperplane or set of hyperplanes in a high or infinite-dimensional space, which can be used for classification, regression, or other tasks. Intuitively, a good separation is achieved by the hyperplane that has the largest distance to the nearest training data points of any class (so-called functional margin), since in general the larger the margin, the lower the generalization error of the classifier.

## Installation
To use the SVM library in your project, you'll need to install the required packages via pip:
```bash
pip install scikit-learn
