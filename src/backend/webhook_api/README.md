# Viewzenix Webhook API

This directory contains the Flask-based webhook API for the Viewzenix trading platform, which serves as the core entry point for TradingView alerts.

## Project Structure

```
webhook_api/
├── __init__.py          # Flask application factory
├── app.py               # Application entry point
├── requirements.txt     # Python dependencies
├── adapters/            # Broker adapters
│   ├── __init__.py
│   ├── base_adapter.py  # Base adapter interface
│   └── alpaca_adapter.py # Alpaca implementation
├── blueprints/          # API route definitions
│   ├── __init__.py
│   ├── webhook.py       # TradingView webhook endpoint
│   ├── orders.py        # Order management endpoints
│   ├── status.py        # System status endpoint
│   ├── cleanup.py       # Orphaned order cleanup endpoint
│   └── bot_state.py     # Bot configuration endpoints
├── models/              # Business logic models
│   ├── trade_classifier.py # Asset and trade type classification
│   └── order_calculator.py # Order size calculation
├── schema/              # Input validation schemas
│   └── tradingview_alert.py # TradingView alert schema
├── swagger/             # API documentation
│   ├── __init__.py
│   └── spec.py          # OpenAPI specification
├── utils/               # Utility functions
└── tests/               # Test directory
    └── test_webhook.py  # API tests
```

## Getting Started

### Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory with the following variables:
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
CORS_ORIGINS=*

# Alpaca API credentials (paper trading)
ALPACA_API_KEY=your_alpaca_key
ALPACA_API_SECRET=your_alpaca_secret
ALPACA_LIVE_TRADING=false

# Optional configuration
BASE_EQUITY=10000
```

### Running the Application

Start the Flask development server:
```bash
python -m flask run --host=0.0.0.0 --port=5000
```

Or run directly:
```bash
python app.py
```

## API Documentation

The API is documented using OpenAPI/Swagger specification. You can access the API documentation at:

```
http://localhost:5000/api/docs
```

This provides an interactive documentation interface where you can:
- View all available endpoints
- See request/response schemas
- Test API calls directly from the browser

The raw OpenAPI specification is available at:
```
http://localhost:5000/api/swagger.json
```

## API Endpoints

### TradingView Webhook
- **POST /webhook** - Receive and process TradingView alerts

### System Status
- **GET /status** - Get system health and trading status

### Orders
- **GET /orders** - List all orders with pagination
- **GET /orders/{order_id}** - Get specific order details
- **DELETE /orders/{order_id}** - Cancel a specific order

### Cleanup
- **POST /cleanup** - Clean up orphaned stop loss and take profit orders

### Bot State
- **GET /bot_state/{bot_id}** - Get bot configuration
- **PUT /bot_state/{bot_id}** - Update bot configuration

## Testing

Run the tests using pytest:
```bash
pytest
```

## TradingView Alert Format

Webhook alerts from TradingView should use the following JSON format:
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