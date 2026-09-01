from flask import Flask, render_template

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Dashboard page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Patients page
@app.route("/patients")
def patients():

    patient_data = [
        {
            "id": 1,
            "name": "Patient 1",
            "age": 35,
            "gender": "Male",
            "diagnosis": "Diabetes",
            "hospital": "City Hospital",
            "status": "Active"
        },
        {
            "id": 2,
            "name": "Patient 2",
            "age": 42,
            "gender": "Female",
            "diagnosis": "Hypertension",
            "hospital": "General Hospital",
            "status": "Active"
        },
        {
            "id": 3,
            "name": "Patient 3",
            "age": 58,
            "gender": "Male",
            "diagnosis": "Heart Disease",
            "hospital": "Central Hospital",
            "status": "Active"
        },
        {
            "id": 4,
            "name": "Patient 4",
            "age": 27,
            "gender": "Female",
            "diagnosis": "Respiratory Disease",
            "hospital": "City Hospital",
            "status": "Active"
        }
    ]

    return render_template(
        "patients.html",
        patients=patient_data
    )


# Hospitals page
@app.route("/hospitals")
def hospitals():

    hospital_data = [
        {
            "id": 1,
            "name": "City Hospital",
            "location": "Chennai",
            "beds": 500,
            "doctors": 80,
            "department": "General Medicine"
        },
        {
            "id": 2,
            "name": "General Hospital",
            "location": "Bangalore",
            "beds": 350,
            "doctors": 60,
            "department": "Cardiology"
        },
        {
            "id": 3,
            "name": "Central Hospital",
            "location": "Hyderabad",
            "beds": 450,
            "doctors": 70,
            "department": "Multi-Specialty"
        }
    ]

    return render_template(
        "hospitals.html",
        hospitals=hospital_data
    )


# Analysis page
@app.route("/analysis")
def analysis():

    return render_template(
        "analysis.html",

        total_patients=2450,
        hospital_visits=3820,
        active_cases=315,
        total_admissions=1200,

        general_hospitals=40,
        specialty_hospitals=25,
        emergency_hospitals=20,
        other_hospitals=15
    )


if __name__ == "__main__":
    app.run(debug=True)
