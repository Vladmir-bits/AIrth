from flask import Flask, jsonify, request
from data_preprocessor import preprocess_data
from energy_forecasting_model import EnergyForecastingModel

app = Flask(__name__)
model = EnergyForecastingModel()

@app.route('/predict', methods=['POST'])
def predict_energy_usage():
    data = request.json
    preprocessed_data = preprocess_data(data)
    prediction = model.predict(preprocessed_data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
