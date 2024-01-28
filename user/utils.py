import firebase_admin
from firebase_admin import credentials

from decouple import config


def create_firebase_token(user):
    # Check if a Firebase service account key file path is defined
    # This should be the path to your Firebase Admin SDK service account JSON file
    firebase_key_path = config("FIREBASE_JSON_KEY")

    # Initialize the Firebase Admin SDK with the service account credentials
    cred = credentials.Certificate(firebase_key_path)
    firebase_admin.initialize_app(cred)

    # Create a custom token using the Firebase Admin SDK
    # 'user.uid' should correspond to a unique identifier for the user
    custom_token = firebase_admin.auth.create_custom_token(user.uid)

    # Return the custom token
    return custom_token
