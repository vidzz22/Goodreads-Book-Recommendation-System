def explain_model(model_name):
    if model_name == "Rank-Based":
        return "Recommends popular books based on average rating."

    elif model_name == "User-CF":
        return "Finds similar users and recommends books they liked."

    elif model_name == "SVD":
        return "Uses matrix factorization to learn hidden patterns."

    else:
        return "Hybrid model combining multiple techniques."