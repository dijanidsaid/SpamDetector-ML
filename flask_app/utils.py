# utils.py (Helper Functions)
import pickle

def load_model():
    """
    Loads the trained model from file.
    """
    with open("models/model.pkl", "rb") as file:  
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