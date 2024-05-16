import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

# Load th trained K-means model
with open('model/Segmentation_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Customer Segmentation")

# Upload CSV file
upload_file = st.file_uploader("Upload your CSV file", type=["csv"])

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write("Data Preview:")
    st.write(df.head())

    # Map Columns to required features
    st.subheader("Map Columns to Features")
    col1, col2 = st.columns(2)

    with col1:
        income = st.selectbox("Select Annual Income Column", df.columns)

    with col2:
        spend_score = st.selectbox("Select Spending Score Column", df.columns)

    if st.button("Segment Customers"):
        df.rename(columns={income: 'Annual Income (k$)', spend_score: 'Spending Score (1-100)'})

        data = df[['Annual Income (k$)', 'Spending Score (1-100)']]

        df['Cluster'] = model.predict(data)

        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=df, palette='viridis')
        plt.title("Customer Segmentation")
        plt.xlabel("Annual Income (k$)")
        plt.ylabel("Spending Score (1-100)")

        plot_path = 'static/cluster_plot.png'
        if not os.path.exists('static'):
            os.makedirs('static')
        plt.savefig(plot_path)
        plt.close()

        st.subheader("Segmented Data with Cluster Information")
        st.write(df)

        st.subheader("Cluster Visualization")
        st.image(plot_path)
