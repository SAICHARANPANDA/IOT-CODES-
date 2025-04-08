import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
data = pd.read_csv("soil_data.csv")
X = data[['soil_moisture', 'temperature']]
y = data['irrigation_needed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, 'irrigation_model.pkl')
print("✅ Model trained and saved as 'irrigation_model.pkl'.")