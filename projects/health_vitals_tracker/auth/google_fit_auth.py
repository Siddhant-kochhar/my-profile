import os
from fastapi import Request, HTTPException
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request as GoogleRequest
from dotenv import load_dotenv
import json

load_dotenv()

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Enable HTTP for localhost

CLIENT_SECRET_FILE = os.getenv("GOOGLE_CLIENT_SECRET_FILE", "credentials/client_secret_150422301585-hdble1j688395bgeogjub4idgie57sap.apps.googleusercontent.com.json")
SCOPES = [
    "https://www.googleapis.com/auth/fitness.activity.read",
    "https://www.googleapis.com/auth/fitness.body.read",
    "https://www.googleapis.com/auth/fitness.heart_rate.read",
    "https://www.googleapis.com/auth/fitness.sleep.read"
]
REDIRECT_URI = "http://localhost:8000/oauth2callback"

def get_google_fit_flow():
    """Create and return a Google OAuth flow for Google Fit API"""
    try:
        if not os.path.exists(CLIENT_SECRET_FILE):
            raise FileNotFoundError(f"Client secret file not found: {CLIENT_SECRET_FILE}")
        
        return Flow.from_client_secrets_file(
            CLIENT_SECRET_FILE,
            scopes=SCOPES,
            redirect_uri=REDIRECT_URI
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create OAuth flow: {str(e)}")

def refresh_credentials(credentials: Credentials):
    """Refresh expired credentials"""
    try:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(GoogleRequest())
        return credentials
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Failed to refresh credentials: {str(e)}")

def get_credentials_from_token(token_info: dict):
    """Create credentials object from token info"""
    try:
        return Credentials(
            token=token_info.get('access_token'),
            refresh_token=token_info.get('refresh_token'),
            token_uri="https://oauth2.googleapis.com/token",
            client_id=token_info.get('client_id'),
            client_secret=token_info.get('client_secret'),
            scopes=SCOPES
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to create credentials: {str(e)}")
