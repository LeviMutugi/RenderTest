# app/ussd_logic.py
import logging

logger = logging.getLogger(__name__)

def handle_ussd(session_id, phone_number, text):
    """Handle USSD menu logic"""
    try:
        logger.info(f"Processing USSD: session={session_id}, phone={phone_number}, text='{text}'")
        
        # Main menu
        if text == "":
            return "CON Welcome to PW USSD Service.\n1. Check Balance\n2. Services\n3. Help"
        
        # Check balance
        elif text == "1":
            return "END Your balance is KES 2,000"
        
        # Services submenu
        elif text == "2":
            return "CON Select a service:\n1. Construction\n2. Consultancy\n0. Back"
        
        # Construction service
        elif text == "2*1":
            return "END Construction details will be sent to you shortly."
        
        # Consultancy service
        elif text == "2*2":
            return "END Consultancy details will be sent to you shortly."
        
        # Back to main menu
        elif text == "2*0":
            return "CON Welcome to PW USSD Service.\n1. Check Balance\n2. Services\n3. Help"
        
        # Help
        elif text == "3":
            return "END For support, call +254700000000 or email support@pw.com"
        
        # Invalid input
        else:
            return "END Invalid input. Please try again."
            
    except Exception as e:
        logger.error(f"Error in USSD logic: {str(e)}")
        return "END An error occurred. Please try again."
