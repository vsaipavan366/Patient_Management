from fastapi import FastAPI

app = FastAPI()

patients = [
    {"id": 1, "name": "Asha", "age": 35, "disease": "Fever"},
    {"id": 2, "name": "Rahul", "age": 42, "disease": "Cold"}
]


@app.get("/")
def home():
    return {"message": "Patient Management API"}


@app.get("/patients")
def get_patients():
    return patients


@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return {"message": "Patient not found"}


@app.post("/patients")
def add_patient(patient: dict):
    patients.append(patient)
    return {"message": "Patient added", "patient": patient}


@app.put("/patients/{patient_id}")
def update_patient(patient_id: int, updated_patient: dict):
    for index, patient in enumerate(patients):
        if patient["id"] == patient_id:
            patients[index] = updated_patient
            return {"message": "Patient updated", "patient": updated_patient}
    return {"message": "Patient not found"}


@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            patients.remove(patient)
            return {"message": "Patient deleted"}
    return {"message": "Patient not found"}