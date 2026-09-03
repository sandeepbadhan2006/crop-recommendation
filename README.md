## CROP PRICE PREDICTION

📌 **Project Overview**
The Crop Price Prediction System is a machine learning model designed to forecast agricultural crop prices based on factors like historical price data, environmental conditions. It helps farmers and agricultural stakeholders make data-driven decisions.

---

🛠️ **Project Architecture & Structure**
```text
.
├── .ipynb_checkpoints/    # Jupyter notebook checkpoints
├── artifacts/              # Trained models, scalers, and encoder files
├── dataset/                # Historical crop price datasets
├── env/                    # Virtual environment configuration
├── notebook/               # Exploratory Data Analysis (EDA) and model training
├── src.egg-info/           # Package build metadata
├── README.md               # Project documentation
├── app.py                  # Web application file
├── requirements.txt        # Python dependencies
└── setup.py                # Package setup script

```
---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv .env
```

## 3️⃣ Activate the Virtual Environment

### Windows

```bash
.env\Scripts\activate
```

### Linux / macOS

```bash
source .env/bin/activate
```

After activation, you should see:

```text
(.env)
```

at the beginning of your terminal.

## 4️⃣ Upgrade pip

```bash
python -m pip install --upgrade pip
```

## 5️⃣ Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

## Running The Application

```bash
streamlit run app.py
```
---

