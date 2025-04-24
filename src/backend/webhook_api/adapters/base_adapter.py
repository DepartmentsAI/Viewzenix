"""
Base Broker Adapter
---
Defines the interface that all broker adapters must implement.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional


class BaseBrokerAdapter(ABC):
    """
    Abstract base class for all broker adapters.
    
    All broker implementations must extend this class and implement
    its abstract methods to ensure consistency across different brokers.
    """
    
    @abstractmethod
    def connect(self) -> bool:
        """
        Establish a connection to the broker API.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        pass
    
    @abstractmethod
    def get_account_info(self) -> Dict[str, Any]:
        """
        Retrieve current account information.
        
        Returns:
            Dict[str, Any]: Account details including balance, equity, etc.
        """
        pass
    
    @abstractmethod
    def place_market_order(
        self, 
        symbol: str, 
        side: str, 
        quantity: float,
        client_order_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Place a market order.
        
        Args:
            symbol: The trading symbol (e.g., 'BTCUSD')
            side: 'buy' or 'sell'
            quantity: Order size
            client_order_id: Optional client-defined order ID for tracking
            
        Returns:
            Dict[str, Any]: Order details including broker order ID
        """
        pass
    
    @abstractmethod
    def place_limit_order(
        self, 
        symbol: str, 
        side: str, 
        quantity: float, 
        price: float,
        client_order_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Place a limit order.
        
        Args:
            symbol: The trading symbol (e.g., 'BTCUSD')
            side: 'buy' or 'sell'
            quantity: Order size
            price: Limit price
            client_order_id: Optional client-defined order ID for tracking
            
        Returns:
            Dict[str, Any]: Order details including broker order ID
        """
        pass
    
    @abstractmethod
    def place_stop_order(
        self, 
        symbol: str, 
        side: str, 
        quantity: float, 
        stop_price: float,
        client_order_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Place a stop order.
        
        Args:
            symbol: The trading symbol (e.g., 'BTCUSD')
            side: 'buy' or 'sell'
            quantity: Order size
            stop_price: Stop price to trigger the order
            client_order_id: Optional client-defined order ID for tracking
            
        Returns:
            Dict[str, Any]: Order details including broker order ID
        """
        pass
    
    @abstractmethod
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
        Place a bracket order with entry, stop loss, and take profit.
        
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
        pass
    
    @abstractmethod
    def get_order(self, order_id: str) -> Dict[str, Any]:
        """
        Get information about a specific order.
        
        Args:
            order_id: Broker order ID
            
        Returns:
            Dict[str, Any]: Order details
        """
        pass
    
    @abstractmethod
    def get_orders(self) -> List[Dict[str, Any]]:
        """
        Get all open orders.
        
        Returns:
            List[Dict[str, Any]]: List of order details
        """
        pass
    
    @abstractmethod
    def cancel_order(self, order_id: str) -> Dict[str, Any]:
        """
        Cancel an existing order.
        
        Args:
            order_id: Broker order ID
            
        Returns:
            Dict[str, Any]: Cancellation details
        """
        pass
    
    @abstractmethod
    def get_positions(self) -> List[Dict[str, Any]]:
        """
        Get all open positions.
        
        Returns:
            List[Dict[str, Any]]: List of position details
        """
        pass 