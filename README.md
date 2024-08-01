# Customer Segmentation using K-Means Clustering

## Overview

This project demonstrates customer segmentation using the K-Means clustering algorithm. The objective is to identify distinct customer groups from a dataset, enabling businesses to tailor marketing strategies and improve customer engagement. The project includes a user-friendly interface developed with the Streamlit library for easy interaction and visualization.

## Features

- **Data Upload:** Users can upload a dataset in CSV format for analysis.
- **Automated Clustering:** Utilizes the K-Means algorithm to automatically classify customers into segments.
- **Visualization:** Displays segmentation results and clusters graphically for easy interpretation.
- **User Interface:** Built with Streamlit for a smooth and interactive user experience.

## Installation

Follow these steps to set up and run the project locally:

### Prerequisites

- Python 3.7 or higher
- Git

### Clone the Repository

```bash
git clone https://github.com/shadowgod2810/CustomerSegmentation.git
cd CustomerSegmentation
```
## Install Dependencies
It is recommended to use a virtual environment to manage dependencies. You can set up a virtual environment using venv or conda.

### Using venv
```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
### Using conda
```bash
conda create --name segmentation_env python=3.7
conda activate segmentation_env
```
Once the virtual environment is activated, install the required packages:

```bash
pip install -r requirements.txt
```
## Run the Application
To start the Streamlit application, use the following command:

```bash
streamlit run app.py
```
The application should now be accessible at http://localhost:8501 in your web browser.

## Usage
Upload Dataset: Use the provided interface to upload a CSV file containing customer data.
Set Parameters: Configure clustering parameters such as the number of clusters if required.
Run Segmentation: Click on the "Run Segmentation" button to perform the clustering.
View Results: The segmented data will be displayed along with visualizations of the clusters.
##Dataset
The sample dataset should include features relevant for segmentation, such as customer demographics, purchase history, etc. Ensure the dataset is cleaned and preprocessed before uploading.

## Contributing
Feel free to fork this repository and submit pull requests for any enhancements or bug fixes. Contributions are always welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
