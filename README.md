# Smart Health Diagnostic Assistant

A simple machine-learning based health diagnostic assistant that predicts possible diseases based on user-selected symptoms.  
This project includes a prediction model, a Streamlit web app, and a Jupyter notebook showing full training and evaluation steps.

---

## 🚀 Features

- ✔️ Select multiple symptoms  
- ✔️ ML model predicts the possible disease  
- ✔️ Shows prediction confidence  
- ✔️ Preventions (coming soon — planned improvement)  
- ✔️ Lightweight and easy to deploy  

---

## 🧠 Machine Learning Model

- Model Type: **Decision Tree Classifier**  
- Framework: **scikit-learn**  
- Training done in Jupyter Notebook included in the repo  
- Saved as: `disease_model.pkl`

---

## 📁 Project Structure

Smart Health Diagnostic Assistant project/
│── app.py # Streamlit app
│── disease_model.pkl # ML model
│── Smart Health Diagnostic Assistant.ipynb # Jupyter notebook
│── Data/ # (empty for now)
│── Models/ # (empty for now)
│── Reports/ # (empty for now)
│── Utils/ # (empty for now)



---

## 🛠️ Tech Stack

- **Python 3.10**
- **Streamlit**
- **scikit-learn**
- **pandas, numpy**
- **Jupyter Notebook**

---

## ▶️ How to Run the Project

Step 1 — Create Virtual Environment
```bash
conda create -n healthenv python=3.10
conda activate healthenv

Step 2 — Install Requirements
pip install streamlit scikit-learn pandas numpy

Step 3 — Run the App
streamlit run app.py

📌 Future Improvements

⬜ Add prevention & treatment recommendations

⬜ Add medicine suggestions

⬜ Add disease descriptions

⬜ Improve UI of the Streamlit app

⬜ Deploy publicly on Streamlit Cloud
