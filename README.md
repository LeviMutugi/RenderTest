# USSD API Service

A FastAPI-based USSD (Unstructured Supplementary Service Data) service for mobile banking and telecommunications.

## Features

- RESTful USSD endpoint for mobile service providers
- Health check endpoint for monitoring
- Comprehensive error handling and logging
- CORS support for web integration
- Production-ready configuration

## API Endpoints

### Health Check
```
GET /health
```
Returns service health status.

### USSD Endpoint
```
POST /ussd
```
Handles USSD requests with the following form parameters:
- `sessionId` (required): Unique session identifier
- `serviceCode` (required): USSD service code
- `phoneNumber` (required): User's phone number
- `text` (optional): User input text

## USSD Menu Flow

1. **Main Menu**: Welcome message with options
   - 1: Check Balance
   - 2: Services
   - 3: Help

2. **Services Submenu**: 
   - 1: Construction
   - 2: Consultancy
   - 0: Back to main menu

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
uvicorn app.main:app --reload
```

3. Access the API at `http://localhost:8000`

## Deployment on Render

This application is configured for deployment on Render:

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Set the following configuration:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `./start.sh`
   - **Environment**: Python 3.9+

## Environment Variables

The application uses the following environment variables:
- `PORT`: Port number (automatically set by Render)

## Testing

Test the USSD endpoint with curl:

```bash
curl -X POST "https://your-app.onrender.com/ussd" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "sessionId=12345&serviceCode=*123#&phoneNumber=+254700000000&text="
```

## Project Structure

```
pyussd/
├── app/
│   ├── main.py          # FastAPI application
│   └── ussdapp.py       # USSD logic
├── requirements.txt      # Python dependencies
├── start.sh            # Startup script for Render
└── README.md           # This file
```

## License

MIT License 