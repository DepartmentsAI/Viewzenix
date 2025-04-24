# Viewzenix Webhook API Documentation

This document provides an overview of the Viewzenix Webhook API, which is responsible for receiving TradingView alerts and executing trades through broker adapters.

## API Access

The API is accessible at the base URL `http://localhost:5000` when running locally.

Interactive API documentation is available at: `http://localhost:5000/api/docs`

## Authentication

Authentication is handled via API keys. Include the API key in the `X-API-KEY` header for requests that require authentication.

## Endpoints

### TradingView Webhook

#### `POST /webhook`

Receives and processes TradingView alerts.

**Request Body:**
```json
{
  "symbol": "BTCUSD",
  "strategy_order_id": "long",
  "strategy_order_action": "buy",
  "strategy_order_contracts": 0.05,
  "strategy_order_price": 64340.15,
  "strategy_order_comment": "Breakout",
  "time": 1713746400000
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "received": true,
    "order_id": "a1b2c3d4-e5f6-g7h8-i9j0",
    "client_order_id": "tv-1713746400-a1b2c3d4",
    "symbol": "BTCUSD",
    "order_type": "market",
    "side": "buy",
    "quantity": 0.1,
    "timestamp": 1713746480000
  }
}
```

### System Status

#### `GET /status`

Returns the current status of the trading system.

**Response:**
```json
{
  "success": true,
  "data": {
    "status": "active",
    "broker_connected": true,
    "broker_name": "Alpaca",
    "positions_count": 3,
    "open_orders_count": 2,
    "global_sl_tp_active": true,
    "base_equity": 10000.0,
    "current_equity": 10250.75,
    "uptime": "2d 5h 30m",
    "server_time": "2023-05-01T12:30:45.123Z"
  }
}
```

### Orders Management

#### `GET /orders`

Returns a list of orders with pagination.

**Query Parameters:**
- `limit` (optional): Maximum number of orders to return (default: 50)
- `offset` (optional): Number of orders to skip (default: 0)
- `status` (optional): Filter by order status (open, filled, canceled)

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "a1b2c3d4-e5f6-g7h8-i9j0",
      "client_order_id": "tv-1713746400-a1b2c3d4",
      "symbol": "BTCUSD",
      "side": "buy",
      "quantity": 0.1,
      "filled_quantity": 0.1,
      "type": "market",
      "status": "filled",
      "created_at": "2023-05-01T12:30:45.123Z"
    }
  ],
  "meta": {
    "pagination": {
      "total": 125,
      "limit": 50,
      "offset": 0
    }
  }
}
```

#### `GET /orders/{order_id}`

Returns details for a specific order.

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "a1b2c3d4-e5f6-g7h8-i9j0",
    "client_order_id": "tv-1713746400-a1b2c3d4",
    "symbol": "BTCUSD",
    "side": "buy",
    "quantity": 0.1,
    "filled_quantity": 0.1,
    "type": "market",
    "status": "filled",
    "created_at": "2023-05-01T12:30:45.123Z"
  }
}
```

#### `DELETE /orders/{order_id}`

Cancels a specific order.

**Response:**
```json
{
  "success": true,
  "data": {
    "order_id": "a1b2c3d4-e5f6-g7h8-i9j0",
    "canceled": true,
    "message": "Order successfully canceled"
  }
}
```

### Cleanup Operations

#### `POST /cleanup`

Cleans up orphaned stop loss and take profit orders.

**Response:**
```json
{
  "success": true,
  "data": {
    "cleaned_orders": 3,
    "orphaned_sl_orders": 2,
    "orphaned_tp_orders": 1,
    "timestamp": 1713746480000
  }
}
```

### Bot State Management

#### `GET /bot_state/{bot_id}`

Gets the current state and configuration for a trading bot.

**Response:**
```json
{
  "success": true,
  "data": {
    "bot_id": "btc_breakout_bot",
    "active": true,
    "config": {
      "sizing_preference": "percentage",
      "risk_percentage": 1.0,
      "use_stop_loss": true,
      "updated_at": 1713746400000
    },
    "last_updated": 1713746400000
  }
}
```

#### `PUT /bot_state/{bot_id}`

Updates the state and configuration for a trading bot.

**Request Body:**
```json
{
  "active": true,
  "config": {
    "sizing_preference": "percentage",
    "risk_percentage": 1.0,
    "use_stop_loss": true
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "bot_id": "btc_breakout_bot",
    "active": true,
    "updated_at": 1713746480000,
    "config_applied": true
  }
}
```

## Error Responses

All endpoints return errors in the following format:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Error message describing the issue"
  }
}
```

Common error codes:
- `VALIDATION_ERROR`: Invalid input data
- `NOT_FOUND`: Requested resource not found
- `BROKER_CONNECTION_FAILED`: Failed to connect to broker
- `SERVER_ERROR`: Internal server error

## Webhook Integration with TradingView

To set up TradingView alerts:

1. Create a new alert in TradingView
2. Set the alert message to use this format:
   ```
   {
     "symbol": "{{ticker}}",
     "strategy_order_id": "long",
     "strategy_order_action": "{{strategy.order.action}}",
     "strategy_order_contracts": {{strategy.order.contracts}},
     "strategy_order_price": {{close}},
     "strategy_order_comment": "{{strategy.order.comment}}",
     "time": {{timenow}}
   }
   ```
3. Set the webhook URL to your Viewzenix webhook endpoint
4. Save the alert 