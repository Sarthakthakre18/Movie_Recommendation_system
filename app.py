from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

movies = pickle.load(open("models/movies.pkl", "rb"))
similarity = pickle.load(open("models/similarity.pkl", "rb"))

def recommend(movie):

    movie_data = movies[movies["title"] == movie]

    if movie_data.empty:
        return ["Movie not found"]

    movie_index = movie_data.index[0]

    distance = similarity[movie_index]

    movie_list = list(enumerate(distance))

    sorted_movies = sorted(
        movie_list,
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for i in sorted_movies[1:6]:
        recommendations.append(
            movies.iloc[i[0]].title
        )

    return recommendations

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        movie = request.form["movie"]

        recommendations = recommend(movie)

    return render_template(
        "index.html",
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)