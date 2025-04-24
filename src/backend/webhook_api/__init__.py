"""
Viewzenix Flask Webhook API
---
This module initializes the Flask application for the Viewzenix trading webhook platform.
"""
import os
from flask import Flask
from flask_cors import CORS
from loguru import logger
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app(test_config=None):
    """
    Create and configure the Flask application instance
    
    Args:
        test_config: Configuration to use for testing
        
    Returns:
        A configured Flask application
    """
    # Create Flask app
    app = Flask(__name__, instance_relative_config=True)
    
    # Configure app
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        # Future database config would go here
    )
    
    # Enable CORS with origins specified in environment variables
    origins = os.environ.get('CORS_ORIGINS', '*').split(',')
    CORS(app, resources={r"/*": {"origins": origins}})
    
    # Configure logging
    logger.add(
        os.path.join("logs", "webhook_api_{time}.log"),
        rotation="1 day",
        retention="30 days",
        level="INFO",
        format="{time} {level} {message}",
        serialize=True
    )
    app.logger = logger
    
    # Register blueprints
    from .blueprints import webhook, orders, status, cleanup, bot_state
    app.register_blueprint(webhook.bp)
    app.register_blueprint(orders.bp)
    app.register_blueprint(status.bp)
    app.register_blueprint(cleanup.bp)
    app.register_blueprint(bot_state.bp)
    
    # Simple index route
    @app.route('/')
    def index():
        return {
            "status": "running",
            "name": "Viewzenix Webhook API",
            "version": "0.1.0"
        }
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Route not found"}, 404
    
    @app.errorhandler(500)
    def server_error(error):
        logger.error(f"Server error: {error}")
        return {"error": "Server error"}, 500
    
    return app 