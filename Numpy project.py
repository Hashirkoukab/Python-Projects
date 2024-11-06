#!/usr/bin/env python
# coding: utf-8

# Project: Cleaning and Analyzing Student Scores with NumPy

# In[1]:


# Things to do


# Clean and analyze data with NumPy.
# Create a dataset with some missing values.
# Replace missing values with the average score.
# Calculate and display some basic statisics.


# Setup Data

# In[2]:


import numpy as np


# In[3]:


# Sample scores, with None for missing values
scores = np.array ([95, 88, None, 76, 84, None, 91, 87, 100, 79])
print("Original scores with missing values:", scores)


# In[4]:


# Calculate average without None values
filtered_scores = [s for s in scores if s is not None]
average_score = sum(filtered_scores) / len(filtered_scores)


# In[5]:


# Replace None with the average score
cleaned_scores = np.array([s if s is not None else average_score for s in scores])
print("Scores after replacing missing values with average:", cleaned_scores)


# Analyze Data

# In[6]:


# Calculate statistics
mean_score = np.mean(cleaned_scores)
max_score = np.max(cleaned_scores)
min_score = np.min(cleaned_scores)

print("Mean score:", mean_score)
print("Max score:", max_score)
print("Min score:", min_score)

