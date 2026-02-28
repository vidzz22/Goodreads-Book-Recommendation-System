📚 Goodreads Book Recommendation System
📌 Project Overview

This project implements multiple recommendation approaches using the Goodreads (Goodbooks-10k) dataset.

The objective is to build and compare different recommendation strategies to understand:

Popularity-based recommendations

Memory-based collaborative filtering

Model-based collaborative filtering

Cold start challenges in recommender systems

Dataset Source:
https://www.kaggle.com/datasets/zygmunt/goodbooks-10k

📂 Project Structure
Goodreads-Book-Recommendation-System/
│
├── rank_based_book_recommendation.ipynb
├── User_based_collaborative_filtering.ipynb
├── Model_based_collaborative_filtering.ipynb
│
└── data/
    ├── books.csv
    ├── ratings.csv
📊 Dataset Information

Number of users: 53,424

Number of books: 10,000

Total ratings: 981,756

Sparsity: ~99.8%

The dataset is highly sparse, making recommendation modeling more challenging.

🔹 1️⃣ Rank-Based Recommendation

This method recommends books based on:

Average rating

Minimum number of ratings

It is useful for:

New users (cold start problem)

Quick baseline recommendations

Advantages:

Simple

Fast

No user similarity required

Limitations:

Not personalized

🔹 2️⃣ User-Based Collaborative Filtering

This method:

Creates a user–book interaction matrix

Computes cosine similarity between users

Recommends books liked by similar users

Advantages:

Personalized recommendations

Intuitive similarity approach

Limitations:

Memory intensive

Not scalable for very large datasets

🔹 3️⃣ Model-Based Collaborative Filtering (SVD)

This method:

Applies Singular Value Decomposition (SVD)

Learns latent factors

Reconstructs predicted rating matrix

Advantages:

Handles sparsity better

More scalable

Captures hidden user–item patterns

Evaluation:

RMSE computed on reconstructed ratings

❄️ Cold Start Problem

The cold start problem occurs when:

A new user has no rating history

A new book has no ratings

In such cases, rank-based recommendations serve as a fallback solution.

🛠 Technologies Used

Python

Pandas

NumPy

Scikit-learn

Google Colab

🚀 How to Run

Clone repository

Place dataset inside data/

Run notebooks in order:

Rank-based

User-based

Model-based

📌 Key Learnings

Recommender systems suffer from sparsity issues

Memory-based methods are intuitive but heavy

Model-based approaches scale better

Cold start requires hybrid strategies

👩‍💻 Author

Vidhya
