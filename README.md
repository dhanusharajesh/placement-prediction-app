# 🎓 Student Placement Prediction App

A machine learning-based web application that predicts whether a student is likely to be placed based on academic performance, skills, and experience. Built using **Streamlit** for an interactive user interface.
📌 Features

- Predict student placement outcomes using a trained ML model
- Interactive web interface with real-time input handling
- Supports multiple input factors:
  - CGPA
  - Internships
  - Projects
  - Workshops / Certifications
  - Aptitude Score
  - Soft Skills Rating
  - Academic Scores (SSC, HSC)
- Instant prediction results

🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: Scikit-learn (Pickle Model)
- **Libraries**: NumPy, Pickle

📂 Project Structure
placement-prediction-app/
│
├── app.py # Main Streamlit application
├── placement_model.pkl # Trained ML model
├── placementdata.csv # Dataset used for training
├── placement-prediction-eda.ipynb # Exploratory Data Analysis

▶️ How to Run Locally

1. Clone the repository
git clone https://github.com/your-username/placement-prediction-app.git
cd placement-prediction-app

2. Install dependencies
pip install streamlit numpy

3. Run the application
streamlit run app.py

🧠 Machine Learning Model
Model trained on student academic and skill-based features
Uses classification to predict placement outcome
Saved using Pickle (.pkl) for deployment

👩‍💻 Author
Dhanusha
GitHub: https://github.com/dhanusharajesh
