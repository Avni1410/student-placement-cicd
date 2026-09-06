from app import app


def test_prediction_api():

    client = app.test_client()

    response = client.post(
        "/predict",
        json={
            "cgpa": 8.5,
            "attendance": 92,
            "coding_score": 85,
            "projects": 3,
            "internships": 2,
            "communication_skills": 9
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "prediction" in data
