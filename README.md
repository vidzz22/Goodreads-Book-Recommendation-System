# 📚 Goodreads Book Recommendation System

---

## 📌 Overview

This project implements and compares multiple recommendation strategies using the **Goodreads (Goodbooks-10k)** dataset.

The objective is to analyze how different recommendation approaches behave under high data sparsity.

**Dataset:**  
https://www.kaggle.com/datasets/zygmunt/goodbooks-10k

---


## 📊 Dataset Statistics

- **Number of Users:** 53,424  
- **Number of Books:** 10,000  
- **Total Ratings:** 981,756  
- **Sparsity:** ~99.8%

The dataset is highly sparse, making recommendation modeling both challenging and realistic.

---

# 🔹 Implemented Approaches

## 1️⃣ Rank-Based Recommendation

Recommends books based on:

- Average rating  
- Minimum number of ratings  

This method acts as a baseline and is useful for:

- New users (cold start problem)  
- Quick recommendations  

### ✅ Advantages
- Simple and fast  
- No similarity computation required  
- Highly scalable  

### ❌ Limitation
- Not personalized  

---

## 2️⃣ User-Based Collaborative Filtering

**Process:**

- Construct user–book interaction matrix  
- Compute cosine similarity between users  
- Recommend books liked by similar users  

### ✅ Advantages
- Personalized recommendations  
- Intuitive similarity-based logic  

### ❌ Limitations
- Memory intensive  
- Not scalable for very large datasets  

---

## 3️⃣ Model-Based Collaborative Filtering (SVD)

This approach:

- Applies Singular Value Decomposition (SVD)  
- Learns latent user and item factors  
- Reconstructs predicted ratings  

### ✅ Advantages
- Handles sparsity better  
- More scalable than memory-based methods  
- Captures hidden interaction patterns  

### 📈 Evaluation
- RMSE computed on reconstructed ratings  

---

## Cold Start Problem

The cold start problem occurs when:

- A new user has no rating history  
- A new book has no interactions  

In such cases, rank-based recommendation serves as a fallback solution.

---

## 🛠 Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Google Colab  

---

## 🚀 How to Run

1. Clone the repository  
2. Place dataset files inside the `data/` folder  
3. Run notebooks in order:
   - Rank-based recommendation  
   - User-based collaborative filtering  
   - Model-based collaborative filtering  

---

## 📌 Key Takeaways

- High sparsity significantly impacts recommendation systems  
- Memory-based methods are intuitive but computationally heavy  
- Model-based approaches scale better  
- Hybrid strategies are required in production systems  

---
