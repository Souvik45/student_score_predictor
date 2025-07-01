import streamlit as st
import joblib
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("/home/sayan/Downloads/student_scores.csv")
# Load the trained model
model = joblib.load('Student_Score_Predictor_Souvik.pkl')

# Title and Description
st.title("🎓 Student Score Predictor")
st.markdown("Model Accuracy(R2 score):96.78%")
st.markdown("Enter the number of hours studied to predict the expected exam score.")

# Input from user
hours = st.number_input("🕒 Enter study hours:", min_value=0.0, step=0.5)

# Predict button
if st.button("Predict Score"):
    prediction = model.predict([[hours]])[0]
    st.success(f"🧠 Predicted Score: {prediction:.2f} marks")

st.markdown("### 📊 Regression Line")

# Create the plot
fig, ax = plt.subplots()
ax.scatter(data['Hours'], data['Scores'], color='blue', label='Actual Scores')
ax.plot(data['Hours'], model.predict(data[['Hours']]), color='red', label='Regression Line')
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Scores")
ax.legend()

# Show it in Streamlit
st.pyplot(fig)


st.markdown("---")  # Horizontal line
st.markdown("✅ Developed by *Souvik Samanta*")
st.markdown("[🔗 View Project on GitHub](https://github.com/yourusername/student-score-app)")
