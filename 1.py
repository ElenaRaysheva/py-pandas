import pandas as pd

ratings = pd.read_csv("./ratings.csv")
movies = pd.read_csv("./movies.csv")
result = ratings[ratings["rating"] == 5.0].set_index("movieId").groupby("movieId").count().sort_values("rating", ascending=False).join(movies.set_index("movieId")).head(1)

print(result.title) # Shawshank Redemption, The (1994)
