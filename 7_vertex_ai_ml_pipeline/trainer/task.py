import os
import joblib
import pandas as pd
from feast import FeatureStore
from google.cloud import storage
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import json
import numpy as np

def main():
    # === Step 1: Init Feast Feature Store ===
    store = FeatureStore(repo_path="my_feature_repo")

    # === Step 2: Get training data from Feature Store ===
    # Define the user-entity DataFrame
    user_ids = pd.DataFrame({
        "user_id": list(range(1, 51)),  # or however many you have
        "event_timestamp": pd.to_datetime("now")
    })

    training_df = store.get_historical_features(
        entity_df=user_ids,
        features=[
            "user_features:avg_rating",
            "user_features:num_ratings"
        ],
    ).to_df()

    print("✅ Retrieved features from Feature Store")
    print(training_df.head())

    # === Step 3: Train a model ===
    X = training_df[["avg_rating", "num_ratings"]]
    y = training_df["avg_rating"]  # For demonstration — replace with actual label if different

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # === Step 4: Evaluate model ===
    y_pred = model.predict(X)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    print(f"✅ Model RMSE: {rmse:.4f}")

    # === Step 5: Save model ===
    output_dir = os.environ.get("AIP_MODEL_DIR", "/tmp/model")
    os.makedirs(output_dir, exist_ok=True)
    joblib.dump(model, os.path.join(output_dir, "model.joblib"))
    print(f"✅ Model saved to {output_dir}/model.joblib")

    # === Step 6: Log evaluation metrics ===
    metrics_path = os.path.join(output_dir, "metrics.json")
    with open(metrics_path, "w") as f:
        json.dump({"rmse": float(rmse)}, f)

    print(f"✅ Metrics saved to {metrics_path}")

if __name__ == "__main__":
    main()
