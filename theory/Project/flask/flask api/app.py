from flask import Flask, jsonify, request
import pickle  # or use joblib for larger models

# Initialize the Flask application
app = Flask(__name__)

# Load the model from the file
model = None
with open("number_plate_model.pkl", "rb") as file:
    model = pickle.load(file)  # Replace with joblib if needed

@app.route('/')
def home():
    return "Flask app is running!"

# Example route for prediction (adjust based on your model's input/output)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()

        # Assuming the model expects a single feature for prediction
        features = data['features']  # Extract the features from the request
        prediction = model.predict([features])

        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    # Run the Flask app on port 8000
    app.run(debug=True, port=8000)

