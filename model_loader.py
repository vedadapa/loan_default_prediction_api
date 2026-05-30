
import joblib
import numpy as np
from pathlib import Path
model_path = Path("model/xgboost_model.joblib")

_model = None

def load():
    global _model
    if _model is None:
        _model = joblib.load(model_path)
        print(f'[model_loader] model loaded from: {model_path}')
    return _model

def predict_default_probability(features:dict) -> dict:

    model = load()
    # important featues the model uses
    feature_order = ["loan_amount", "term", "property_value", "income", "LTV"]

    X = np.array([[features[f] for f in feature_order]])
    prob = model.predict_proba(X)[0]
    defaulter_prob = float(prob[1])
    confidence = float(max(prob))

    # thresholds for preditions
    if defaulter_prob < 0.3:
        risk_label = 'low'
        approved = True
    elif defaulter_prob < 0.6:
        risk_label = "Medium"
        approved = False
    else:
        risk_label = "High"
        approved = False
    return {
        "default_probability":round(defaulter_prob,4),
        "risk_label": risk_label,
        "approved": approved,
        "confidence": confidence
    }