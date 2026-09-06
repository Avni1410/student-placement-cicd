import pandas as pd


REQUIRED_COLUMNS = [
    "cgpa",
    "attendance",
    "coding_score",
    "projects",
    "internships",
    "communication_skills",
    "placed"
]


def load_and_validate_data(path):
    df = pd.read_csv(path)

    # Check required columns
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    # Check missing values
    if df.isnull().sum().sum() > 0:
        raise ValueError("Dataset contains missing values")

    # Check valid target values
    if not set(df["placed"].unique()).issubset({0, 1}):
        raise ValueError("Invalid values in placed column")

    # Check numeric columns
    for column in REQUIRED_COLUMNS:
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise ValueError(
                f"Column {column} must be numeric"
            )

    return df


def prepare_data(path):
    df = load_and_validate_data(path)

    X = df.drop("placed", axis=1)
    y = df["placed"]

    return X, y
