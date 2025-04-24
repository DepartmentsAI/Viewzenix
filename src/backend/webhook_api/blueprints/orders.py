"""
Orders Blueprint
---
Provides endpoints for retrieving and managing orders.
"""
from flask import Blueprint, jsonify, request
from loguru import logger

from ..adapters.alpaca_adapter import AlpacaAdapter


bp = Blueprint('orders', __name__, url_prefix='/orders')


@bp.route('', methods=['GET'])
def get_orders():
    """
    Get the list of recent orders.
    
    Query parameters:
    - limit: Maximum number of orders to return (default: 50)
    - offset: Number of orders to skip (default: 0)
    - status: Filter by order status (open, filled, canceled)
    
    Returns:
        JSON list of orders
    """
    try:
        # Parse query parameters
        limit = int(request.args.get('limit', 50))
        offset = int(request.args.get('offset', 0))
        status = request.args.get('status')
        
        # Validate parameters
        if limit < 1 or limit > 100:
            limit = 50
        
        if offset < 0:
            offset = 0
            
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
            
        # Get all orders from the broker
        orders = adapter.get_orders()
        
        # Filter by status if provided
        if status:
            orders = [order for order in orders if order.get('status', '').lower() == status.lower()]
            
        # Calculate total for pagination
        total = len(orders)
        
        # Apply pagination
        paginated_orders = orders[offset:offset+limit]
        
        # Return formatted response
        return jsonify({
            "success": True,
            "data": paginated_orders,
            "meta": {
                "pagination": {
                    "total": total,
                    "limit": limit,
                    "offset": offset
                }
            }
        })
        
    except Exception as e:
        logger.error(f"Error retrieving orders: {str(e)}")
        return jsonify({
            "success": False,
            "error": {
                "code": "SERVER_ERROR",
                "message": f"Error retrieving orders: {str(e)}"
            }
        }), 500


@bp.route('/<order_id>', methods=['GET'])
def get_order(order_id):
    """
    Get details for a specific order.
    
    Args:
        order_id: Broker order ID
        
    Returns:
        JSON order details
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
            
        # Get the order details
        order = adapter.get_order(order_id)
        
        # Return the order
        return jsonify({
            "success": True,
            "data": order
        })
        
    except Exception as e:
        logger.error(f"Error retrieving order {order_id}: {str(e)}")
        return jsonify({
            "success": False,
            "error": {
                "code": "SERVER_ERROR",
                "message": f"Error retrieving order: {str(e)}"
            }
        }), 500


@bp.route('/<order_id>', methods=['DELETE'])
def cancel_order(order_id):
    """
    Cancel a specific order.
    
    Args:
        order_id: Broker order ID
        
    Returns:
        JSON confirmation of cancellation
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
            
        # Cancel the order
        result = adapter.cancel_order(order_id)
        
        # Return confirmation
        return jsonify({
            "success": True,
            "data": {
                "order_id": order_id,
                "canceled": True,
                "message": "Order successfully canceled"
            }
        })
        
    except Exception as e:
        logger.error(f"Error canceling order {order_id}: {str(e)}")
        return jsonify({
            "success": False,
            "error": {
                "code": "SERVER_ERROR",
                "message": f"Error canceling order: {str(e)}"
            }
        }), 500 