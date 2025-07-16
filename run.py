#!/usr/bin/env python3
"""
Simple startup script for Render deployment
"""
import os
import sys

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set environment variables
os.environ.setdefault('PORT', '8000')

# Import and run the app
if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv
    
    # Load environment variables
    load_dotenv()
    
    # Import app
    from app.main import app
    
    # Get port from environment
    port = int(os.environ.get('PORT', 8000))
    
    print(f"Starting server on port {port}")
    
    # Run the application
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
