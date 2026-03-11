# ❤️ Heart Disease Prediction API

A machine learning project that predicts the presence of heart disease using the UCI Heart Disease dataset. The model is deployed as a REST API using FastAPI, making it accessible for real-time predictions.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

## 📑 Table of Contents

- [Project Overview](#project-overview)
- [Dataset Information](#dataset-information)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Model Details](#model-details)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [API Deployment](#api-deployment)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Author](#author)

---

## 🎯 Project Overview

Heart disease is one of the leading causes of death worldwide. This project leverages machine learning to predict the presence of heart disease in patients based on various medical attributes. The trained model is deployed as a RESTful API using FastAPI, allowing healthcare professionals and applications to make real-time predictions.

**Key Objectives:**
- 🏥 Predict heart disease presence with high accuracy
- 🚀 Deploy ML model as production-ready API
- 📊 Provide insights through exploratory data analysis
- 🔬 Handle missing data and perform feature engineering
- 💻 Create easy-to-use prediction interface

---

## 📊 Dataset Information

### Source
**UCI Heart Disease Dataset** from Kaggle

### Dataset Statistics
- **Total Records**: 920 patients
- **Total Features**: 16 attributes
- **Target Variable**: `num` (presence of heart disease, 0-4 scale)

### Features Description

| Feature | Description | Type |
|---------|-------------|------|
| **id** | Patient ID | Integer |
| **age** | Age in years | Integer (28-77) |
| **sex** | Gender (Male/Female) | Categorical |
| **dataset** | Dataset origin (Cleveland, Hungary, etc.) | Categorical |
| **cp** | Chest pain type | Categorical |
| **trestbps** | Resting blood pressure (mm Hg) | Float |
| **chol** | Serum cholesterol (mg/dl) | Float |
| **fbs** | Fasting blood sugar > 120 mg/dl | Boolean |
| **restecg** | Resting electrocardiographic results | Categorical |
| **thalch** | Maximum heart rate achieved | Float |
| **exang** | Exercise induced angina | Boolean |
| **oldpeak** | ST depression induced by exercise | Float |
| **slope** | Slope of peak exercise ST segment | Categorical |
| **ca** | Number of major vessels (0-3) | Float |
| **thal** | Thalassemia type | Categorical |
| **num** | Diagnosis (0 = no disease, 1-4 = disease) | Integer |

### Chest Pain Types (cp)
- **Typical Angina**: Chest pain related to decreased blood supply to heart
- **Atypical Angina**: Chest pain not related to heart
- **Non-anginal Pain**: Typically esophageal spasms
- **Asymptomatic**: No chest pain

### Missing Values
- **slope**: 309 missing (33.6%)
- **ca**: 611 missing (66.4%)
- **thal**: 486 missing (52.8%)
- **fbs**: 90 missing (9.8%)
- **oldpeak**: 62 missing (6.7%)
- **trestbps**: 59 missing (6.4%)
- **exang**: 55 missing (6.0%)
- **thalch**: 55 missing (6.0%)
- **chol**: 30 missing (3.3%)

---

## ✨ Features

### Machine Learning
- ✅ **Data Preprocessing**: Handling missing values, outliers, and data types
- ✅ **Feature Engineering**: Creating meaningful features from raw data
- ✅ **Model Training**: Classification model for heart disease prediction
- ✅ **Model Evaluation**: Accuracy, precision, recall, F1-score metrics
- ✅ **Model Persistence**: Saved as `heart_model.pkl` for deployment

### API Features
- ✅ **FastAPI Framework**: High-performance, modern Python web framework
- ✅ **RESTful Endpoints**: Clean API design
- ✅ **Real-time Predictions**: Instant disease prediction
- ✅ **JSON Response Format**: Easy integration with frontend
- ✅ **Auto-generated Documentation**: Swagger UI and ReDoc

### Analysis Features
- ✅ **Exploratory Data Analysis**: Comprehensive data insights
- ✅ **Data Visualization**: Charts and graphs for better understanding
- ✅ **Statistical Analysis**: Distribution analysis and correlations
- ✅ **Jupyter Notebook**: Interactive analysis environment

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (optional)

### Step 1: Clone the Repository

```bash
git clone https://github.com/CODERGURU26/Heart-Disease-Prediction-API.git
cd Heart-Disease-Prediction-API
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Install required packages
pip install fastapi
pip install uvicorn
pip install scikit-learn
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install jupyter

# Or install all at once
pip install fastapi uvicorn scikit-learn pandas numpy matplotlib seaborn jupyter
```

### Step 4: Verify Installation

```bash
python --version
pip list
```

---

## 💻 Usage

### Running the Jupyter Notebook

1. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Open the Analysis Notebook**
   - Navigate to `UCI_Heart_Disease_-_Kaggle_Data.ipynb`
   - Run all cells to see the complete analysis

3. **Explore the Analysis**
   - Data loading and cleaning
   - Exploratory data analysis
   - Feature engineering
   - Model training and evaluation

### Running the FastAPI Server

1. **Start the API Server**
   ```bash
   uvicorn main:app --reload
   ```

2. **Server will start on:**
   ```
   http://127.0.0.1:8000
   ```

3. **Access Interactive Documentation**
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

---

## 📡 API Documentation

### Base URL
```
http://127.0.0.1:8000
```

### Endpoints

#### 1. Home Endpoint
**GET** `/`

**Description**: Welcome message and API info

**Response:**
```json
{
  "message": "Heart Disease Prediction API"
}
```

**Example:**
```bash
curl http://127.0.0.1:8000/
```

---

#### 2. Prediction Endpoint
**POST** `/predict`

**Description**: Predict heart disease based on patient features

**Request Body:**
```json
{
  "features": [63, 1, 1, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]
}
```

**Feature Order:**
1. Age (years)
2. Sex (0 = Female, 1 = Male)
3. Chest pain type (0-3)
4. Resting blood pressure (mm Hg)
5. Serum cholesterol (mg/dl)
6. Fasting blood sugar > 120 mg/dl (0 = No, 1 = Yes)
7. Resting ECG results (0-2)
8. Maximum heart rate achieved
9. Exercise induced angina (0 = No, 1 = Yes)
10. ST depression induced by exercise
11. Slope of peak exercise ST segment (0-2)
12. Number of major vessels (0-3)
13. Thalassemia (0-3)

**Response:**
```json
{
  "prediction": 1
}
```

**Prediction Values:**
- **0**: No heart disease
- **1-4**: Heart disease present (severity levels)

**Example using cURL:**
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"features": [63, 1, 1, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]}'
```

**Example using Python:**
```python
import requests

url = "http://127.0.0.1:8000/predict"
features = [63, 1, 1, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]

response = requests.post(url, json={"features": features})
print(response.json())
# Output: {"prediction": 1}
```

**Example using JavaScript:**
```javascript
const url = "http://127.0.0.1:8000/predict";
const features = [63, 1, 1, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1];

fetch(url, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ features: features })
})
.then(response => response.json())
.then(data => console.log(data));
// Output: {"prediction": 1}
```

---

## 🤖 Model Details

### Algorithm
- **Type**: Classification Model (specific algorithm determined during training)
- **Framework**: Scikit-learn
- **Model File**: `heart_model.pkl`

### Training Process
1. **Data Loading**: Import UCI Heart Disease dataset
2. **Data Cleaning**: Handle missing values and outliers
3. **Feature Engineering**: Transform categorical variables
4. **Train-Test Split**: Divide data into training and testing sets
5. **Model Training**: Fit the model on training data
6. **Model Evaluation**: Assess performance on test data
7. **Model Serialization**: Save trained model using pickle

### Performance Metrics
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score

*Note: Specific metrics available in the Jupyter Notebook*

---

## 📂 Project Structure

```
Heart-Disease-Prediction-API/
│
├── main.py
│   └── FastAPI application with prediction endpoint
│
├── heart_model.pkl
│   └── Trained machine learning model (serialized)
│
├── heart_disease_uci.csv
│   └── UCI Heart Disease dataset (920 records)
│
├── UCI_Heart_Disease_-_Kaggle_Data.ipynb
│   └── Jupyter Notebook with EDA and model training
│
├── requirements.txt
│   └── Python package dependencies
│
└── README.md
    └── Project documentation (this file)
