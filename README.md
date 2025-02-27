# Diabetes Prediction API

This project uses a Random Forest machine learning classification model to predict the type of diabetes in individuals. The model leverages a large dataset with various health-related features such as "HighBP", "HighChol", "BMI", "HeartDiseaseorAttack", "GenHlth", "PhysHlth", "DiffWalk", and "Age". The main focus of this project is the development of an API that handles all of the predictions.

## Project Features

- **Random Forest Classifier:** The backend uses a Random Forest machine learning model to predict diabetes types based on health data.
- **API Endpoints:** The project provides an API with the following endpoints:
  - **`/model_info`:** Provides information about the trained model.
  - **`/prediction`:** Makes a prediction based on input data.
  - **`/performance`:** Displays the performance metrics of the model.
  - **`/figure`:** Generates and returns a figure (e.g., a graph or chart) related to the model's performance.

## Project Structure

The project includes the following files:

- **`master.yml`**: The YAML configuration file.
- **`random_forest_model_with_pipe(2).pkl`**: The trained Random Forest model with a pipeline.
- **`README.md`**: This file with setup instructions and project details.
- **`requirements.txt`**: The list of required dependencies for the project.
- **`server.py`**: The entry point for running the API server.
- **`X_diabetes.csv`**: The feature dataset for diabetes prediction.
- **`Y_diabetes.csv`**: The target labels dataset for diabetes prediction.
- **`src/`**: Contains the source code including:
  - **`model.py`**: The script for loading and using the trained model.


### Prerequisites
Ensure that you have Python installed on your system. You will also need to install the dependencies listed in the `requirements.txt` file.
