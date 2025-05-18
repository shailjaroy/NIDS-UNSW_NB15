from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the trained model and preprocessing pipeline
#model = joblib.load("random_forest_model.joblib")
model = load_model("mlp_model3.h5")
preprocessor = joblib.load("preprocessing_pipeline.joblib")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON request data
        data = request.get_json()
        
        # Define the feature names
        feature_names = [
            'dur', 'proto', 'service', 'state', 'spkts', 'dpkts', 'sbytes', 'dbytes', 'rate', 'sttl', 'dttl', 'sload', 
            'dload', 'sloss', 'dloss', 'sinpkt', 'dinpkt', 'sjit', 'djit', 'swin', 'stcpb', 'dtcpb', 'dwin', 'tcprtt', 
            'synack', 'ackdat', 'smean', 'dmean', 'trans_depth', 'response_body_len', 'ct_srv_src', 'ct_state_ttl', 
            'ct_dst_ltm', 'ct_src_dport_ltm', 'ct_dst_sport_ltm', 'ct_dst_src_ltm', 'is_ftp_login', 'ct_ftp_cmd', 
            'ct_flw_http_mthd', 'ct_src_ltm', 'ct_srv_dst', 'is_sm_ips_ports'
        ]
        
        # Validate input data
        if len(data['features']) != len(feature_names):
            return jsonify({"error": f"Expected {len(feature_names)} features, got {len(data['features'])}"})
        
        # Ensure the features are in a proper DataFrame format
        input_features = pd.DataFrame([data['features']], columns=feature_names)
        
        # Debug: Print input features
        print("Input Features:", input_features)
        
        # Apply preprocessing
        processed_features = preprocessor.transform(input_features)
        
        # Debug: Print processed features
        print("Processed Features:", processed_features)
        
        # Make prediction
        prediction = model.predict(processed_features)
        
        # Debug: Print raw prediction
        print("Raw Prediction:", prediction)
        
        # Determine predicted class for binary classification
        threshold = 0.5
        predicted_class = 1 if prediction[0] > threshold else 0
        
        # Return prediction as JSON
        return jsonify({"prediction": int(predicted_class)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)