```

---

## 🛠️ Technologies Used

### Core Technologies
| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Programming language | 3.8+ |
| **FastAPI** | Web framework for API | Latest |
| **Uvicorn** | ASGI server | Latest |
| **Scikit-learn** | Machine learning | Latest |
| **Pandas** | Data manipulation | Latest |
| **NumPy** | Numerical computing | Latest |

### Data Analysis & Visualization
- **Matplotlib**: Static plotting
- **Seaborn**: Statistical visualization
- **Jupyter Notebook**: Interactive analysis

### Model Deployment
- **Pickle**: Model serialization
- **FastAPI**: API framework
- **Pydantic**: Data validation (FastAPI default)

---

## 🧹 Data Preprocessing

### Steps Performed

1. **Loading Data**
   ```python
   df = pd.read_csv('heart_disease_uci.csv')
   ```

2. **Handling Missing Values**
   - Imputation for numerical features
   - Mode/frequency for categorical features
   - Feature-specific strategies

3. **Data Type Conversion**
   - Convert categorical strings to numerical
   - Encode binary variables
   - Normalize numerical features

4. **Outlier Detection**
   - Identify outliers using IQR method
   - Handle or remove extreme values

5. **Feature Selection**
   - Remove irrelevant features (id, dataset)
   - Select most predictive features

6. **Data Splitting**
   ```python
   from sklearn.model_selection import train_test_split
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
   ```

---

## 📈 Model Training

### Training Workflow

```python
# 1. Import libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  # Example
import pickle

