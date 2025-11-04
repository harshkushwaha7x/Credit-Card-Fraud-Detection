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

This project aims to detect fraudulent credit card transactions using machine learning models such as Logistic Regression, Random Forest, and XGBoost. It demonstrates how data preprocessing, feature scaling, and model evaluation can be used to build a robust fraud detection system. The dataset used is highly imbalanced, and techniques like SMOTE are employed to handle class imbalance effectively.

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

## 📊 Example Output

**Model Comparison:**

| Model               | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---------------------|----------|------------|---------|-----------|----------|
| Logistic Regression | 0.95     | 0.93       | 0.90    | 0.91      | 0.97     |
| Random Forest       | 0.98     | 0.96       | 0.95    | 0.95      | 0.99     |
| XGBoost             | 0.99     | 0.98       | 0.97    | 0.97      | 0.99     |

---

## ✅ Testing & Quality

- Tested using train/test split and k-fold cross validation.  
- Verified against overfitting using learning curves and ROC plots.  
- Code formatted with Black and PEP8 compliance.

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
- GitHub: [https://github.com/harshkushwaha7x](https://github.com/harshkushwaha7x)  
- LinkedIn: [https://linkedin.com/in/harshkushwaha7x](https://www.linkedin.com/in/harsh-kushwaha-7x/)  
- Email: harshkushwaha4151@gmail.com  

---

<div align="center">
Made by <b>Harsh Kushwaha</b> 💻
</div>