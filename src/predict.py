import joblib


MODEL_PATH = "model/placement_model.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


def predict_placement(
    cgpa,
    attendance,
    coding_score,
    projects,
    internships,
    communication_skills
):
    model = load_model()

    data = [[
        cgpa,
        attendance,
        coding_score,
        projects,
        internships,
        communication_skills
    ]]

    prediction = model.predict(data)[0]

    return "Placed" if prediction == 1 else "Not Placed"
