import pytest
import joblib
import pandas as pd
import numpy as np
import os


# ─────────────────────────────────────────
# Test 1 — Model file exists
# ─────────────────────────────────────────
def test_model_file_exists():
    assert os.path.exists('regressor.sav'), "Model file not found"


# ─────────────────────────────────────────
# Test 2 — Encoder file exists
# ─────────────────────────────────────────
def test_encoder_file_exists():
    assert os.path.exists('encoder.sav'), "Encoder file not found"


# ─────────────────────────────────────────
# Test 3 — Model loads without error
# ─────────────────────────────────────────
def test_model_loads():
    model = joblib.load(open('regressor.sav', 'rb'))
    assert model is not None


# ─────────────────────────────────────────
# Test 4 — Encoder loads without error
# ─────────────────────────────────────────
def test_encoder_loads():
    with open('encoder.sav', 'rb') as f:
        enc = joblib.load(f)
    assert enc is not None


# ─────────────────────────────────────────
# Test 5 — Prediction returns a number
# ─────────────────────────────────────────
def test_prediction_output():
    model = joblib.load(open('regressor.sav', 'rb'))
    with open('encoder.sav', 'rb') as f:
        enc = joblib.load(f)

    # Sample input matching your app's feature structure
    features = [[30000, 'Petrol', 'Individual', 'Manual', 1, 5]]
    df = pd.DataFrame(features, columns=[
        'Kms_Driven', 'Fuel_Type', 'Seller_Type',
        'Transmission', 'Past_Owners', 'Age'
    ])

    df_transformed = enc.transform(df)
    prediction = model.predict(df_transformed)

    assert prediction is not None
    assert len(prediction) == 1
    assert isinstance(prediction[0], (int, float, np.floating))


# ─────────────────────────────────────────
# Test 6 — Prediction is a positive number
# ─────────────────────────────────────────
def test_prediction_is_positive():
    model = joblib.load(open('regressor.sav', 'rb'))
    with open('encoder.sav', 'rb') as f:
        enc = joblib.load(f)

    features = [[15000, 'Diesel', 'Dealer', 'Automatic', 2, 3]]
    df = pd.DataFrame(features, columns=[
        'Kms_Driven', 'Fuel_Type', 'Seller_Type',
        'Transmission', 'Past_Owners', 'Age'
    ])

    df_transformed = enc.transform(df)
    prediction = model.predict(df_transformed)

    assert prediction[0] > 0, "Price prediction should be positive"