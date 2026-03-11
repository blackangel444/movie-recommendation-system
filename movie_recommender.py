import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# Merge datasets
movies = movies.merge(credits, on='title')

# Select important columns
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

# Fill missing values
movies = movies.fillna('')

# Combine features into one column
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast']

# Convert text to vectors
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Compute similarity matrix
similarity = cosine_similarity(vectors)

def recommend(movie):

    movie = movie.lower()

    # convert titles to lowercase
    movies['title_lower'] = movies['title'].str.lower()

    if movie not in movies['title_lower'].values:
        print("Movie not found in dataset.")
        return

    movie_index = movies[movies['title_lower'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    print("\nRecommended movies:\n")

    for i in movie_list:
        print(movies.iloc[i[0]].title)

# User input
movie_name = input("Enter a movie name: ")

recommend(movie_name)
