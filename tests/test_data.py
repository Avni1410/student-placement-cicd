from src.preprocess import load_and_validate_data


def test_dataset_is_valid():
    df = load_and_validate_data("data/students.csv")

    assert len(df) > 0
    assert "placed" in df.columns