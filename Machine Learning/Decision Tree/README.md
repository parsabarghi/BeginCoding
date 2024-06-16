# Decision Trees

## Introduction
Decision Trees are a non-parametric supervised learning method used for classification and regression tasks. They are powerful models that predict the value of a target variable by learning simple decision rules inferred from the data features.

## How Decision Trees Work
A Decision Tree is a flowchart-like tree structure where an internal node represents a feature(or attribute), the branch represents a decision rule, and each leaf node represents the outcome. The topmost node in a tree is known as the root node. It learns to partition on the basis of the attribute value. It partitions the tree in a recursive manner called recursive partitioning.

The key concept in a Decision Tree is to use a tree-based model to make predictions. The model is built by:
1. Selecting the best attribute using Attribute Selection Measures(ASM) to split the records.
2. Making that attribute a decision node and breaking the dataset into smaller subsets.
3. Starting tree building by repeating this process recursively for each child until one of the condition will match:
•  All the tuples belong to the same attribute value.

•  There are no more remaining attributes.

•  There are no more instances.


The decision rules are generally in form of:


![image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5eApvBtA8Fu6iQMYnEwBmdhb9hPcxOxkmqg&s)

## Features of Decision Trees
•  Simple to understand and interpret.

•  Requires little data preparation.

•  Able to handle both numerical and categorical data.

•  Uses a white box model.
