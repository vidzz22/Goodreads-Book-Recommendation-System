import pandas as pd

def get_top_books(n=10):
    ratings = pd.read_csv("data/ratings.csv")
    books = pd.read_csv("data/books.csv")

    avg = ratings.groupby("book_id")["rating"].mean()
    count = ratings.groupby("book_id")["rating"].count()

    df = pd.DataFrame({
        "avg_rating": avg,
        "count": count
    })

    df = df[df["count"] > 50]
    df = df.sort_values("avg_rating", ascending=False).head(n)

    result = books[books["book_id"].isin(df.index)]

    return result["title"].tolist()