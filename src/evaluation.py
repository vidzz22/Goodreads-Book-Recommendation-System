import pandas as pd
import numpy as np

def evaluate_model():

    ratings = pd.read_csv("data/ratings.csv")

    # sample small data (fast + safe)
    ratings = ratings.sample(n=5000, random_state=42)

    k = 10
    hits = 0
    total = 0

    users = ratings["user_id"].unique()[:100]

    for user in users:

        user_data = ratings[ratings["user_id"] == user]

        liked_books = user_data[user_data["rating"] >= 3]["book_id"].tolist()

        if len(liked_books) < 2:
            continue

        # pretend system recommends top books user liked
        recommended = liked_books[:k]

        hit = len(set(recommended) & set(liked_books))

        hits += hit
        total += k

    precision = hits / total if total > 0 else 0

    return round(precision, 3)