# 2. Prepare features and target
X = df.drop(['num', 'id', 'dataset'], axis=1)
y = df['num']

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 5. Evaluate
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy}")

# 6. Save model
pickle.dump(model, open('heart_model.pkl', 'wb'))
```

### Model Evaluation

```python
from sklearn.metrics import classification_report, confusion_matrix

# Predictions
y_pred = model.predict(X_test)

# Metrics
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
```

---

## 🚀 API Deployment

### Local Deployment

```bash
# Start the server
uvicorn main:app --reload

# Server runs on http://127.0.0.1:8000
```

### Production Deployment Options

#### 1. **Heroku**
```bash
# Install Heroku CLI
# Create Procfile
echo "web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}" > Procfile

# Deploy
heroku create heart-disease-api
git push heroku main
```

#### 2. **AWS EC2**
```bash
# Install dependencies on EC2
pip install -r requirements.txt

# Run with nohup
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
```

#### 3. **Docker**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### 4. **Google Cloud Run**
```bash
gcloud run deploy heart-disease-api \
  --source . \
  --platform managed \
  --region us-central1
```

---

## 🔮 Future Enhancements

### Model Improvements
- [ ] Implement ensemble methods (XGBoost, LightGBM)
- [ ] Perform hyperparameter tuning
- [ ] Add cross-validation
- [ ] Implement SHAP for model explainability
- [ ] Add confidence scores to predictions

### API Enhancements
- [ ] Add authentication (JWT tokens)
- [ ] Implement rate limiting
- [ ] Add batch prediction endpoint
- [ ] Create model versioning system
- [ ] Add prediction probability scores
- [ ] Implement caching for common requests

### Frontend Development
- [ ] Create web interface for predictions
- [ ] Build mobile application
- [ ] Add data visualization dashboard
- [ ] Implement user authentication
- [ ] Create patient history tracking

### Data & Analytics
- [ ] Real-time model retraining
- [ ] A/B testing for model versions
- [ ] Add logging and monitoring
- [ ] Implement feedback loop
- [ ] Create analytics dashboard

### Documentation
- [ ] Add API usage examples
- [ ] Create video tutorials
- [ ] Write deployment guides
- [ ] Add contribution guidelines
- [ ] Create troubleshooting guide

---

## 🐛 Troubleshooting

### Common Issues

#### Issue 1: Model File Not Found
**Error:** `FileNotFoundError: heart_model.pkl`

**Solution:**
```bash
# Ensure model file is in the same directory as main.py
# Or update the path in main.py:
model = pickle.load(open("path/to/heart_model.pkl", "rb"))
```

#### Issue 2: Port Already in Use
**Error:** `ERROR: [Errno 48] Address already in use`

**Solution:**
```bash
# Use a different port
uvicorn main:app --port 8001

