import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from src.preprocess import prepare_data


DATA_PATH = "data/students.csv"
MODEL_PATH = "model/placement_model.pkl"


def train_model():
    X, y = prepare_data(DATA_PATH)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"Model Accuracy: {accuracy:.2f}")

    # Quality gate
    if accuracy < 0.80:
        raise ValueError(
            f"Model accuracy {accuracy:.2f} is below required 0.80"
        )

    os.makedirs("model", exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to {MODEL_PATH}")

    return accuracy


if __name__ == "__main__":
    train_model()