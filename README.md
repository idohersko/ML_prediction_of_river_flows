# ML Prediction of River Flows

![River Flow](https://github.com/yourusername/ML_prediction_of_river_flows/blob/main/meteorologicalServiceGUI/Images/all_new.png)

## Overview

Southern Israel faces a critical challenge in water resource management due to the lack of historical hydraulic flow data. This repository presents a machine learning approach to predict historical river flows using high-resolution 10-minute meteorological data. The project includes data collection, feature engineering, model training, and a GUI application for further research.

### Abstract

Southern Israel lacks historical hydraulic flow data beyond the last 20 years, impacting water resource management. This study utilizes machine learning to predict river flows from meteorological data, resulting in 21 models for 21 links between meteorological and hydraulic stations. Our top-performing XGBoost model achieves a 98% precision and recall rate.

### Introduction

Water resource management in arid regions like Southern Israel is crucial. While meteorological data spans decades, historical hydraulic flow data is limited to the past two decades, hindering water resource understanding. This project bridges the gap by predicting river flows using high-resolution meteorological data.

### Method and Experimental Setup

#### Datasets

- **IMS Data**: Meteorological data obtained from the Israeli Meteorological Service (IMS).
- **Flows Data**: River flow data from the Water Authority in Israel for three periods.
- **Link Data**: Dataset for setting up time windows and links between meteorological and hydraulic stations.
- **Hydraulic Stations**: Hydraulic station data from the Water Authority.

#### Visualization

- Visualizations of flow patterns and attributes.
- Average flow strength and flow occurrences.
- IMS data analysis, including temperature, humidity, and rain patterns.
- Map of meteorological and hydraulic station locations.

#### Features Engineering

- Description of key features used in the dataset.
- Features like temperature, humidity, rainfall, and more.
- Target label: 1 for flow, 0 for no flow.

#### Preprocess and Dataframe Building

- Data cleaning and preprocessing steps.
- Generation of features based on the IMS dataset.
- Integration of datasets and temporal relationships.

## Repository Structure

- **data/**: Folder containing raw data files.
  - 10min_data.rar
  - flows_and_link_data.rar
  - stations_longitude_latitude.rar
- **meteorologicalServiceGUI/**: Folder containing the GUI application.
  - **Images/**: Images used in the GUI.
    - all.gif
    - all_new.png
  - **Models/**: Pre-trained machine learning models.
    - model1.pkl
    - model2.pkl
    - model3.pkl
    - ...
    - model4.pkl
  - runGui.py: GUI application code.
- Visualization.ipynb: Jupyter notebook for data visualization.
- get_data_from_api.py: Script for retrieving data from APIs.
- main_code.ipynb: Jupyter notebook for the main project code.
- README.md: This readme file.

## Getting Started

1. Clone the repository: `git clone https://github.com/yourusername/ML_prediction_of_river_flows.git`
2. Set up your Python environment with the required dependencies.
3. Explore the Jupyter notebooks and scripts for data analysis and model training.
4. Use the GUI application for predictions.

## How to Cite

If you use this work in your research or find it helpful, please cite our GitHub repository:

