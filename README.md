# Car Price Predictor

Linear Regression model trained on Quikr used cars dataset. R² = 0.899.

## Files

```
car_model.pkl        # trained model (random_state=302)
app.py               # Flask API
index.html           # frontend
requirements.txt
render.yaml
```

## Deploy Backend on Render (free)

1. Push this folder to GitHub
2. Go to https://render.com → New → Web Service
3. Connect your GitHub repo
4. Settings:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
   - Plan: Free
5. Click Deploy. Wait ~2 min.
6. Copy your app URL: `https://your-app-name.onrender.com`

## Update Frontend

Open `index.html`, find this line at the top of the script:

```js
const API_URL = 'https://your-app-name.onrender.com/predict';
```

Replace with your actual Render URL.

## Deploy Frontend on GitHub Pages

1. Go to repo Settings → Pages
2. Source: `main` branch, `/ (root)` folder
3. Save. Site live at: `https://yourusername.github.io/yourrepo`

## Local Testing

```bash
pip install -r requirements.txt
python app.py
# API runs at http://localhost:5000
# Change API_URL in index.html to http://localhost:5000/predict
```

## Model Info

- Algorithm: Linear Regression with OneHotEncoding
- Features: name, company, year, kms_driven, fuel_type
- Target: Price (INR)
- Dataset: Quikr used cars (815 records after cleaning)
- Best random_state: 302
