# 🌸 BloomWatch — Smart Bloom Stage & Crop Prediction System  
A complete geospatial + machine learning system designed for predicting **Bloom Stages**, **Crop Types**, and **6-Month Forecasts** across the **Nashik agricultural region**, divided into **64 uniform tiles**.  
This repository contains the **React Frontend**, **FastAPI Backend**, and **ML CSV Outputs** that power BloomWatch.

---

# 📌 Project Overview

Agricultural forecasting is traditionally challenging due to climate variability, satellite data complexity, and data preprocessing overhead. **BloomWatch solves this** by combining:

- 🛰️ Satellite-based environmental parameters  
- 🤖 Machine Learning models trained in Google Colab  
- 🌍 A region-specific grid (Nashik → 64 tiles)  
- ⚡ A simple and efficient FastAPI backend  
- 💻 A React-based interactive map dashboard  

BloomWatch enables farmers and researchers to visualize **bloom stages**, **crop distribution**, and **future predictions** tile-by-tile.

---

# ⚠️ Important Notes About This Version

### 🚧 1. Colab Live Backend Not Used (Due to Time Constraint)
The original plan was to connect the FastAPI backend directly to Google Colab for **real-time ML inference**, but due to strict deadlines:

- Instead of live inference  
- We use **pre-generated CSV predictions** from Colab notebooks  
- These are served through FastAPI for fast & consistent results  

### 🚧 2. Multilingual Chatbot Not Completed
The system was planned to include a **multilanguage farm assistant chatbot** for personalized guidance, but this feature is **not implemented** due to time constraints.

Both features remain part of the roadmap.

---

# 🌍 Region Details — Nashik (64 Tiles)

The Nashik agricultural area was divided into **64 uniform tiles**.  
Each tile has:

- A unique **Tile ID**
- Latitude & longitude boundaries  
- Bloom stage prediction  
- Crop type prediction  
- 6 months future bloom forecasts  
- Probability scores (dynamic for each tile)

These tiles are the core dataset powering BloomWatch.

---

# 🧠 Machine Learning Approach

### Data Sources
The ML models were trained in Google Colab using:

- **NDVI**
- **EVI**
- **Land Surface Temperature (LST)**
- **Precipitation**
- **Soil Moisture**
- **Vegetation Indices**
- **Topography (DEM)**  
- **Custom domain features**

### ML Models Used
- Random Forest  
- XGBoost  
- Stacking classifiers  
- Time-series forecasting models  
- Probability-based ensemble scoring  

### Outputs Generated (From Colab)
The ML pipeline outputs multiple CSVs:

- **bloom_predictions.csv** → Bloom stage per tile  
- **crop_predictions.csv** → Crop class per tile  
- **future_predictions_6months_dynamic_prob.csv** → 11,520 future predictions  
- **tile_master.csv** → Final consolidated dataset  

These CSVs are placed in `/backend/data/`.

---

# 🧩 Full Project Structure

```
BloomWatch/
│
├── frontend/                    # React frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── MapView.js
│   │   │   ├── TileCard.js
│   │   │   └── PredictionsPanel.js
│   │   ├── pages/
│   │   │   └── Home.js
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   │   └── map_assets/
│   └── package.json
│
├── backend/                    # FastAPI backend
│   ├── main.py                 # Backend entrypoint
│   ├── data/                   # All ML CSV outputs
│   │   ├── tile_master.csv
│   │   ├── bloom_predictions.csv
│   │   ├── crop_predictions.csv
│   │   └── future_predictions_6months_dynamic_prob.csv
│   ├── models/                 # (Optional) ML models
│   └── requirements.txt
│
└── ml/                         # Google Colab notebooks
    ├── preprocessing.ipynb
    ├── training.ipynb
    └── forecasting.ipynb
```

---

# ⚡ FastAPI Backend — How It Works

The backend does **not** run ML models live.  
Instead, it:

- Loads CSV files  
- Filters records based on tile  
- Sends bloom stage, crop predictions, and forecasts  
- Returns probability distributions for better insights  

### Backend Startup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### API Endpoints (Sample)
| Endpoint | Description |
|---------|-------------|
| `/predict/bloom/{tile_id}` | Returns bloom stage for a specific tile |
| `/predict/crop/{tile_id}` | Returns crop class |
| `/predict/forecast/{tile_id}` | 6-month bloom forecast |
| `/tiles/all` | Return full dataset |

---

# 💻 React Frontend — Features

### Interactive Map
- Shows all 64 tiles  
- Click any tile to view predictions  
- Smooth animations  
- Color-coded bloom stages  

### Tile Information Panel
- Bloom stage with label (1–5)  
- Crop class  
- Probabilities visualization  
- Historical tile data  

### Forecast View
- 6-month future predictions  
- Graph view (line/area charts)  
- Dynamic probability scores  

To run:

```bash
cd frontend
npm install
npm start
```

---

# 📦 Datasets Included

### `tile_master.csv`
Master reference for all 64 tiles.

### `bloom_predictions.csv`
Primary model predictions for bloom stages.

### `crop_predictions.csv`
ML-based crop classification.

### `future_predictions_6months_dynamic_prob.csv`
11,520 rows generated from forecasting models.

All are stored under:

```
/backend/data/
```

---

# 🔮 Roadmap (Future Work)

| Feature | Status | Notes |
|---------|--------|-------|
| Multilanguage chatbot | ❌ Pending | Not completed due to time constraints |
| Real-time Colab inference | ❌ Pending | Currently running via CSV backend |
| Mobile App | Planned | Likely Flutter/React Native |
| Full GIS integration | Planned | Live NDVI/EVI from GEE |
| Farmer advisory alerts | Planned | SMS + WhatsApp |

---

# 📚 Technologies Used

### **Frontend**
- React  
- Leaflet Maps  
- Axios  
- Recharts  

### **Backend**
- FastAPI  
- Pandas  
- Uvicorn  
- Numpy  
- Scikit-learn  
- XGBoost  

### **Machine Learning**
- Google Colab  
- SMOTE  
- Hyperparameter tuning  
- Stacking classifiers  
- Time-series forecasting  

---

# 👩‍🌾 Why BloomWatch?

- Helps farmers plan crop cycles  
- Predicts blooming phases accurately  
- Useful for vineyard, pomegranate, and mango regions  
- Assists agricultural researchers  
- Scalable for other districts beyond Nashik  

---

## 🎥 Demo Video (Add Your Link Below)
👉 **Demo Video:** *Add YouTube or Google Drive link here*


# 👥 Team

**Developed by:**  
 -Harshada Dhamne  
 -Mayur Khalse   
 -Krishna Lohakare  
 -Samruddhi Kadam   


---

# ⭐ Support The Project

If BloomWatch helped or inspired you, please consider starring the repo:

> ⭐ **Star this repository on GitHub!**

It motivates us to continue building.

---

# 📄 License
This project is released under an open license for research & educational purposes.

