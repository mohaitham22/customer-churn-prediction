# Customer Churn Prediction

A machine learning project that predicts whether a customer is likely to churn based on their profile using a trained classification model.

## Features

- **Churn Prediction Model**: Trained machine learning model using scikit-learn
- **Interactive UI**: Built with Streamlit for easy predictions
- **Data Analysis**: Jupyter notebook with exploratory data analysis and model training

## Project Structure

```
├── ui.py                    # Streamlit web app
├── project.ipynb           # Jupyter notebook with analysis
├── model.pkl               # Trained ML model
├── scaler.pkl              # Feature scaler
├── label_encoder.pkl       # Label encoder
├── Bank.csv                # Training data
└── requirements.txt        # Python dependencies
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the Web App

```bash
streamlit run ui.py
```

The app will open at `http://localhost:8501`

### Run the Jupyter Notebook

```bash
jupyter notebook project.ipynb
```

## Try the Live Demo

You can try the interactive web app online without installing anything:
[Live Demo on Streamlit Cloud](https://your-streamlit-cloud-url)

## How to Use the App

1. Fill in customer profile information:
   - Credit Score, Age, Tenure
   - Geography and Gender
   - Account Balance and Products
   - Credit Card and Member Status
   - Estimated Salary
   - Satisfaction Score and Card Type
   - Points Earned

2. Click "Predict Churn" button
3. View the prediction result and probability

## Model Details

- **Algorithm**: Classification model trained on customer banking data
- **Features**: 13 input features
- **Accuracy**: Model trained on Bank.csv dataset

## License

This project is open source and available for educational purposes.
