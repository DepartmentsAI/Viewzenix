"""
Alpaca Broker Adapter
---
Implementation of the broker adapter interface for the Alpaca API.
"""
import os
from typing import Dict, Any, List, Optional
import requests
from loguru import logger

from .base_adapter import BaseBrokerAdapter


class AlpacaAdapter(BaseBrokerAdapter):
    """
    Adapter for the Alpaca API.
    
    Implements the BaseBrokerAdapter interface for Alpaca trading API.
    Paper trading is used by default, can be switched to live trading
    by setting the ALPACA_LIVE_TRADING environment variable to 'true'.
    """
    
    def __init__(self):
        """Initialize the Alpaca adapter with API credentials from environment variables."""
        self.api_key = os.environ.get('ALPACA_API_KEY')
        self.api_secret = os.environ.get('ALPACA_API_SECRET')
        
        # Determine if we're using live or paper trading
        use_live = os.environ.get('ALPACA_LIVE_TRADING', 'false').lower() == 'true'
        
        if use_live:
            self.base_url = 'https://api.alpaca.markets'
            logger.warning("Using LIVE trading with Alpaca")
        else:
            self.base_url = 'https://paper-api.alpaca.markets'
            logger.info("Using PAPER trading with Alpaca")
            
        self.headers = {
            'APCA-API-KEY-ID': self.api_key,
            'APCA-API-SECRET-KEY': self.api_secret,
            'Content-Type': 'application/json'
        }
    
    def _make_request(self, method: str, endpoint: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Make an HTTP request to the Alpaca API.
        
        Args:
            method: HTTP method (GET, POST, DELETE, etc.)
            endpoint: API endpoint (e.g., '/v2/orders')
            data: Optional data payload for POST/PUT requests
            
        Returns:
            Dict[str, Any]: JSON response from Alpaca API
            
        Raises:
            Exception: If request fails
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method.upper() == 'GET':
                response = requests.get(url, headers=self.headers)
            elif method.upper() == 'POST':
                response = requests.post(url, headers=self.headers, json=data)
            elif method.upper() == 'DELETE':
                response = requests.delete(url, headers=self.headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            return response.json() if response.content else {}
            
        except Exception as e:
            logger.error(f"Alpaca API request failed: {str(e)}")
            raise
    
    def connect(self) -> bool:
        """
        Test connection to Alpaca API.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            account = self._make_request('GET', '/v2/account')
            logger.info(f"Connected to Alpaca account: {account.get('id')}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Alpaca: {str(e)}")
            return False
    
    def get_account_info(self) -> Dict[str, Any]:
        """
        Get Alpaca account information.
        
        Returns:
            Dict[str, Any]: Account details including balance, equity, etc.
        """
        return self._make_request('GET', '/v2/account')
    
    def place_market_order(
        self, 
        symbol: str, 
        side: str, 
        quantity: float,
        client_order_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Place a market order on Alpaca.
        
        Args:
            symbol: The trading symbol (e.g., 'BTCUSD')
            side: 'buy' or 'sell'
            quantity: Order size
            client_order_id: Optional client-defined order ID for tracking
            
        Returns:
            Dict[str, Any]: Order details including broker order ID
        """
        data = {
            "symbol": symbol,
            "qty": str(quantity),
            "side": side.lower(),
            "type": "market",
            "time_in_force": "gtc"
        }
        
        if client_order_id:
            data["client_order_id"] = client_order_id
            
        logger.info(f"Placing market order: {data}")
        return self._make_request('POST', '/v2/orders', data)
    
    def place_limit_order(
        self, 
        symbol: str, 
        side: str, 
        quantity: float, 
        price: float,
        client_order_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Place a limit order on Alpaca.
        
        Args:
            symbol: The trading symbol (e.g., 'BTCUSD')
            side: 'buy' or 'sell'
            quantity: Order size
            price: Limit price
            client_order_id: Optional client-defined order ID for tracking
            
        Returns:
            Dict[str, Any]: Order details including broker order ID
        """
        data = {
            "symbol": symbol,
            "qty": str(quantity),
            "side": side.lower(),
            "type": "limit",
            "time_in_force": "gtc",
            "limit_price": str(price)
        }
        
        if client_order_id:
            data["client_order_id"] = client_order_id
            
        logger.info(f"Placing limit order: {data}")
        return self._make_request('POST', '/v2/orders', data)
    
    def place_stop_order(
        self, 
        symbol: str, 
        side: str, 
        quantity: float, 
        stop_price: float,
        client_order_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Place a stop order on Alpaca.
        
        Args:
            symbol: The trading symbol (e.g., 'BTCUSD')
            side: 'buy' or 'sell'
            quantity: Order size
            stop_price: Stop price to trigger the order
            client_order_id: Optional client-defined order ID for tracking
            
        Returns:
            Dict[str, Any]: Order details including broker order ID
        """
        data = {
            "symbol": symbol,
            "qty": str(quantity),
            "side": side.lower(),
            "type": "stop",
            "time_in_force": "gtc",
            "stop_price": str(stop_price)
        }
        
        if client_order_id:
            data["client_order_id"] = client_order_id
            
        logger.info(f"Placing stop order: {data}")
        return self._make_request('POST', '/v2/orders', data)
    
    def place_bracket_order(
        self, 
        symbol: str, 
        side: str, 
        quantity: float, 
        entry_price: Optional[float] = None,
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None,
        client_order_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Place a bracket order on Alpaca with entry, stop loss, and take profit.
        
        Args:
            symbol: The trading symbol (e.g., 'BTCUSD')
            side: 'buy' or 'sell'
            quantity: Order size
            entry_price: Optional limit price for entry (None for market)
            stop_loss: Optional stop loss price
            take_profit: Optional take profit price
            client_order_id: Optional client-defined order ID for tracking
            
        Returns:
            Dict[str, Any]: Order details including all broker order IDs
        """
        order_type = "limit" if entry_price else "market"
        
        data = {
            "symbol": symbol,
            "qty": str(quantity),
            "side": side.lower(),
            "type": order_type,
            "time_in_force": "gtc",
            "order_class": "bracket"
        }
        
        if entry_price:
            data["limit_price"] = str(entry_price)
            
        if stop_loss:
            data["stop_loss"] = {"stop_price": str(stop_loss)}
            
        if take_profit:
            data["take_profit"] = {"limit_price": str(take_profit)}
            
        if client_order_id:
            data["client_order_id"] = client_order_id
            
        logger.info(f"Placing bracket order: {data}")
        return self._make_request('POST', '/v2/orders', data)
    
    def get_order(self, order_id: str) -> Dict[str, Any]:
        """
        Get information about a specific order from Alpaca.
        
        Args:
            order_id: Alpaca order ID
            
        Returns:
            Dict[str, Any]: Order details
        """
        return self._make_request('GET', f'/v2/orders/{order_id}')
    
    def get_orders(self) -> List[Dict[str, Any]]:
        """
        Get all open orders from Alpaca.
        
        Returns:
            List[Dict[str, Any]]: List of order details
        """
        return self._make_request('GET', '/v2/orders')
    
    def cancel_order(self, order_id: str) -> Dict[str, Any]:
        """
        Cancel an existing order on Alpaca.
        
        Args:
            order_id: Alpaca order ID
            
        Returns:
            Dict[str, Any]: Cancellation details
        """
        return self._make_request('DELETE', f'/v2/orders/{order_id}')
    
    def get_positions(self) -> List[Dict[str, Any]]:
        """
        Get all open positions from Alpaca.
        
        Returns:
            List[Dict[str, Any]]: List of position details
        """
        return self._make_request('GET', '/v2/positions') 