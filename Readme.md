Overview
The rapid expansion of the Internet of Things (IoT) has revolutionized connectivity but also introduced substantial cybersecurity risks. Traditional security measures struggle against sophisticated cyberattacks in IoT environments. This project presents a robust Network Intrusion Detection System (NIDS) tailored for IoT networks, leveraging Machine Learning (ML) and Deep Learning (DL) techniques to identify and mitigate threats in real-time.
Objectives
•	Develop a real-time intrusion detection system for IoT networks.
•	Classify network traffic as either "Normal" or "Attack".
•	Implement both ML and DL models for effective detection.
•	Deploy the solution as a RESTful API using Flask for real-time detection.
Dataset
The project utilizes the UNSW-NB15 dataset, which contains modern network traffic patterns, including both legitimate and malicious activities:
•	Training Set: 175,341 records
•	Testing Set: 82,332 records
•	Features: 44 features (40 numerical, 4 categorical)
The dataset includes attack types like Fuzzers, Analysis, Backdoors, DoS, Exploits, Generic, Reconnaissance, Shellcode, and Worms.
Architecture
The architecture consists of:
1.	Data Preprocessing:
o	Data cleaning, feature selection, and transformation.
o	One-Hot Encoding for categorical features and standardization for numerical features.
2.	Model Development:
o	Machine Learning Models:
	Decision Tree
	Random Forest
o	Deep Learning Models:
	Model 1
	Model2
	Model 3
3.	API Deployment:
o	Deployed using Flask as a RESTful API for real-time traffic analysis.

Model Performance
Model	Accuracy	F1-Score	Recall	Precision
Decision Tree	91.23%	0.90	0.87	0.93
Random Forest	91.67%	0.93	0.97	0.89
Neural Network Model 1	92.65%	0.94	0.95	0.94
Neural Network Model 2	95.24%	0.99	0.98	0.94
Neural Network Model 3	94.72%	0.98	0.94	0.94
Model 2 (Deep Neural Network) emerged as the best performer, achieving 95.24% accuracy on the test set with high precision and recall.
Flask API Deployment
The best-performing models are deployed as a Flask API. The API accepts network traffic data as input and returns predictions in real time.
Example:
curl -X POST "http://127.0.0.1:5000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "features": [15.40279, "tcp", "-", "REQ", 14, 0, 630, 0, 0.844003, 254, 0, 303.841064, 0, 13, 0, 1184.83, 0, 2188.4775, 0, 255, 0, 0, 0, 0, 0, 0, 45, 0, 0, 0, 18, 6, 9, 3, 3, 17, 0, 0, 0, 10, 17, 0]
     }'
Response:

{
  "prediction": 0
}
Future Work
•	Extend to multi-class classification for specific attack types.
•	Deploy on cloud-based platforms for scalability.

How to Run the Project
1.	Clone the repository:
git clone <repo-url>
cd <repo-directory>
2.	Install dependencies:
pip install -r requirements.txt
3.	Run the Flask API:
python app.py
4.	Send POST requests to test:
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"data": <your_data>}'

Author
Shailja Roy - Master of Science in Engineering Technology, San Jose State University, May 2025


