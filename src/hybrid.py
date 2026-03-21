from src.rank_based import get_top_books
from src.model_cf import train_svd, recommend_svd

user_item = None
matrix = None

def hybrid_recommend(user_id, books):
    global user_item, matrix

    if user_item is None or matrix is None:
        user_item, matrix = train_svd()

    if user_id in user_item.index:
        return recommend_svd(user_id, user_item, matrix, books)
    else:
        return get_top_books()