# ==========================================
# DECODELABS: PROJECT 2 - DATA CLASSIFICATION
# Supervised Learning Pipeline
# ==========================================

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def run_classification_pipeline():
    print("--- DecodeLabs AI Engine: Supervised Classification ---")
    
    # 1. Load and Understand the Dataset
    # We use the built-in Iris dataset (featuring sepal length/width and petal length/width)
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target
    
    print(f"\n[INFO] Dataset loaded successfully with {X.shape[0]} samples and {X.shape[1]} features.")
    
    # 2. Structural Integrity: The Split (Shuffling to remove order bias)
    # 80% for training pattern recognition, 20% for testing/validation
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=True
    )
    print(f"[INFO] Data split completed: {X_train.shape[0]} training samples, {X_test.shape[0]} test samples.")
    
    # 3. The Gatekeeper Rule: Feature Scaling
    # Standardizing features so mean = 0 and variance = 1
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("[INFO] Feature scaling (StandardScaler) applied successfully.")
    
    # 4. Model Training: Applying K-Nearest Neighbors (KNN)
    # Using K=3 as our optimal tuning parameter
    print("[INFO] Training K-Nearest Neighbors (KNN) classifier...")
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train_scaled, y_train)
    
    # 5. Diagnostic Evaluation & Predictions
    y_pred = model.predict(X_test_scaled)
    
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n--- MODEL EVALUATION RESULTS ---")
    print(f"Accuracy Score: {accuracy * 100:.2f}%")
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

if __name__ == "__main__":
    run_classification_pipeline()