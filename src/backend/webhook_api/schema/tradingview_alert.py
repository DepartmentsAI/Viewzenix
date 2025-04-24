"""
TradingView Alert Schema
---
JSON schema validation for TradingView webhook payloads
"""
from typing import Dict, Any
import jsonschema
from loguru import logger


# Define the TradingView alert JSON schema
TRADINGVIEW_ALERT_SCHEMA = {
    "type": "object",
    "required": [
        "symbol",
        "strategy_order_id",
        "strategy_order_action",
        "strategy_order_contracts",
        "strategy_order_price",
        "time"
    ],
    "properties": {
        "symbol": {
            "type": "string",
            "description": "Trading symbol (e.g., BTCUSD, AAPL, EUR/USD)"
        },
        "strategy_order_id": {
            "type": "string",
            "description": "Identifier for the trade (e.g., 'long', 'short')"
        },
        "strategy_order_action": {
            "type": "string",
            "enum": ["buy", "sell"],
            "description": "Trade direction"
        },
        "strategy_order_contracts": {
            "type": ["number", "string"],
            "description": "Order size (quantity)"
        },
        "strategy_order_price": {
            "type": ["number", "string"],
            "description": "Current price when alert triggered"
        },
        "strategy_order_comment": {
            "type": "string",
            "description": "Optional comment for the trade"
        },
        "time": {
            "type": ["number", "string"],
            "description": "Timestamp in milliseconds"
        }
    },
    "additionalProperties": True
}


def validate_tradingview_alert(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate TradingView alert JSON against schema.
    
    Args:
        payload: JSON payload from TradingView alert
        
    Returns:
        Dict[str, Any]: Validated and potentially sanitized payload
        
    Raises:
        ValueError: If payload doesn't match schema
    """
    try:
        # Ensure strategy_order_contracts is a float
        if "strategy_order_contracts" in payload:
            try:
                payload["strategy_order_contracts"] = float(payload["strategy_order_contracts"])
            except (ValueError, TypeError):
                raise ValueError("strategy_order_contracts must be convertible to a number")
        
        # Ensure strategy_order_price is a float
        if "strategy_order_price" in payload:
            try:
                payload["strategy_order_price"] = float(payload["strategy_order_price"])
            except (ValueError, TypeError):
                raise ValueError("strategy_order_price must be convertible to a number")
        
        # Ensure time is an integer
        if "time" in payload:
            try:
                payload["time"] = int(payload["time"])
            except (ValueError, TypeError):
                raise ValueError("time must be convertible to an integer")
        
        # Validate against the schema
        jsonschema.validate(instance=payload, schema=TRADINGVIEW_ALERT_SCHEMA)
        
        logger.info(f"Validated TradingView alert for {payload['symbol']}")
        return payload
        
    except jsonschema.exceptions.ValidationError as e:
        logger.error(f"TradingView alert validation failed: {str(e)}")
        raise ValueError(f"Invalid TradingView alert format: {str(e)}")
    except Exception as e:
        logger.error(f"Error processing TradingView alert: {str(e)}")
        raise 