import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def user_cf_recommend(user_id, n=10):
    ratings = pd.read_csv("data/ratings.csv")
    books = pd.read_csv("data/books.csv")

    # sample to reduce size
    ratings = ratings.sample(n=5000, random_state=42)

    user_item = ratings.pivot_table(
        index="user_id",
        columns="book_id",
        values="rating"
    ).fillna(0)

    if user_id not in user_item.index:
        return []

    similarity = cosine_similarity(user_item)
    sim_df = pd.DataFrame(similarity, index=user_item.index, columns=user_item.index)

    similar_users = sim_df[user_id].sort_values(ascending=False)[1:6].index

    recs = user_item.loc[similar_users].mean().sort_values(ascending=False).head(n)

    return books[books["book_id"].isin(recs.index)]["title"].tolist()