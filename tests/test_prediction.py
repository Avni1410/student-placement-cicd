from src.predict import predict_placement


def test_prediction():
    result = predict_placement(
        8.5,
        92,
        85,
        3,
        2,
        9
    )

    assert result in ["Placed", "Not Placed"]