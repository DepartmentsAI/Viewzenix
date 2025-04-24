"""
Status Blueprint
---
Provides endpoints for checking the health and status of the trading system.
"""
import time
import os
from datetime import datetime
from flask import Blueprint, jsonify
from loguru import logger

from ..adapters.alpaca_adapter import AlpacaAdapter


bp = Blueprint('status', __name__, url_prefix='/status')

# Store start time for uptime calculation
START_TIME = time.time()


@bp.route('', methods=['GET'])
def get_status():
    """
    Get the current status of the trading system.
    
    Returns:
        JSON with system status information
    """
    try:
        # Initialize the broker adapter and check connection
        adapter = AlpacaAdapter()
        broker_connected = adapter.connect()
        
        # Calculate uptime
        uptime_seconds = time.time() - START_TIME
        days = int(uptime_seconds // 86400)
        hours = int((uptime_seconds % 86400) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        uptime_str = f"{days}d {hours}h {minutes}m"
        
        # Get account information if connected
        account_info = {}
        positions_count = 0
        open_orders_count = 0
        
        if broker_connected:
            try:
                account_info = adapter.get_account_info()
                positions = adapter.get_positions()
                positions_count = len(positions)
                
                orders = adapter.get_orders()
                open_orders_count = len(orders)
            except Exception as e:
                logger.error(f"Error getting additional status info: {str(e)}")
                broker_connected = False
        
        # Determine if global stop loss / take profit is active (placeholder)
        # This would be based on configuration and state management
        global_sl_tp_active = True
        
        # Get equity information
        base_equity = float(os.environ.get('BASE_EQUITY', '10000.0'))  # Default placeholder
        current_equity = float(account_info.get('equity', '0.0'))
        
        # Return the status information
        return jsonify({
            "success": True,
            "data": {
                "status": "active" if broker_connected else "degraded",
                "broker_connected": broker_connected,
                "broker_name": "Alpaca",
                "positions_count": positions_count,
                "open_orders_count": open_orders_count, 
                "global_sl_tp_active": global_sl_tp_active,
                "base_equity": base_equity,
                "current_equity": current_equity,
                "uptime": uptime_str,
                "server_time": datetime.utcnow().isoformat()
            }
        })
        
    except Exception as e:
        logger.error(f"Error getting system status: {str(e)}")
        return jsonify({
            "success": False,
            "error": {
                "code": "SERVER_ERROR",
                "message": "Error retrieving system status"
            }
        }), 500 