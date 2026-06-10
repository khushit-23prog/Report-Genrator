import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# ==========================================
# STEP 1: CREATE DATASET
# ==========================================

data = {
    "message": [
        "Congratulations! You won a free iPhone",
        "Claim your prize now",
        "Win cash today",
        "Exclusive offer just for you",
        "Free lottery ticket available",
        "Get free recharge now",
        "Earn money from home",
        "Limited time offer",
        "You have won 10000 rupees",
        "Click here to claim reward",

        "Meeting at 10 AM tomorrow",
        "Please submit your assignment",
        "Let's go for lunch today",
        "Project deadline is next week",
        "Call me when you arrive",
        "Happy Birthday! Have a nice day",
        "Class starts at 9 AM",
        "How are you today?",
        "Please check your email",
        "Let's meet this evening"
    ],

    "label": [
        "spam","spam","spam","spam","spam",
        "spam","spam","spam","spam","spam",

        "ham","ham","ham","ham","ham",
        "ham","ham","ham","ham","ham"
    ]
}

df = pd.DataFrame(data)

print("=" * 50)
print("DATASET PREVIEW")
print("=" * 50)
print(df.head())

# ==========================================
# STEP 2: DATA PREPROCESSING
# ==========================================

df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})

print("\nLabel Mapping Completed")
print(df.head())

# ==========================================
# STEP 3: FEATURES AND TARGET
# ==========================================

X = df["message"]
y = df["label"]

# ==========================================
# STEP 4: TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ==========================================
# STEP 5: TEXT VECTORIZATION
# ==========================================

vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print("\nText Vectorization Completed")

# ==========================================
# STEP 6: MODEL TRAINING
# ==========================================

model = MultinomialNB()

model.fit(X_train, y_train)

print("Model Training Completed")

# ==========================================
# STEP 7: PREDICTIONS
# ==========================================

y_pred = model.predict(X_test)

# ==========================================
# STEP 8: MODEL EVALUATION
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 50)
print("MODEL PERFORMANCE")
print("=" * 50)

print(f"Accuracy : {accuracy * 100:.2f}%")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ==========================================
# STEP 9: CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

# ==========================================
# STEP 10: USER PREDICTION SYSTEM
# ==========================================

print("\n" + "=" * 50)
print("SPAM DETECTION SYSTEM READY")
print("Type 'exit' to stop")
print("=" * 50)

while True:

    user_message = input("\nEnter Message: ")

    if user_message.lower() == "exit":
        print("Program Closed")
        break

    transformed_message = vectorizer.transform(
        [user_message]
    )

    prediction = model.predict(
        transformed_message
    )

    if prediction[0] == 1:
        print("Result : SPAM EMAIL")
    else:
        print("Result : NOT SPAM")