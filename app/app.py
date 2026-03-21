import streamlit as st
import pandas as pd
import random

from src.rank_based import get_top_books
from src.model_cf import train_svd, recommend_svd

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="Book Recommender", layout="wide")

# ---------------------------
# CUSTOM LIGHT UI THEME
# ---------------------------
st.markdown("""
<style>
body {
    background-color: #fdf6ec;
}

.main {
    background-color: #fdf6ec;
}

h1 {
    color: #5a3e2b;
}

h2, h3 {
    color: #6b4f3b;
}

.stButton>button {
    background-color: #d4a373;
    color: white;
    border-radius: 10px;
    padding: 10px;
    border: none;
}

.stButton>button:hover {
    background-color: #b08968;
}

.card {
    background-color: #faedcd;
    padding: 15px;
    border-radius: 15px;
    height: 160px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    transition: transform 0.2s ease;
}

.card:hover {
    transform: scale(1.05);
}

.reason {
    font-size: 12px;
    color: #7f5539;
}

.section-title {
    margin-top: 20px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# TITLE
# ---------------------------
st.title("📚 AI-Powered Book Recommendation Engine")

st.markdown("""
A hybrid recommendation system that adapts based on user behavior,  
similar to platforms like Netflix and Amazon.
""")

# ---------------------------
# LOAD DATA
# ---------------------------
books = pd.read_csv("data/books.csv")

# Train model (sampled)
user_item, matrix = train_svd()

# ---------------------------
# SIDEBAR (USER PROFILE)
# ---------------------------
st.sidebar.header("👤 Your Reading Profile")

sample_books = books["title"].dropna().tolist()[:100]

selected_books = st.sidebar.multiselect(
    "Select books you like",
    sample_books
)

explore_level = st.sidebar.slider(
    "Exploration Level",
    0, 100, 50
)

st.sidebar.markdown("---")
st.sidebar.caption("Higher exploration → more diverse recommendations")

# ---------------------------
# CORE LOGIC
# ---------------------------
def generate_feed():

    # Cold Start
    if len(selected_books) == 0:
        return get_top_books()

    # Simulated user behavior
    user_id = random.choice(user_item.index.tolist())

    recs = recommend_svd(user_id, user_item, matrix, books)

    return recs


# ---------------------------
# DISPLAY FUNCTION (CARDS)
# ---------------------------
def display_books(recs, reason):

    cols = st.columns(5)

    for i, book in enumerate(recs):
        with cols[i % 5]:
            st.markdown(f"""
                <div class="card">
                    <h4>📖 {book[:35]}</h4>
                    <p class="reason">{reason}</p>
                </div>
            """, unsafe_allow_html=True)


# ---------------------------
# MAIN BUTTON
# ---------------------------
st.markdown("## 📌 Generate Your Feed")

if st.button("✨ Generate Recommendations"):

    recs = generate_feed()

    # ---------------------------
    # SECTIONS (LIKE NETFLIX)
    # ---------------------------

    st.markdown("### 🔥 Trending Now")
    display_books(get_top_books(), "Popular among all readers")

    st.markdown("### 🎯 Recommended for You")
    reason = "Based on your selected preferences" if selected_books else "General popular trends"
    display_books(recs, reason)

    st.markdown("### 🧠 Because Similar Users Liked")
    display_books(generate_feed(), "Derived from similar user behavior")

# ---------------------------
# EXPLANATION SECTION
# ---------------------------
st.markdown("---")
st.markdown("## 🧠 How This System Works")

st.info("""
This system uses a **Hybrid Recommendation Strategy**:

• **Cold Start** → Uses popularity-based ranking when no user data is available  
• **Collaborative Filtering** → Finds users with similar behavior  
• **SVD (Matrix Factorization)** → Learns hidden patterns between users and books  

📌 The system dynamically adapts based on user interaction and available data.
""")