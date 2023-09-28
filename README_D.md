# Model Deployment Guide

This guide will walk you through the steps needed to deploy the wine quality prediction model.

## Requirements
- Python 3.7+
- Scikit-learn
- Joblib (for loading the trained model)

## Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/slvrxx/DS-Proj_HW

cd wine_quality_analysis
pip install scikit-learn joblib

import joblib

model = joblib.load('Modeling/trained_model.pkl')
# Now you can use the model for predictions

