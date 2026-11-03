import joblib
import pandas as pd

model = joblib.load("model.pkl")

sample = pd.DataFrame([{
    "latency": 150,
    "packet_loss": 18,
    "jitter": 35,
    "bandwidth": 95,
    "cpu": 65,
    "memory": 55,
    "error_rate": 7
}])

prediction = model.predict(sample)[0]

probabilities = model.predict_proba(sample)[0]
confidence = max(probabilities) * 100

print("Predicted Fault:", prediction)
print("Confidence:", round(confidence, 2), "%")