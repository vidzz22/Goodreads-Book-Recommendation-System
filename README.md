Goodreads Book Recommendation System
Overview

This project implements and compares multiple recommendation strategies using the Goodreads (Goodbooks-10k) dataset.

The objective is to analyze how different recommendation approaches behave under high data sparsity and to understand their scalability, personalization capability, and suitability for cold start scenarios.

Dataset: https://www.kaggle.com/datasets/zygmunt/goodbooks-10k

Project Structure
Goodreads-Book-Recommendation-System/
│
├── rank_based_book_recommendation.ipynb
├── User_based_collaborative_filtering.ipynb
├── Model_based_collaborative_filtering.ipynb
│
└── data/
    ├── books.csv
    ├── ratings.csv
Dataset Statistics

Number of Users: 53,424

Number of Books: 10,000

Total Ratings: 981,756

Sparsity: ~99.8%

The dataset is highly sparse, which makes recommendation modeling challenging and realistic.

Implemented Approaches
1. Rank-Based Recommendation

Recommends books based on:

Average rating

Minimum number of ratings

This method serves as a baseline and works well for new users (cold start problem).

Advantages

Simple and fast

No similarity computation required

Scalable

Limitation

Not personalized

2. User-Based Collaborative Filtering

Steps:

Construct user–book interaction matrix

Compute cosine similarity between users

Recommend books liked by similar users

Advantages

Personalized recommendations

Intuitive similarity-based logic

Limitations

Memory intensive

Not scalable for very large user bases

3. Model-Based Collaborative Filtering (SVD)

This approach uses Singular Value Decomposition (SVD) to:

Learn latent user and item factors

Reconstruct predicted rating matrix

Generate top-N personalized recommendations

Advantages

Handles sparsity better

More scalable than memory-based methods

Captures hidden user–item interactions

Evaluation Metric

RMSE computed on reconstructed ratings

Cold Start Problem

The cold start problem occurs when:

A new user has no rating history

A new book has no interactions

In such cases, rank-based recommendations act as a fallback strategy.

Technologies Used

Python

Pandas

NumPy

Scikit-learn

Google Colab

How to Run

Clone the repository

Ensure dataset files are placed inside the data/ folder

Run notebooks in the following order:

Rank-based recommendation

User-based collaborative filtering

Model-based collaborative filtering

Key Takeaways

High sparsity significantly impacts recommendation quality.

Memory-based collaborative filtering is intuitive but computationally expensive.

Model-based approaches scale better and generalize more effectively.

Hybrid strategies are often required in production systems.

Author

Vidhya Walke
