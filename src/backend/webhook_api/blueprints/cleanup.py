"""
Cleanup Blueprint
---
Provides endpoints for cleaning up orphaned orders.
"""
import time
from flask import Blueprint, jsonify
from loguru import logger

from ..adapters.alpaca_adapter import AlpacaAdapter


bp = Blueprint('cleanup', __name__, url_prefix='/cleanup')


@bp.route('', methods=['POST'])
def cleanup_orphaned_orders():
    """
    Manually trigger the cleanup process for orphaned orders.
    
    This identifies and cancels orphaned stop loss and take profit orders
    that are no longer associated with an active position.
    
    Returns:
        JSON response with cleanup details
    """
    try:
        # Initialize broker adapter
        adapter = AlpacaAdapter()
        
        if not adapter.connect():
            return jsonify({
                "success": False,
                "error": {
                    "code": "BROKER_CONNECTION_FAILED",
                    "message": "Failed to connect to broker"
                }
            }), 500
            
        # Get all open positions
        positions = adapter.get_positions()
        position_symbols = {p['symbol'] for p in positions}
        
        # Get all open orders
        orders = adapter.get_orders()
        
        # Identify orphaned stop loss and take profit orders
        orphaned_sl_orders = []
        orphaned_tp_orders = []
        
        for order in orders:
            symbol = order.get('symbol')
            side = order.get('side', '').lower()
            order_type = order.get('type', '').lower()
            
            # Skip if the symbol has an open position
            if symbol in position_symbols:
                continue
                
            # Identify the order type (SL or TP)
            client_order_id = order.get('client_order_id', '')
            order_id = order.get('id')
            
            if order_type in ('stop', 'stop_limit'):
                orphaned_sl_orders.append(order_id)
                logger.info(f"Identified orphaned stop loss order: {order_id} for {symbol}")
                
            elif order_type == 'limit':
                orphaned_tp_orders.append(order_id)
                logger.info(f"Identified orphaned take profit order: {order_id} for {symbol}")
        
        # Cancel orphaned orders
        canceled_sl_count = 0
        canceled_tp_count = 0
        
        for order_id in orphaned_sl_orders:
            try:
                adapter.cancel_order(order_id)
                canceled_sl_count += 1
                logger.info(f"Canceled orphaned stop loss order: {order_id}")
            except Exception as e:
                logger.error(f"Failed to cancel orphaned SL order {order_id}: {str(e)}")
                
        for order_id in orphaned_tp_orders:
            try:
                adapter.cancel_order(order_id)
                canceled_tp_count += 1
                logger.info(f"Canceled orphaned take profit order: {order_id}")
            except Exception as e:
                logger.error(f"Failed to cancel orphaned TP order {order_id}: {str(e)}")
        
        # Return cleanup results
        return jsonify({
            "success": True,
            "data": {
                "cleaned_orders": canceled_sl_count + canceled_tp_count,
                "orphaned_sl_orders": canceled_sl_count,
                "orphaned_tp_orders": canceled_tp_count,
                "timestamp": int(time.time() * 1000)
            }
        })
        
    except Exception as e:
        logger.error(f"Error during cleanup process: {str(e)}")
        return jsonify({
            "success": False,
            "error": {
                "code": "SERVER_ERROR",
                "message": f"Error during cleanup process: {str(e)}"
            }
        }), 500 