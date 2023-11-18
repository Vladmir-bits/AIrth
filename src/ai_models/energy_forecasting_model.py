# Import necessary libraries
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

class EnergyForecastingModel:
    def __init__(self):
        self.model = RandomForestRegressor()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)

# Example usage
# model = EnergyForecastingModel()
# model.train(X_train, y_train)
# predictions = model.predict(X_test)
