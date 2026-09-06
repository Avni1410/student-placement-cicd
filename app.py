from flask import Flask, request, jsonify

from src.predict import predict_placement


app = Flask(__name__)


@app.route("/")
def home():
    return "Student Placement Prediction API"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    result = predict_placement(
        data["cgpa"],
        data["attendance"],
        data["coding_score"],
        data["projects"],
        data["internships"],
        data["communication_skills"]
    )

    return jsonify({
        "prediction": result
    })


if __name__ == "__main__":
    app.run()
