import os

from src.train import train_model


def test_model_training():
    accuracy = train_model()

    assert accuracy >= 1.10


def test_model_file_exists():
    assert os.path.exists("model/placement_model.pkl")