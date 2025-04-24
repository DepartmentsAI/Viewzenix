"""
Order Calculator
---
Calculates order sizes based on different sizing strategies (percentage, fixed, notional).
"""
from typing import Dict, Any, Optional
from loguru import logger


class OrderCalculator:
    """
    Calculates order sizes based on different strategies and account information.
    """
    
    @staticmethod
    def calculate_from_tradingview(
        alert_data: Dict[str, Any],
        account_info: Dict[str, Any],
        sizing_preference: str = "tradingview"
    ) -> float:
        """
        Calculate the order size based on TradingView alert data and account info.
        
        Args:
            alert_data: Classified TradingView alert data
            account_info: Account information from broker
            sizing_preference: Strategy to use for sizing:
                - "tradingview": Use the contracts from TradingView directly
                - "percentage": Use a percentage of equity
                - "notional": Use a fixed dollar amount
                - "fixed": Use a fixed quantity
                
        Returns:
            float: Calculated order size
        """
        symbol = alert_data.get("symbol", "")
        price = alert_data.get("strategy_order_price", 0.0)
        
        # Get equity from account info
        equity = float(account_info.get("equity", 0.0))
        
        # Different sizing strategies
        if sizing_preference == "tradingview":
            # Use the contracts directly from TradingView alert
            contracts = alert_data.get("strategy_order_contracts", 0.0)
            logger.info(f"Using TradingView contracts: {contracts}")
            return float(contracts)
            
        elif sizing_preference == "percentage":
            # Use a percentage of account equity
            # Get percentage from settings (placeholder)
            percentage = 0.02  # 2% by default, should come from configuration
            contracts = (equity * percentage) / price if price > 0 else 0.0
            
            logger.info(f"Calculated {percentage:.1%} of equity ({equity}) order: {contracts} units")
            return contracts
            
        elif sizing_preference == "notional":
            # Use a fixed dollar amount
            # Get dollar amount from settings (placeholder)
            dollar_amount = 1000.0  # $1000 by default, should come from configuration
            contracts = dollar_amount / price if price > 0 else 0.0
            
            logger.info(f"Calculated ${dollar_amount} notional order: {contracts} units")
            return contracts
            
        elif sizing_preference == "fixed":
            # Use a fixed quantity
            # Get fixed quantity from settings (placeholder)
            fixed_quantity = 1.0  # Default, should come from configuration
            
            logger.info(f"Using fixed quantity: {fixed_quantity}")
            return fixed_quantity
            
        else:
            logger.warning(f"Unknown sizing preference: {sizing_preference}, defaulting to TradingView contracts")
            return float(alert_data.get("strategy_order_contracts", 0.0))
    
    @staticmethod
    def apply_asset_constraints(
        quantity: float,
        alert_data: Dict[str, Any],
        broker_constraints: Optional[Dict[str, Any]] = None
    ) -> float:
        """
        Apply asset-specific constraints to order size.
        
        Some brokers or assets have minimum order sizes, maximum order sizes,
        or lot size constraints. This method adjusts the calculated quantity
        based on these constraints.
        
        Args:
            quantity: Calculated order size
            alert_data: Classified TradingView alert data
            broker_constraints: Optional broker-specific constraints
            
        Returns:
            float: Adjusted order size
        """
        symbol = alert_data.get("symbol", "")
        asset_class = alert_data.get("asset_class", "equity")
        
        if broker_constraints is None:
            broker_constraints = {}
        
        # Apply minimum order size constraints
        min_size = broker_constraints.get("min_order_size", {}).get(asset_class, 0.0)
        if quantity < min_size and quantity > 0:
            logger.info(f"Order size {quantity} below minimum {min_size}, adjusting to minimum")
            quantity = min_size
            
        # Apply lot size constraints (e.g., stocks might need to be in whole shares)
        lot_size = broker_constraints.get("lot_size", {}).get(asset_class, 0.0)
        if lot_size > 0:
            # Round to nearest lot size
            adjusted_quantity = round(quantity / lot_size) * lot_size
            if adjusted_quantity != quantity:
                logger.info(f"Adjusted quantity from {quantity} to {adjusted_quantity} based on lot size {lot_size}")
                quantity = adjusted_quantity
                
        # Apply maximum order size constraints
        max_size = broker_constraints.get("max_order_size", {}).get(asset_class, float('inf'))
        if quantity > max_size:
            logger.info(f"Order size {quantity} above maximum {max_size}, adjusting to maximum")
            quantity = max_size
            
        return quantity 