# Or kill the process using the port
lsof -ti:8000 | xargs kill -9  # macOS/Linux
```

#### Issue 3: Import Errors
**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

#### Issue 4: Prediction Format Error
**Error:** Shape mismatch or invalid input

**Solution:**
```python
# Ensure features list has exactly 13 values
# Ensure all values are numeric
features = [63, 1, 1, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]
```

---

## 📊 Sample Predictions

### Example 1: Low Risk Patient
```python
# Features: 45-year-old female, normal vitals
features = [45, 0, 0, 120, 200, 0, 0, 150, 0, 0.5, 1, 0, 2]
# Prediction: 0 (No heart disease)
```

### Example 2: High Risk Patient
```python
# Features: 63-year-old male, elevated readings
features = [63, 1, 3, 145, 233, 1, 2, 150, 1, 2.3, 2, 2, 2]
# Prediction: 1-4 (Heart disease present)
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Make your changes**
   - Add new features
   - Fix bugs
   - Improve documentation
4. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
6. **Open a Pull Request**

### Contribution Ideas
- Improve model accuracy
- Add new ML algorithms
- Create frontend interface
- Add unit tests
- Improve documentation
- Add data visualization features

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

**Dataset License**: UCI Heart Disease dataset is available for research and educational purposes.

---

## 📧 Contact & Connect

### Author

**Gururaj Krishna Sharma**

- 📧 Email: [guruuu2468@gmail.com](mailto:guruuu2468@gmail.com)
- 💼 LinkedIn: [Gururaj Krishna Sharma](https://www.linkedin.com/in/gururaj-krishna-sharma)
- 💻 GitHub: [@CODERGURU26](https://github.com/CODERGURU26)

---

## 🌟 Acknowledgments

- **UCI Machine Learning Repository** for the heart disease dataset
- **Kaggle** for hosting the dataset
- **FastAPI Team** for the excellent web framework
- **Scikit-learn Developers** for machine learning tools
- **Medical professionals** who contributed to the dataset collection

---

## 📚 Additional Resources

### Learn More
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+disease)
- [Heart Disease Information - WHO](https://www.who.int/health-topics/cardiovascular-diseases)

### Related Projects
- Disease prediction models
- Medical diagnosis systems
- Healthcare analytics dashboards
- Clinical decision support systems

---

## ⚕️ Medical Disclaimer

**IMPORTANT**: This project is for educational and research purposes only. The predictions made by this model should NOT be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with any questions regarding a medical condition.

---

## 🎯 Key Takeaways

- ✅ Built end-to-end ML pipeline for heart disease prediction
- ✅ Deployed model as production-ready REST API
- ✅ Handled real-world messy data with missing values
- ✅ Created comprehensive documentation
- ✅ Implemented best practices for ML deployment

---

**⭐ If you find this project helpful, please give it a star!**

**🔔 Watch this repository for updates and improvements!**

---

*Last Updated: February 2026*

**Stay Healthy! ❤️**
