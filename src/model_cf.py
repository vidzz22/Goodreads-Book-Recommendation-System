import pandas as pd
from sklearn.decomposition import TruncatedSVD

def train_svd(sample_size=5000):
    ratings = pd.read_csv("data/ratings.csv")

    # 🔥 IMPORTANT: reduce size to avoid memory error
    ratings = ratings.sample(n=sample_size, random_state=42)

    user_item = ratings.pivot_table(
        index="user_id",
        columns="book_id",
        values="rating"
    ).fillna(0)

    svd = TruncatedSVD(n_components=20)
    matrix = svd.fit_transform(user_item)

    return user_item, matrix


def recommend_svd(user_id, user_item, matrix, books_df, n=10):
    if user_id not in user_item.index:
        return []

    user_index = user_item.index.get_loc(user_id)
    scores = matrix[user_index]

    top_items = scores.argsort()[::-1][:n]
    book_ids = user_item.columns[top_items]

    return books_df[books_df["book_id"].isin(book_ids)]["title"].tolist()