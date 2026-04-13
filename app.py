import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("placement_model.pkl", "rb"))

st.title("Student Placement Prediction App")
st.write("Predict whether a student will get placed based on their academic and skill scores.")


StudentID = st.number_input("Enter Student ID", min_value=1, step=1)
CGPA = st.number_input("Enter CGPA (0–10)", min_value=0.0, max_value=10.0, step=0.1)
Internships = st.number_input("Enter Number of Internships", min_value=0, step=1)
Projects = st.number_input("Enter Number of Projects", min_value=0, step=1)
Workshops = st.number_input("Enter Number of Workshops/Certifications", min_value=0, step=1)
AptitudeTestScore = st.number_input("Enter Aptitude Test Score", min_value=0, max_value=100, step=1)
SoftSkillsRating = st.number_input("Enter Soft Skills Rating (1–10)", min_value=0, max_value=10, step=1)
ExtracurricularActivities = st.selectbox("Participated in Extracurricular Activities?", [0, 1])
PlacementTraining = st.selectbox("Completed Placement Training?", [0, 1])
SSC_Marks = st.number_input("Enter SSC Marks (out of 100)", min_value=0, max_value=100, step=1)
HSC_Marks = st.number_input("Enter HSC Marks (out of 100)", min_value=0, max_value=100, step=1)


if st.button("Predict Placement"):
    input_data = np.array([[StudentID, CGPA, Internships, Projects, Workshops,
                            AptitudeTestScore, SoftSkillsRating,
                            ExtracurricularActivities, PlacementTraining,
                            SSC_Marks, HSC_Marks]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("The student is likely to be PLACED.")
    else:
        st.error("The student is UNLIKELY to be placed.")
