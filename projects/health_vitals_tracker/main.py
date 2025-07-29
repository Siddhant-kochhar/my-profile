from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv
from auth.google_fit_auth import get_google_fit_flow

load_dotenv()

app = FastAPI(title="Health Vitals Tracker", description="A FastAPI application for tracking health vitals using Google Fit")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Health Alert System is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "health_vitals_tracker"}

from fastapi.responses import RedirectResponse

@app.get("/login")
def login():
    flow = get_google_fit_flow()
    auth_url, _ = flow.authorization_url(
        prompt='consent',
        include_granted_scopes='true',
        access_type='offline'   # To get refresh token as well
    )
    return RedirectResponse(auth_url)


@app.get("/oauth2callback")
def oauth2callback(code: str, state: str = None):
    """Handle OAuth callback from Google"""
    try:
        flow = get_google_fit_flow()
        flow.fetch_token(code=code)
        
        # Get credentials
        credentials = flow.credentials
        
        # Here you would typically store the credentials securely
        # and use them to fetch health data from Google Fit
        
        return {"message": "OAuth successful", "access_token": credentials.token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"OAuth callback failed: {str(e)}")

@app.get("/health-vitals")
def get_health_vitals():
    """Get health vitals data (placeholder)"""
    return {
        "heart_rate": 75,
        "steps": 8500,
        "calories": 2100,
        "sleep_hours": 7.5,
        "timestamp": "2024-01-15T10:30:00Z"
    }

@app.get("/favicon.ico")
def favicon():
    """Handle favicon requests"""
    return {"message": "No favicon configured"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
