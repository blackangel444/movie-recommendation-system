# Movie Recommendation System

A **content-based Movie Recommendation System** built with **Python and Machine Learning**.
The system analyzes movie metadata from the **TMDB dataset** and recommends movies similar to the one entered by the user.

The project also integrates the **TMDB API** to fetch additional movie information such as **movie posters**.

---

## Overview

This project uses **Natural Language Processing (NLP)** and **cosine similarity** to recommend movies based on features such as:

* Movie overview
* Genres
* Keywords
* Cast information

These features are converted into numerical vectors and compared using **cosine similarity** to find similar movies.

---

## Features

* Content-based movie recommendation
* Uses movie metadata from TMDB dataset
* Calculates similarity using cosine similarity
* Recommends top similar movies
* Integration with **TMDB API** for movie data
* Beginner-friendly Machine Learning project

---

## Dataset

This project uses the **TMDB 5000 Movie Dataset**.

Files used:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

Dataset source:

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## TMDB API

This project uses the **TMDB API** to retrieve additional movie information such as **poster images**.

To use the API:

1. Create an account on TMDB
   https://www.themoviedb.org

2. Generate your API key from the account settings.

3. Add your API key inside the code:

```python
api_key = "YOUR_TMDB_API_KEY"
```

⚠️ Do not upload your real API key to GitHub.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* TMDB API
* Natural Language Processing (NLP)

---

## Machine Learning Concepts Used

* Feature Engineering
* Text Vectorization
* CountVectorizer
* Cosine Similarity
* Content-Based Filtering

---

## Project Structure

```
movie-recommendation-system
│
├── movie_recommender.py
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/blackangel444/movie-recommendation-system.git
```

Navigate to the project folder

```
cd movie-recommendation-system
```

Install dependencies

```
pip install -r requirements.txt
```

---

## How to Run

Run the program using:

```
python movie_recommender.py
```

Enter a movie name when prompted.

Example:

```
Enter a movie name: Inception
```

Output:

```
Recommended Movies:

Interstellar
The Prestige
Memento
The Dark Knight
Looper
```

---

## Future Improvements

Possible upgrades:

* Web interface using Streamlit or Flask
* Display movie posters
* Add search suggestions
* Improve recommendation algorithm
* Deploy as a web application

---

## Author

Suyash Gawde
