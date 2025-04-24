# Viewzenix API Specifications

This document outlines the RESTful API endpoints for the Viewzenix application.

## API Base URL

- Development: `http://localhost:3001/api/v1`
- Production: [To be determined]
- Trading Webhook: `http://localhost:5000/webhook` (Flask)

## Authentication

Most endpoints require authentication using JSON Web Tokens (JWT).

**Authentication Header Format:**
```
Authorization: Bearer <token>
```

**Token Acquisition:**
- Obtain via the `/auth/login` endpoint
- Refresh via the `/auth/refresh` endpoint

## Standard Response Format

All API responses follow this standard format:

```json
{
  "success": true|false,
  "data": { /* response data */ },
  "error": { 
    "code": "ERROR_CODE",
    "message": "Human-readable error message"
  },
  "meta": { 
    "pagination": { /* pagination info if applicable */ }
  }
}
```

## Error Codes

Common error codes that may be returned:

- `UNAUTHORIZED`: Authentication token missing or invalid
- `FORBIDDEN`: User lacks permission for the requested operation
- `NOT_FOUND`: Requested resource not found
- `VALIDATION_ERROR`: Request data failed validation
- `SERVER_ERROR`: Internal server error

## Endpoints

### Authentication

#### POST /auth/register
Creates a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "name": "John Doe"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "userId": "123e4567-e89b-12d3-a456-426614174000",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

#### POST /auth/login
Authenticates a user and returns a JWT.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "token": "eyJhbG...",
    "refreshToken": "eyJhbG...",
    "expiresIn": 3600
  }
}
```

#### POST /auth/refresh
Refreshes an expired JWT using a refresh token.

**Request Body:**
```json
{
  "refreshToken": "eyJhbG..."
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "token": "eyJhbG...",
    "refreshToken": "eyJhbG...",
    "expiresIn": 3600
  }
}
```

### Users

#### GET /users/profile
Retrieves the authenticated user's profile.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "userId": "123e4567-e89b-12d3-a456-426614174000",
    "email": "user@example.com",
    "name": "John Doe",
    "createdAt": "2023-04-01T12:00:00Z"
  }
}
```

#### PUT /users/profile
Updates the authenticated user's profile.

**Request Body:**
```json
{
  "name": "John Updated Doe",
  "email": "updated@example.com"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "userId": "123e4567-e89b-12d3-a456-426614174000",
    "email": "updated@example.com",
    "name": "John Updated Doe",
    "updatedAt": "2023-04-02T12:00:00Z"
  }
}
```

### Trading Webhook API (Flask)

#### POST /webhook
Receives TradingView webhook alerts and processes trading signals.

**Request Body (from TradingView):**
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

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "received": true,
    "order_id": "alpaca-12345678",
    "symbol": "BTCUSD",
    "order_type": "market",
    "side": "buy",
    "quantity": 0.05,
    "timestamp": 1713746400120
  }
}
```

#### GET /status
Retrieves the current status of the trading system.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "status": "active",
    "broker_connected": true,
    "positions_count": 3,
    "open_orders_count": 5,
    "global_sl_tp_active": true,
    "base_equity": 100000,
    "current_equity": 103500,
    "uptime": "3d 5h 12m"
  }
}
```

#### POST /cleanup
Manually triggers the cleanup process for orphaned orders.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "cleaned_orders": 2,
    "orphaned_sl_orders": 1,
    "orphaned_tp_orders": 1,
    "timestamp": 1713746500000
  }
}
```

#### GET /orders
Retrieves the list of recent orders.

**Query Parameters:**
- `limit`: Maximum number of orders to return (default: 50)
- `offset`: Number of orders to skip (default: 0)
- `status`: Filter by order status (open, filled, canceled)

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "order_id": "alpaca-12345678",
      "client_order_id": "bot1-1713746400000-uuid123",
      "symbol": "BTCUSD",
      "side": "buy",
      "quantity": 0.05,
      "order_type": "market",
      "status": "filled",
      "filled_price": 64338.50,
      "created_at": "2023-04-22T10:20:00Z",
      "updated_at": "2023-04-22T10:20:02Z",
      "has_sl_tp": true
    }
  ],
  "meta": {
    "pagination": {
      "total": 120,
      "limit": 50,
      "offset": 0
    }
  }
}
```

#### PUT /bot_state
Updates the active state of a trading bot.

**Request Body:**
```json
{
  "bot_id": "bot1",
  "active": true,
  "config": {
    "base_order_pct": 0.02,
    "use_limit_orders": false,
    "attach_sl_tp": true,
    "sl_pct": 0.01,
    "tp_pct": 0.02,
    "enable_global_sl_tp": true,
    "global_sl_pct": 0.80,
    "global_tp_pct": 1.20
  }
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "bot_id": "bot1",
    "active": true,
    "updated_at": "2023-04-22T11:15:00Z",
    "config_applied": true
  }
}
```

### [Other Resources]

Additional API endpoints will be defined as the project progresses.

## Pagination

For endpoints that return lists, pagination is supported using the following query parameters:

- `page`: Page number (default: 1)
- `limit`: Results per page (default: 20, max: 100)

**Example:**
```
GET /api/v1/resources?page=2&limit=10
```

**Paginated Response:**
```json
{
  "success": true,
  "data": [ /* array of items */ ],
  "meta": {
    "pagination": {
      "total": 45,
      "pages": 5,
      "page": 2,
      "limit": 10
    }
  }
}
```

## Rate Limiting

API endpoints are rate-limited to prevent abuse:

- 100 requests per minute per IP address
- 1000 requests per hour per user account

Exceeding these limits will result in a 429 Too Many Requests response.

## Versioning

The API version is included in the URL path (`/api/v1/`). Future breaking changes will use a new version number.

*Note: This API specification will be expanded as the project progresses.* 