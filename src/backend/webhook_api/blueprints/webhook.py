"""
Webhook Blueprint
---
Handles TradingView webhook alerts.
"""
import uuid
import time
from flask import Blueprint, request, jsonify, current_app
from loguru import logger

from ..schema.tradingview_alert import validate_tradingview_alert
from ..models.trade_classifier import TradeClassifier
from ..models.order_calculator import OrderCalculator
from ..adapters.alpaca_adapter import AlpacaAdapter


bp = Blueprint('webhook', __name__, url_prefix='/webhook')


@bp.route('', methods=['POST'])
def receive_tradingview_alert():
    """
    Receive and process a TradingView webhook alert.
    
    Returns:
        JSON response with order processing details
    """
    try:
        # Get the JSON payload
        payload = request.json
        if not payload:
            return jsonify({
                "success": False,
                "error": {
                    "code": "INVALID_PAYLOAD",
                    "message": "No JSON payload provided"
                }
            }), 400
            
        # Validate the TradingView alert format
        validated_data = validate_tradingview_alert(payload)
        
        # Classify the trade (asset class, trade type)
        classified_data = TradeClassifier.classify_trade(validated_data)
        
        # Generate a client order ID for tracking
        client_order_id = f"tv-{int(time.time())}-{str(uuid.uuid4())[:8]}"
        
        # Initialize Alpaca adapter and connect
        adapter = AlpacaAdapter()
        connected = adapter.connect()
        
        if not connected:
            return jsonify({
                "success": False,
                "error": {
                    "code": "BROKER_CONNECTION_FAILED",
                    "message": "Failed to connect to broker"
                }
            }), 500
            
        # Get account information for order sizing
        account_info = adapter.get_account_info()
        
        # Calculate order size based on configuration
        # For now, we'll use the TradingView contracts value directly
        symbol = classified_data.get("symbol")
        side = classified_data.get("strategy_order_action", "").lower()
        
        # Use order calculator to determine size
        quantity = OrderCalculator.calculate_from_tradingview(
            classified_data,
            account_info,
            sizing_preference="tradingview"  # This would come from configuration
        )
        
        # Apply broker/asset constraints
        broker_constraints = {
            "min_order_size": {
                "crypto": 0.001,
                "equity": 1.0,
                "forex": 0.01
            },
            "lot_size": {
                "crypto": 0.001,
                "equity": 1.0,
                "forex": 0.01
            }
        }
        
        quantity = OrderCalculator.apply_asset_constraints(
            quantity,
            classified_data,
            broker_constraints
        )
        
        # Place the order
        result = adapter.place_market_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
            client_order_id=client_order_id
        )
        
        # Return success response
        return jsonify({
            "success": True,
            "data": {
                "received": True,
                "order_id": result.get("id", "unknown"),
                "client_order_id": client_order_id,
                "symbol": symbol,
                "order_type": "market",
                "side": side,
                "quantity": quantity,
                "timestamp": int(time.time() * 1000)
            }
        })
        
    except ValueError as e:
        logger.error(f"Validation error processing webhook: {str(e)}")
        return jsonify({
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": str(e)
            }
        }), 400
        
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        return jsonify({
            "success": False,
            "error": {
                "code": "SERVER_ERROR",
                "message": "An error occurred processing the webhook"
            }
        }), 500 