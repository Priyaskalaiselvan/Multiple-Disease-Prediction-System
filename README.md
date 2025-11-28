# Multiple-Disease-Prediction-System
This project predicts **Kidney Disease**, **Liver Disease**, and **Parkinson Disease** using   separate machine learning models, trained on 3 different medical datasets.
### Kidney | Liver | Parkinson  
Complete End-to-End Machine Learning + Streamlit Application

The project includes:
- Data cleaning & preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature Engineering  
- Handling Imbalance  
- Model Building & Hyperparameter Tuning  
- Model Evaluation  
- Model Saving (.pkl)  
- A unified **Streamlit web app** for all 3 disease predictions  


# 🚀 Features

### ✔ End-to-End ML Pipeline for 3 Diseases  
- **Kidney Disease Model**  
- **Liver Disease Model**  
- **Parkinson Disease Model**

### ✔ Advanced ML Techniques  
- Imbalanced dataset handling (SMOTE / Random Oversampling)  
- RobustScaler  normalization  
- Model pipelines  
- Threshold tuning (`predict_proba`)  

### ✔ Professional Streamlit UI  
- Sidebar navigation  
  - Box-style input layout
 
project/
│
├── data/
│ ├── kidney.csv
│ ├── liver.csv
│ └── parkinson.csv
│
├── notebooks/
│ ├── kidney_model.ipynb
│ ├── liver_model.ipynb
│ └── parkinson_model.ipynb
│
├── models/
│ ├── kidney_model.pkl
│ ├── liver_model.pkl
│ └── parkinson_model.pkl
│
├── disease_prediction.py # Streamlit app
├── requirements.txt
├── README.md

# 🔬 **1. Data Cleaning Workflow (ALL 3 DATASETS)**

### ✔ Handling missing values  
- Replaced `?`, blanks, NaN  
- Converted categorical values to binary/ordinal  
- Mapped target column (`status`, `classification`, etc.)

### ✔ Outlier removal  
- Boxplot inspection  
- IQR method  

### ✔ Feature scaling  
- Kidney  
- Liver → **RobustScaler**→  
- Parkinson → **RobustScaler**→  

### ✔ Categorical Encoding  
- Gender encoded (Male=1, Female=0)  

# 📊 **2. Exploratory Data Analysis (EDA)**

EDA performed using:
### Visualizations used:
- Heatmap (correlation)  
- Boxplots for outliers

# 🧠 **3. Model Building**

### Kidney Disease
Models tested:
- Logistic Regression  
- RandomForest  
- XGBoost  

Final model:
✔ **RandomForestClassifier**  

### Liver Disease
Models tested:
- Logistic Regression  
- Knn 
- XGBoost
- Randomforest 

Final model:
✔ **Logistic Regression**  
✔ Outlier removal improved accuracy  
✔ Hyperparameter tuning   
✔ Custom threshold tuning (0.51)  

### Parkinson Disease
Models tested:
- DecisionTree  
- Logistic Regression
- Knn
- XGBoost  

Final model:
✔ ** XGBClassifier**  
✔ MinMax scaling  
✔ Custom threshold tuning (0.51)  

Then loaded the model in Streamlit App

🛠️ Tech Stack
Python Pandas NumPy Scikit-learn Imbalanced-learn Streamlit Joblib

📌 Future Enhancements

Add SHAP explainability
Add result export as PDF
Deploy to Streamlit Cloud
Add login/authentication



 
- Probability-based prediction  
- DataFrame input conversion  
