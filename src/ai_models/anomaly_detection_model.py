from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetectionModel:
    def __init__(self):
        self.model = IsolationForest()

    def fit(self, X):
        self.model.fit(X)

    def detect(self, X):
        return self.model.predict(X)

# Example usage
# anomaly_detector = AnomalyDetectionModel()
# anomaly_detector.fit(X_train)
# anomalies = anomaly_detector.detect(X_test)
