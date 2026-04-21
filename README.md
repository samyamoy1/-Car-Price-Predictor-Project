# Car Price Predictor

A machine learning web application that predicts the resale price of used cars in the Indian market. Built using a Linear Regression model trained on the Quikr used cars dataset.

**Live Demo:** https://samyamoy1.github.io/-Car-Price-Predictor-Project

---

## Overview

This project takes five inputs from the user — car name, company, year of purchase, kilometres driven, and fuel type — and returns an estimated resale price in Indian Rupees. The prediction is served through a REST API backed by a trained scikit-learn pipeline.

The frontend is a plain HTML page hosted on GitHub Pages. The backend is a Flask application deployed on Render.

---

## Model Details

| Property | Value |
|---|---|
| Algorithm | Linear Regression |
| Encoding | OneHotEncoder (name, company, fuel_type) |
| Dataset | Quikr Used Cars |
| Records after cleaning | 815 |
| Train/Test split | 90/10 |
| Best random_state | 302 |
| R² Score | 0.899 |

**Features used:** `name`, `company`, `year`, `kms_driven`, `fuel_type`

**Target:** `Price` (INR)

---

## Project Structure

```
app.py               Flask API
car_model.pkl        Trained scikit-learn pipeline
index.html           Frontend (GitHub Pages)
requirements.txt     Python dependencies
render.yaml          Render deployment config
car_prediction.ipynb Original training notebook
cleaned_car.csv      Cleaned dataset
```

---

## Tech Stack

- **Model:** scikit-learn (LinearRegression, OneHotEncoder, Pipeline)
- **Backend:** Flask, Gunicorn
- **Frontend:** HTML, CSS, Vanilla JS
- **Hosting:** GitHub Pages (frontend), Render (backend)

---

## Local Setup

**1. Clone the repo**

```bash
git clone https://github.com/samyamoy1/-Car-Price-Predictor-Project.git
cd -Car-Price-Predictor-Project
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the API**

```bash
python app.py
```

API will be available at `http://localhost:5000`.

**4. Update the frontend**

Open `index.html` and change the `API_URL` at the top of the script:

```js
const API_URL = 'http://localhost:5000/predict';
```

Open `index.html` in a browser and test.

---

## API Reference

**POST** `/predict`

Request body:

```json
{
  "name": "Hyundai Grand i10",
  "company": "Hyundai",
  "year": 2017,
  "kms_driven": 35000,
  "fuel_type": "Petrol"
}
```

Response:

```json
{
  "price": 385000
}
```

---

## Data Cleaning Steps

The raw Quikr dataset required significant cleaning before training:

- Removed rows where `year` contained non-numeric values
- Removed rows where `Price` was listed as "Ask For Price"
- Stripped units and commas from `kms_driven`, converted to integer
- Dropped rows with null `fuel_type`
- Truncated car name to first three words
- Removed outliers where `Price` exceeded 60,00,000
- Reset index after all filtering

---

## Author

Samyamoy — [GitHub](https://github.com/samyamoy1)
