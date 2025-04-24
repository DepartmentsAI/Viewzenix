"""
Viewzenix Webhook API Entry Point
---
This module serves as the entry point for the Viewzenix Flask webhook API.
"""
from . import create_app
from loguru import logger

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    logger.info("Starting Viewzenix Webhook API")
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    ) 