#!/usr/bin/env python3
import os
import sys

# Ensure we can import our app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # Get port from environment
    port = int(os.environ.get('PORT', 8000))

    print(f"Starting Gemini Balance on port {port}")

    # Import and run
    import uvicorn
    from dotenv import load_dotenv
    load_dotenv()
    from app.main import app

    uvicorn.run(app, host="0.0.0.0", port=port)
