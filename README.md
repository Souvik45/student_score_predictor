<h1 align="center">🎓 Student Score Predictor</h1>

<p align="center">
  I created this linear regression project where I explored the relationship between study hours and student scores and deployed the model using Streamlit.
</p>

---

## 🚀 Demo

🔗 *Live App*: Coming Soon  
📌 Run it locally using Streamlit

---

## 📸 Preview

<img src="https://via.placeholder.com/800x400.png?text=Student+Score+Predictor+App+Screenshot" alt="App Screenshot" width="80%" />

---

## ✅ Features

- 📥 Takes user input for study hours
- 🔮 Predicts score using a trained ML model
- 📊 Displays a regression line plot
- 📈 Shows model accuracy (R² score)
- 🧑‍💻 Clean and interactive Streamlit UI

---

## 📁 Project Structure


student-score-predictor/
├── app.py                              # Main Streamlit app
├── student_scores.csv                  # Dataset
├── Student_Score_Predictor_Souvik.pkl  # Trained ML model
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation

---

## 🧠 Dataset

The dataset contains two columns:

| Hours | Scores |
|-------|--------|
| 2.5   | 21     |
| 5.1   | 47     |
| ...   | ...    |

Used to train a linear regression model to predict scores based on study hours.

---

## 📈 Model Performance

- 🔹 R² Score: *96.78%*
- 🔹 RMSE: *4.35*
- 🔹 Slope: *9.68*
- 🔹 Intercept: *2.83*

---

## 🔧 Tech Stack

- Python
- Streamlit
- scikit-learn
- Pandas
- Matplotlib
- Joblib

---

## ⚙️ How to Run Locally

'''bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/student-score-predictor.git
cd student-score-predictor

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py 

---

## 🙌 Personal Note

This project helped me understand not just how linear regression works,but also how to bring it to life with a user interface.It was fun!

---
## 👨‍💻 Author
