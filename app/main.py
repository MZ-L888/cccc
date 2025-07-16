import os
import uvicorn
from dotenv import load_dotenv

# Load .env file to environment variables before importing app config
load_dotenv()

from app.core.application import create_app
from app.log.logger import get_main_logger

app = create_app()

if __name__ == "__main__":
    logger = get_main_logger()
    # Support Render's PORT environment variable
    port = int(os.getenv("PORT", 8000))
    logger.info(f"Starting application server on port {port}...")
    uvicorn.run(app, host="0.0.0.0", port=port)
