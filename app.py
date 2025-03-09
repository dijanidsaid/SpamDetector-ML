# app.py
from flask import Flask, request, render_template, jsonify
#from utils import model_predict  # Import the predict function from utils.py
# utils.py (Helper Functions)
import pickle

def load_model():
    """
    Loads the trained model from file.
    """
    with open("/model.pkl", "rb") as file:  
        model = pickle.load(file)  # Load the model using pickle
    return model

def model_predict(features):
    """
    Predicts using the loaded model.
    Args:
        features (str): The email text to classify.
    Returns:
        int: 1 if the email is spam, -1 if it is not spam.
    """
    model = load_model()  # Load the model
    prediction = model.predict([features])  # Make a prediction
    return 1 if prediction[0] == 1 else -1  # Return 1 (spam) or -1 (not spam)

# Initialize Flask app
app = Flask(__name__, template_folder='.')

@app.route("/")
def home():
    """
    Renders the home page with the form.
    """
    return render_template("index.html")  # Load the index.html template

@app.route('/predict', methods=['POST'])  # Handle POST requests

def predict_route():
    """
    Handles form submission and returns prediction.
    """
    email = request.form.get('email')  # Get email from form data
    
    if not email:  # If email is empty
        return render_template("index.html", error="Please enter an email.")  # Show error

    prediction = model_predict(email)  # Make a prediction
    result = "Spam" if prediction == 1 else "Not Spam"  # Convert prediction to text
    return render_template("index.html", email=email, result=result)  # Return result to template
   

# Create an API endpoint
@app.route('/api/predict', methods=['POST'])  # Handle POST requests

def predict_api():
    """
    API endpoint that accepts a JSON payload and returns a prediction.
    """
    try:
        data = request.get_json()  # Extract JSON data
        email = data.get('email')  # Get email from JSON
        
        if not email:  # If email is empty
            return jsonify({'error': 'Email is required.'}), 400  # Return error response

        prediction = model_predict(email)  # Make a prediction
        result = "Spam" if prediction == 1 else "Not Spam"  # Convert prediction to text
        return jsonify({'email': email, 'result': result})  # Return JSON response

    except Exception as e:  # Catch any exceptions
        return jsonify({'error': str(e)}), 400  # Return error response 

# Run the Flask app
import os
if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000, debug=True)  # Run on all available IPs, port 5000
    port = int(os.environ.get("PORT", 5000))  # Get PORT from environment
    app.run(host="0.0.0.0", port=port, debug=True)