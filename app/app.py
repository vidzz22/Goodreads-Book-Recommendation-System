from src.evaluation import evaluate_model
import streamlit as st
import pandas as pd

from src.rank_based import get_top_books
from src.user_cf import user_cf_recommend
from src.model_cf import train_svd, recommend_svd

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="Book Recommendation System", layout="wide")

# ---------------------------
# TITLE
# ---------------------------
st.title("Book Recommendation System")

st.write("""
This system recommends books using:
- Popularity-based method
- Collaborative Filtering (User-based)
- Model-based approach (SVD)
""")

# ---------------------------
# LOAD DATA
# ---------------------------
books = pd.read_csv("data/books.csv")
ratings = pd.read_csv("data/ratings.csv")

# ---------------------------
# SIDEBAR INPUT
# ---------------------------
st.sidebar.header("User Input")

book_list = books["title"].dropna().unique().tolist()[:100]

selected_books = st.sidebar.multiselect(
    "Select up to 5 books",
    book_list,
    max_selections=5,
    placeholder="Choose books..."
)

# ---------------------------
# DISPLAY FUNCTION
# ---------------------------
def display_books(title, recs, reason):
    st.subheader(title)

    if len(recs) == 0:
        st.write("No recommendations available.")
        return

    cols = st.columns(5)

    for i, book in enumerate(recs):
        with cols[i % 5]:
            st.markdown(f"""
                <div style="padding:12px;border:1px solid #ddd;border-radius:10px;height:130px;">
                    <b>{book[:40]}</b><br>
                    <span style="font-size:12px;color:gray;">
                        {reason}
                    </span>
                </div>
            """, unsafe_allow_html=True)

# ---------------------------
# DIRECT PERSONALIZATION
# ---------------------------
def direct_personalization():

    if len(selected_books) == 0:
        return get_top_books()

    selected_ids = books[books["title"].isin(selected_books)]["book_id"].tolist()

    similar_users = ratings[
        (ratings["book_id"].isin(selected_ids)) &
        (ratings["rating"] >= 4)
    ]["user_id"].unique()

    if len(similar_users) == 0:
        return get_top_books()

    recs = ratings[
        ratings["user_id"].isin(similar_users)
    ]["book_id"].value_counts().head(10).index.tolist()

    recs = [b for b in recs if b not in selected_ids]

    final = books[books["book_id"].isin(recs)]["title"].tolist()

    if len(final) == 0:
        return get_top_books()

    return final

# ---------------------------
# TRAIN SVD
# ---------------------------
user_item, matrix = train_svd()

# ---------------------------
# MAIN BUTTON
# ---------------------------
if st.button("Generate Recommendations"):

    # 1. Popular
    display_books("Trending", get_top_books(), "Popular among users")

    # 2. SVD
    if selected_books:
        svd_recs = recommend_svd(
            ratings["user_id"].iloc[0],
            user_item,
            matrix,
            books
        )
        display_books("Recommended for You (SVD)", svd_recs, "Based on patterns")

    # 3. User-CF
    if selected_books:
        cf_recs = user_cf_recommend(ratings["user_id"].iloc[1])
        display_books("Similar Users Liked", cf_recs, "Based on similar users")

    # 4. Direct Personalization
    dp_recs = direct_personalization()
    display_books("Based on Your Selection", dp_recs, "From your input")

    # ---------------------------
    # SIMPLE EVALUATION
    # ---------------------------
    st.markdown("---")
    st.subheader("Model Evaluation")

    precision = evaluate_model()

    st.write(f"Precision@K: {precision}")
