<div align="center">

# 💳 Credit Card Fraud Detection 🕵️‍♀️

**Credit Card Fraud Detection** is a machine learning project built to identify fraudulent transactions using predictive analytics. It uses multiple ML models, feature engineering, and performance evaluation techniques to ensure reliable fraud prediction. The project is containerized with Docker and ready for cloud deployment via Azure Container Registry.

• [Live Demo](https://creditcard-h3e5aaaffcajawc8.centralindia-01.azurewebsites.net/) • [Portfolio](https://portflio-3.vercel.app/) • [GitHub](https://github.com/harshkushwaha7x)

</div>

---

<p align="center">
  <a href="https://github.com/harshkushwaha7x/Credit-Card-Fraud-Detection"><img src="https://img.shields.io/github/last-commit/harshkushwaha7x/Credit-Card-Fraud-Detection?style=flat-square" alt="last commit"></a>
  <a href="https://github.com/harshkushwaha7x/Credit-Card-Fraud-Detection"><img src="https://img.shields.io/github/languages/top/harshkushwaha7x/Credit-Card-Fraud-Detection?style=flat-square" alt="languages"></a>
  <a href="https://github.com/harshkushwaha7x/Credit-Card-Fraud-Detection/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="license" /></a>
  <img src="https://img.shields.io/badge/version-1.0.0-success?style=flat-square" alt="version" />
</p>

---

## ✨ Summary

This project aims to detect fraudulent credit card transactions using machine learning models. After comparing 27+ models using LazyPredict (including Logistic Regression, Random Forest, XGBoost, SVC, and more), Logistic Regression was selected as the final deployed model. The dataset used is highly imbalanced (0.172% fraud rate), and RandomUnderSampler was employed to handle class imbalance in the training data while maintaining the original distribution in the test set for realistic evaluation.

---

## 📦 Highlights & Use Cases

- Real-world application of machine learning in finance and cybersecurity.  
- Demonstrates data preprocessing, EDA, and model optimization.  
- Suitable for deployment on cloud (Azure, AWS, GCP) using Docker containers.  
- Perfect for portfolios or research demonstrating applied ML workflows.

---

## 🚀 Features

- 📊 Exploratory Data Analysis (EDA) & visualization of transaction patterns  
- ⚙️ Feature engineering & data balancing with RandomUnderSampler  
- 🤖 Logistic Regression classifier  
- 📈 Model evaluation: accuracy, precision, recall, F1-score, ROC-AUC  
- 🧠 Fraud probability prediction for new transactions  
- 🐳 Containerized deployment with Docker  
- ☁️ Azure Container Registry integration for scalable cloud hosting

---

## 🧩 Tech Stack

**Language:** Python  
**Libraries:** NumPy, Pandas, Scikit-Learn, Matplotlib, Seaborn, XGBoost  
**Environment:** Streamlit / Jupyter Notebook  
**Containerization:** Docker  
**Deployment:** Azure Container Registry  
**Version Control:** Git & GitHub

---

## 📁 Project Structure

```
/CreditCard-Fraud-Detection
│
├── data/                      # Dataset files (CSV)
├── notebooks/                 # EDA and training notebooks
├── src/                       # Source code (preprocessing, model, utils)
├── models/                    # Saved trained models (.pkl)
├── Dockerfile                 # Docker configuration
├── requirements.txt           # Python dependencies
├── app.py                     # Streamlit inference app
├── README.md                  # Project documentation
└── LICENSE                    # License file
```

---

## 🛠️ Quick Start (Local)

1. **Clone the repository**
```bash
git clone https://github.com/harshkushwaha7x/Credit-Card-Fraud-Detection
cd Credit-Card-Fraud-Detection
```

2. **Create a virtual environment & install dependencies**
```bash
python -m venv venv
source venv/bin/activate  # for macOS/Linux
venv\Scripts\activate     # for Windows
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Access locally**
```
http://localhost:8501
```

---

## 🧭 Using the App

- Provide the 9 inputs (Amount, Transaction Time, Location Score, Merchant Type, Card Usage, Risk Factor, Account Age, Spending Pattern, Alert Count).
- The app auto-fills the remaining features with default values to match the model’s expected 15-feature vector, preventing shape errors.

---

## 🧪 Model Workflow

1. **Data Preprocessing**  
   - Handle missing values and scaling.  
   - Address class imbalance using RandomUnderSampler.  

2. **Model Training**  
   - Train a Logistic Regression classifier.  

3. **Evaluation Metrics**  
   - Accuracy, Precision, Recall, F1-Score, ROC-AUC.  

4. **Prediction & Deployment**  
   - Export trained model to `models/logistic_regression_model.pkl`.  
   - Deploy an interactive Streamlit UI app.  

---

## 🐳 Docker Deployment

### Build & Push Docker Image
```bash
docker build -t creditcard.azurecr.io/cc:latest .
docker login creditcard.azurecr.io
docker push creditcard.azurecr.io/cc:latest
```

### Run Locally
```bash
docker run -e PORT=8501 -p 8501:8501 creditcard.azurecr.io/cc:latest
```

---

## 📊 Dataset Information

**Source:** Kaggle's Credit Card Fraud Detection Dataset  
**Origin:** Transactions by European cardholders (September 2013)  
**Total Transactions:** 284,807  
**Fraudulent Transactions:** 492 (0.172%)  
**Duration:** 2 days  
**Features:** 28 PCA-transformed features (V1-V28) + Time + Amount

---

## 📈 Model Performance

### **LazyPredict Comparison (Top 10 Models)**

| Model                      | Accuracy | Balanced Accuracy | ROC-AUC | F1-Score |
|----------------------------|----------|-------------------|---------|----------|
| SVC                        | 1.00     | 0.97              | 0.97    | 1.00     |
| Logistic Regression        | 0.99     | 0.97              | 0.97    | 0.99     |
| CalibratedClassifierCV     | 0.99     | 0.97              | 0.97    | 0.99     |
| Perceptron                 | 0.98     | 0.97              | 0.97    | 0.99     |
| ExtraTreesClassifier       | 0.98     | 0.97              | 0.97    | 0.99     |
| RandomForestClassifier     | 0.98     | 0.97              | 0.97    | 0.99     |
| KNeighborsClassifier       | 0.98     | 0.97              | 0.97    | 0.99     |
| LGBMClassifier             | 0.98     | 0.97              | 0.97    | 0.99     |
| AdaBoostClassifier         | 0.98     | 0.97              | 0.97    | 0.99     |
| XGBClassifier              | 0.97     | 0.96              | 0.96    | 0.98     |

### **Final Deployed Model: Logistic Regression**

**Test Set Performance (Imbalanced - 56,962 samples):**

| Class          | Precision | Recall | F1-Score | Support |
|----------------|-----------|--------|----------|----------|
| Non-Fraud (0)  | 1.00      | 0.96   | 0.98     | 56,864   |
| Fraud (1)      | 0.04      | 0.93   | 0.08     | 98       |
| **Accuracy**   |           |        | **0.96** | 56,962   |
| **Macro Avg**  | 0.52      | 0.95   | 0.53     | 56,962   |
| **Weighted Avg** | 1.00    | 0.96   | 0.98     | 56,962   |

**Key Insights:**
- **High Recall (93%)**: Successfully detects 93% of fraudulent transactions
- **Low Precision (4%)**: High false positive rate due to extreme class imbalance (0.172% fraud)
- **Overall Accuracy (96%)**: Reflects the imbalanced nature of real-world fraud detection
- **Trade-off**: Model prioritizes catching fraud (high recall) over minimizing false alarms

---

## ✅ Testing & Quality

- **Train/Test Split**: 80/20 stratified split (227,845 train / 56,962 test)
- **Data Balancing**: RandomUnderSampler applied only to training data (166 samples per class)
- **Test Set**: Maintained original imbalanced distribution for realistic evaluation
- **Validation**: Confusion matrix analysis and classification reports
- **Model Comparison**: 27+ models tested using LazyPredict
- **Deployment**: Live on Azure Web App with Docker containerization

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create your branch: `git checkout -b feature/new-feature`  
3. Commit changes: `git commit -m "Added new feature"`  
4. Push and open a Pull Request  

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE).

---

## 📬 Contact

**Harsh Kushwaha** — Developer & Maintainer 
- Portfolio: [https://portflio-3.vercel.app/](https://portflio-3.vercel.app/) 
- GitHub: [https://github.com/harshkushwaha7x](https://github.com/harshkushwaha7x)  
- LinkedIn: [https://linkedin.com/in/harshkushwaha7x](https://www.linkedin.com/in/harsh-kushwaha-7x/)  
- Email: harshkushwaha4151@gmail.com  

---

<div align="center">
Made by <b>Harsh Kushwaha</b> 💻
</div>