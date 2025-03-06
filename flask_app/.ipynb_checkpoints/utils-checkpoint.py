# utils.py (Helper Functions)
import pickle
import numpy as np

def load_model():
    """
    Loads the trained model from file.
    """
    with open("models/model.pkl", "rb") as file:  
        model = pickle.load(file)  # Hint: Use pickle to load the model
    return model

def model_predict(features):
    """
    Predicts using the loaded model.
    """
    model = load_model()  # Hint: Load the model before predicting
    prediction =  model.predict([email])# Hint: Use the correct method to make predictions
    # If the email is spam, prediction should be 1, otherwise -1
    #prediction =
    #return prediction 
    return 1 if prediction[0] == 1 else -1