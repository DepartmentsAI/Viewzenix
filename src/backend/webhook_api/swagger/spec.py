"""
Swagger Specification
---
OpenAPI specification for the Viewzenix Webhook API.
"""

# Swagger specification dictionary
SWAGGER_SPEC = {
    "swagger": "2.0",
    "info": {
        "title": "Viewzenix Webhook API",
        "description": "API for receiving TradingView alerts and executing trades",
        "version": "0.1.0"
    },
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ],
    "securityDefinitions": {
        "ApiKeyAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "X-API-KEY"
        }
    },
    "paths": {
        "/": {
            "get": {
                "summary": "API health check",
                "description": "Returns the API status and version information",
                "operationId": "getApiStatus",
                "responses": {
                    "200": {
                        "description": "Successful operation",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "status": {
                                    "type": "string",
                                    "example": "running"
                                },
                                "name": {
                                    "type": "string",
                                    "example": "Viewzenix Webhook API"
                                },
                                "version": {
                                    "type": "string",
                                    "example": "0.1.0"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/webhook": {
            "post": {
                "summary": "Process TradingView alert",
                "description": "Receives and processes a webhook alert from TradingView",
                "operationId": "processTradingViewAlert",
                "parameters": [
                    {
                        "in": "body",
                        "name": "alert",
                        "description": "TradingView alert payload",
                        "required": True,
                        "schema": {
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
                                    "description": "Trading symbol (e.g., BTCUSD, AAPL, EUR/USD)",
                                    "example": "BTCUSD"
                                },
                                "strategy_order_id": {
                                    "type": "string",
                                    "description": "Identifier for the trade (e.g., 'long', 'short')",
                                    "example": "long"
                                },
                                "strategy_order_action": {
                                    "type": "string",
                                    "description": "Trade direction",
                                    "enum": ["buy", "sell"],
                                    "example": "buy"
                                },
                                "strategy_order_contracts": {
                                    "type": "number",
                                    "description": "Order size (quantity)",
                                    "example": 0.1
                                },
                                "strategy_order_price": {
                                    "type": "number",
                                    "description": "Current price when alert triggered",
                                    "example": 64500.25
                                },
                                "strategy_order_comment": {
                                    "type": "string",
                                    "description": "Optional comment for the trade",
                                    "example": "Breakout signal"
                                },
                                "time": {
                                    "type": "integer",
                                    "description": "Timestamp in milliseconds",
                                    "example": 1713746400000
                                }
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful operation",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": True
                                },
                                "data": {
                                    "type": "object",
                                    "properties": {
                                        "received": {
                                            "type": "boolean",
                                            "example": True
                                        },
                                        "order_id": {
                                            "type": "string",
                                            "example": "a1b2c3d4-e5f6-g7h8-i9j0"
                                        },
                                        "client_order_id": {
                                            "type": "string",
                                            "example": "tv-1713746400-a1b2c3d4"
                                        },
                                        "symbol": {
                                            "type": "string",
                                            "example": "BTCUSD"
                                        },
                                        "order_type": {
                                            "type": "string",
                                            "example": "market"
                                        },
                                        "side": {
                                            "type": "string",
                                            "example": "buy"
                                        },
                                        "quantity": {
                                            "type": "number",
                                            "example": 0.1
                                        },
                                        "timestamp": {
                                            "type": "integer",
                                            "example": 1713746480000
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "400": {
                        "description": "Invalid input",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": False
                                },
                                "error": {
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "string",
                                            "example": "VALIDATION_ERROR"
                                        },
                                        "message": {
                                            "type": "string",
                                            "example": "Invalid TradingView alert format"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "500": {
                        "description": "Server error",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": False
                                },
                                "error": {
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "string",
                                            "example": "SERVER_ERROR"
                                        },
                                        "message": {
                                            "type": "string",
                                            "example": "An error occurred processing the webhook"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/status": {
            "get": {
                "summary": "Get system status",
                "description": "Returns the current status of the trading system",
                "operationId": "getSystemStatus",
                "responses": {
                    "200": {
                        "description": "Successful operation",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": True
                                },
                                "data": {
                                    "type": "object",
                                    "properties": {
                                        "status": {
                                            "type": "string",
                                            "example": "active"
                                        },
                                        "broker_connected": {
                                            "type": "boolean",
                                            "example": True
                                        },
                                        "broker_name": {
                                            "type": "string",
                                            "example": "Alpaca"
                                        },
                                        "positions_count": {
                                            "type": "integer",
                                            "example": 3
                                        },
                                        "open_orders_count": {
                                            "type": "integer",
                                            "example": 2
                                        },
                                        "global_sl_tp_active": {
                                            "type": "boolean",
                                            "example": True
                                        },
                                        "base_equity": {
                                            "type": "number",
                                            "example": 10000.0
                                        },
                                        "current_equity": {
                                            "type": "number",
                                            "example": 10250.75
                                        },
                                        "uptime": {
                                            "type": "string",
                                            "example": "2d 5h 30m"
                                        },
                                        "server_time": {
                                            "type": "string",
                                            "example": "2023-05-01T12:30:45.123Z"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "500": {
                        "description": "Server error",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": False
                                },
                                "error": {
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "string",
                                            "example": "SERVER_ERROR"
                                        },
                                        "message": {
                                            "type": "string",
                                            "example": "Error retrieving system status"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/orders": {
            "get": {
                "summary": "Get orders",
                "description": "Returns a list of orders with pagination",
                "operationId": "getOrders",
                "parameters": [
                    {
                        "in": "query",
                        "name": "limit",
                        "description": "Maximum number of orders to return",
                        "required": False,
                        "type": "integer",
                        "default": 50
                    },
                    {
                        "in": "query",
                        "name": "offset",
                        "description": "Number of orders to skip",
                        "required": False,
                        "type": "integer",
                        "default": 0
                    },
                    {
                        "in": "query",
                        "name": "status",
                        "description": "Filter by order status",
                        "required": False,
                        "type": "string",
                        "enum": ["open", "filled", "canceled"]
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful operation",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": True
                                },
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "id": {
                                                "type": "string",
                                                "example": "a1b2c3d4-e5f6-g7h8-i9j0"
                                            },
                                            "client_order_id": {
                                                "type": "string",
                                                "example": "tv-1713746400-a1b2c3d4"
                                            },
                                            "symbol": {
                                                "type": "string",
                                                "example": "BTCUSD"
                                            },
                                            "side": {
                                                "type": "string",
                                                "example": "buy"
                                            },
                                            "quantity": {
                                                "type": "number",
                                                "example": 0.1
                                            },
                                            "filled_quantity": {
                                                "type": "number",
                                                "example": 0.1
                                            },
                                            "type": {
                                                "type": "string",
                                                "example": "market"
                                            },
                                            "status": {
                                                "type": "string",
                                                "example": "filled"
                                            },
                                            "created_at": {
                                                "type": "string",
                                                "example": "2023-05-01T12:30:45.123Z"
                                            }
                                        }
                                    }
                                },
                                "meta": {
                                    "type": "object",
                                    "properties": {
                                        "pagination": {
                                            "type": "object",
                                            "properties": {
                                                "total": {
                                                    "type": "integer",
                                                    "example": 125
                                                },
                                                "limit": {
                                                    "type": "integer",
                                                    "example": 50
                                                },
                                                "offset": {
                                                    "type": "integer",
                                                    "example": 0
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "500": {
                        "description": "Server error",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": False
                                },
                                "error": {
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "string",
                                            "example": "SERVER_ERROR"
                                        },
                                        "message": {
                                            "type": "string",
                                            "example": "Error retrieving orders"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/orders/{order_id}": {
            "get": {
                "summary": "Get order by ID",
                "description": "Returns details for a specific order",
                "operationId": "getOrderById",
                "parameters": [
                    {
                        "in": "path",
                        "name": "order_id",
                        "description": "Order ID",
                        "required": True,
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful operation",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": True
                                },
                                "data": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "string",
                                            "example": "a1b2c3d4-e5f6-g7h8-i9j0"
                                        },
                                        "client_order_id": {
                                            "type": "string",
                                            "example": "tv-1713746400-a1b2c3d4"
                                        },
                                        "symbol": {
                                            "type": "string",
                                            "example": "BTCUSD"
                                        },
                                        "side": {
                                            "type": "string",
                                            "example": "buy"
                                        },
                                        "quantity": {
                                            "type": "number",
                                            "example": 0.1
                                        },
                                        "filled_quantity": {
                                            "type": "number",
                                            "example": 0.1
                                        },
                                        "type": {
                                            "type": "string",
                                            "example": "market"
                                        },
                                        "status": {
                                            "type": "string",
                                            "example": "filled"
                                        },
                                        "created_at": {
                                            "type": "string",
                                            "example": "2023-05-01T12:30:45.123Z"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Order not found",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": False
                                },
                                "error": {
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "string",
                                            "example": "NOT_FOUND"
                                        },
                                        "message": {
                                            "type": "string",
                                            "example": "Order not found"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "500": {
                        "description": "Server error",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": False
                                },
                                "error": {
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "string",
                                            "example": "SERVER_ERROR"
                                        },
                                        "message": {
                                            "type": "string",
                                            "example": "Error retrieving order"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "delete": {
                "summary": "Cancel order",
                "description": "Cancels a specific order",
                "operationId": "cancelOrder",
                "parameters": [
                    {
                        "in": "path",
                        "name": "order_id",
                        "description": "Order ID",
                        "required": True,
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful operation",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": True
                                },
                                "data": {
                                    "type": "object",
                                    "properties": {
                                        "order_id": {
                                            "type": "string",
                                            "example": "a1b2c3d4-e5f6-g7h8-i9j0"
                                        },
                                        "canceled": {
                                            "type": "boolean",
                                            "example": True
                                        },
                                        "message": {
                                            "type": "string",
                                            "example": "Order successfully canceled"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Order not found",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": False
                                },
                                "error": {
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "string",
                                            "example": "NOT_FOUND"
                                        },
                                        "message": {
                                            "type": "string",
                                            "example": "Order not found"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "500": {
                        "description": "Server error",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "success": {
                                    "type": "boolean",
                                    "example": False
                                },
                                "error": {
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "string",
                                            "example": "SERVER_ERROR"
                                        },
                                        "message": {
                                            "type": "string",
                                            "example": "Error canceling order"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
} 