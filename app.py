import pickle
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

pipe = pickle.load(open('car_model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        d = request.json
        df = pd.DataFrame([{
            'name':       d['name'],
            'company':    d['company'],
            'year':       int(d['year']),
            'kms_driven': int(d['kms_driven']),
            'fuel_type':  d['fuel_type']
        }])
        price = int(pipe.predict(df)[0])
        return jsonify({'price': price})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/')
def index():
    return 'Car Price Predictor API running.'

if __name__ == '__main__':
    app.run(debug=True)
