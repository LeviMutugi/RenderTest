# app/main.py

import logging
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from app.ussdapp import handle_ussd

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="USSD API",
    description="A USSD service API for mobile banking",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Health check endpoint for Render"""
    return {"status": "healthy", "service": "ussd-api"}

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "USSD API is running", "endpoints": ["/health", "/ussd"]}

@app.post("/ussd", response_class=PlainTextResponse)
async def ussd(
    sessionId: str = Form(...),
    serviceCode: str = Form(...),
    phoneNumber: str = Form(...),
    text: str = Form("")
):
    """Handle USSD requests"""
    try:
        logger.info(f"USSD request: sessionId={sessionId}, phoneNumber={phoneNumber}, text={text}")
        
        # Validate required parameters
        if not sessionId or not phoneNumber:
            raise HTTPException(status_code=400, detail="Missing required parameters")
        
        response = handle_ussd(sessionId, phoneNumber, text)
        logger.info(f"USSD response: {response}")
        return response
        
    except Exception as e:
        logger.error(f"Error processing USSD request: {str(e)}")
        return "END An error occurred. Please try again later."
