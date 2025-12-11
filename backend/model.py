import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load data
df = pd.read_csv("cleaned_data.csv")

# Use only 3 features
features = ["alcohol", "density", "pH"]

X = df[features]
y = df["quality"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
with open("wine_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained with 3 features and saved!")
