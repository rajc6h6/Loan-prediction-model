# 💼 Loan Approval Prediction – ML Model by Raj

This project predicts whether a person’s loan will be approved based on input features like income, credit history, employment status, etc. I built the model from scratch — cleaned the dataset, handled nulls, encoded features, built a complete pipeline, and deployed it as a Streamlit web app.

---

## 🔧 Tools & Libraries Used

- **Python**
- **Pandas**, **NumPy** – for data preprocessing
- **scikit-learn** – ML model, pipeline, hyperparameter tuning
- **Streamlit** – to create the interactive web app
- **Joblib** – for model saving/loading

---

## 🚀 What I Did

- Cleaned and explored the loan dataset
- Handled null values and encoded categorical variables
- Used `ColumnTransformer` and `Pipeline` for clean workflow
- Trained a **RandomForestClassifier**
- Tuned hyperparameters with **GridSearchCV**
- Built a user interface using **Streamlit**
- Made the model accessible via a simple web app

---

## 📊 Model Accuracy

- Final model accuracy on test set: **~78.9%**
- Model generalizes well — no overfitting

---

## 🧪 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/loan-prediction-model

# 2. Install requirements
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
