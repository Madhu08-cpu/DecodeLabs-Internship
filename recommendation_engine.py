import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load Dataset (or create a sample dataframe)
data = {
    'role': ['Data Scientist', 'DevOps Engineer', 'Backend Developer', 'Frontend Developer'],
    'skills': [
        'Python SQL Machine Learning Data Analysis Statistics',
        'AWS Docker Kubernetes CI/CD Linux Terraform',
        'Java Python SQL APIs Microservices Node.js',
        'JavaScript React HTML CSS UI UX TypeScript'
    ]
}
df = pd.DataFrame(data)

print("--- WELCOME TO DECODELABS TECH STACK RECOMMENDER ---")

# 2. Input: Capture user state (Minimum 3 inputs as required)
print("\nEnter your top 3 preferred skills or technologies:")
input_1 = input("Skill 1: ")
input_2 = input("Skill 2: ")
input_3 = input("Skill 3: ")

# Combine user inputs into a single query string
user_profile = f"{input_1} {input_2} {input_3}"

# 3. Process: TF-IDF Vectorization & Cosine Similarity
# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the job skills, and transform the user profile
tfidf_matrix_skills = vectorizer.fit_transform(df['skills'])
tfidf_matrix_user = vectorizer.transform([user_profile])

# Calculate Cosine Similarity scores
similarity_scores = cosine_similarity(tfidf_matrix_user, tfidf_matrix_skills)

# Add scores to the dataframe
df['match_score'] = similarity_scores[0]

# Sort results by highest match score
ranked_recommendations = df.sort_values(by='match_score', ascending=False)

# 4. Output: Display Top-N Recommendations
print("\n--- TOP MATCHED JOB ROLES ---")
for index, row in ranked_recommendations.iterrows():
    percentage = round(row['match_score'] * 100, 2)
    print(f"👉 {row['role']} (Match Confidence: {percentage}%)")