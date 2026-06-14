# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Machine Learning, Natural Language Processing (NLP), and Flask.

## 📌 Overview

This project recommends movies similar to a user's selected movie by analyzing movie metadata such as genres, keywords, cast, crew, and overview.

The recommendation engine uses NLP techniques and Cosine Similarity to identify movies with similar content.

---

## 🚀 Features

* Recommend Top 5 similar movies
* Content-based recommendation approach
* NLP preprocessing and feature engineering
* Interactive web interface using Flask
* Fast recommendations using precomputed similarity matrix

---

## 🛠️ Tech Stack

### Machine Learning & Data Processing

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK

### NLP Techniques

* Text Preprocessing
* Stemming
* CountVectorizer

### Similarity Measurement

* Cosine Similarity

### Web Development

* Flask
* HTML
* CSS

---

## 📂 Project Structure

```text
Movie_Recommendation_System/
│
├── data/
│   ├── movies.csv
│   └── credits.csv
│
├── models/
│   ├── movies.pkl
│   └── similarity.pkl
│
├── notebooks/
│   └── movie_recommendation.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Workflow

### 1. Data Collection

* movies.csv
* credits.csv

### 2. Data Preprocessing

* Merge datasets
* Select important features
* Handle missing values

### 3. Feature Engineering

Extract:

* Genres
* Keywords
* Cast
* Director
* Overview

### 4. NLP Processing

* Remove spaces from names
* Create tags feature
* Apply stemming

### 5. Vectorization

Convert movie tags into numerical vectors using CountVectorizer.

### 6. Similarity Calculation

Calculate similarity scores using Cosine Similarity.

### 7. Recommendation Generation

For a given movie:

* Find movie index
* Retrieve similarity scores
* Sort movies by similarity
* Return top 5 recommendations

---

## ▶️ How to Run

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Flask App

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## 📊 Example

Input:

```text
Avatar
```

Output:

```text
Top 5 similar movie recommendations
```

---

## 🎯 Key Learnings

* Data Preprocessing
* Feature Engineering
* Natural Language Processing
* Recommendation Systems
* Cosine Similarity
* Model Serialization using Pickle
* Flask Integration
* End-to-End Machine Learning Application Development

---

## 📚 Dataset

TMDB 5000 Movie Dataset

* movies.csv
* credits.csv

---

## 👨‍💻 Author

Sarthak Thakre

AIML Engineering Student | Python | Machine Learning | Data Science
