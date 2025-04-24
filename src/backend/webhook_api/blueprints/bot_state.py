"""
Bot State Blueprint
---
Provides endpoints for managing trading bot configurations and states.
"""
import time
import json
import os
from flask import Blueprint, jsonify, request
from loguru import logger


bp = Blueprint('bot_state', __name__, url_prefix='/bot_state')

# Default config directory
CONFIG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config')
os.makedirs(CONFIG_DIR, exist_ok=True)


def get_bot_config(bot_id):
    """
    Get configuration for a specific bot.
    
    Args:
        bot_id: Bot identifier
        
    Returns:
        dict: Bot configuration or empty dict if not found
    """
    config_path = os.path.join(CONFIG_DIR, f"{bot_id}.json")
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error reading bot config {bot_id}: {str(e)}")
            return {}
    
    return {}


def save_bot_config(bot_id, config):
    """
    Save configuration for a specific bot.
    
    Args:
        bot_id: Bot identifier
        config: Bot configuration dict
        
    Returns:
        bool: True if saved successfully, False otherwise
    """
    config_path = os.path.join(CONFIG_DIR, f"{bot_id}.json")
    
    try:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        return True
    except Exception as e:
        logger.error(f"Error saving bot config {bot_id}: {str(e)}")
        return False


@bp.route('/<bot_id>', methods=['GET'])
def get_bot_state(bot_id):
    """
    Get the current state and configuration for a trading bot.
    
    Args:
        bot_id: Bot identifier
        
    Returns:
        JSON with bot state and configuration
    """
    try:
        # Get bot configuration
        config = get_bot_config(bot_id)
        
        if not config:
            return jsonify({
                "success": False,
                "error": {
                    "code": "BOT_NOT_FOUND",
                    "message": f"Bot {bot_id} not found or has no configuration"
                }
            }), 404
            
        # Return bot state and configuration
        return jsonify({
            "success": True,
            "data": {
                "bot_id": bot_id,
                "active": config.get("active", False),
                "config": config,
                "last_updated": config.get("updated_at")
            }
        })
        
    except Exception as e:
        logger.error(f"Error retrieving bot state for {bot_id}: {str(e)}")
        return jsonify({
            "success": False,
            "error": {
                "code": "SERVER_ERROR",
                "message": f"Error retrieving bot state: {str(e)}"
            }
        }), 500


@bp.route('/<bot_id>', methods=['PUT'])
def update_bot_state(bot_id):
    """
    Update the state and configuration for a trading bot.
    
    Args:
        bot_id: Bot identifier
        
    Returns:
        JSON confirmation of the update
    """
    try:
        # Get request data
        data = request.json
        
        if not data:
            return jsonify({
                "success": False,
                "error": {
                    "code": "INVALID_PAYLOAD",
                    "message": "No JSON payload provided"
                }
            }), 400
            
        # Get current config or initialize new one
        config = get_bot_config(bot_id) or {}
        
        # Update active state if provided
        if "active" in data:
            config["active"] = bool(data["active"])
            
        # Update configuration if provided
        if "config" in data:
            for key, value in data["config"].items():
                config[key] = value
                
        # Add timestamp
        config["updated_at"] = int(time.time() * 1000)
        
        # Save the configuration
        if save_bot_config(bot_id, config):
            return jsonify({
                "success": True,
                "data": {
                    "bot_id": bot_id,
                    "active": config.get("active", False),
                    "updated_at": config["updated_at"],
                    "config_applied": True
                }
            })
        else:
            return jsonify({
                "success": False,
                "error": {
                    "code": "CONFIG_SAVE_FAILED",
                    "message": "Failed to save bot configuration"
                }
            }), 500
            
    except Exception as e:
        logger.error(f"Error updating bot state for {bot_id}: {str(e)}")
        return jsonify({
            "success": False,
            "error": {
                "code": "SERVER_ERROR",
                "message": f"Error updating bot state: {str(e)}"
            }
        }), 500 