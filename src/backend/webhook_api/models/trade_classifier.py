"""
Trade Classifier
---
Classifies trades by asset class and trade type based on symbol and order parameters.
"""
import re
from typing import Dict, Any, Tuple, Literal
from loguru import logger


# Types for better type hinting
AssetClass = Literal["crypto", "equity", "forex"]
TradeType = Literal["long_entry", "long_exit", "short_entry", "short_exit"]


class TradeClassifier:
    """
    Classifies trade alerts to determine asset class and trade type.
    """
    
    # Common crypto currency symbols (non-exhaustive)
    CRYPTO_SYMBOLS = {
        "BTC", "ETH", "XRP", "SOL", "ADA", "DOT", "DOGE", "AVAX", "MATIC", 
        "LINK", "UNI", "LTC", "BCH", "XLM", "ALGO", "ATOM", "FTM", "NEAR", "XTZ"
    }
    
    @staticmethod
    def classify_asset_class(symbol: str) -> AssetClass:
        """
        Determine if the symbol is for crypto, equity, or forex.
        
        Args:
            symbol: Trading symbol (e.g., BTCUSD, AAPL, EUR/USD)
            
        Returns:
            AssetClass: "crypto", "equity", or "forex"
        """
        # Check for crypto symbols
        symbol_upper = symbol.upper()
        
        # Check for common crypto patterns: BTCUSD, BTC-USD, BTC/USD
        crypto_pattern = r'^([A-Z]{2,5})[-/]?(?:USD|USDT|USDC|EUR|JPY|BTC|ETH)$'
        crypto_match = re.match(crypto_pattern, symbol_upper)
        if crypto_match and crypto_match.group(1) in TradeClassifier.CRYPTO_SYMBOLS:
            return "crypto"
        
        # Check for forex pattern: EUR/USD, EURUSD, etc.
        forex_pattern = r'^[A-Z]{3}[-/]?[A-Z]{3}$'
        if re.match(forex_pattern, symbol_upper):
            return "forex"
            
        # Assume everything else is equity
        return "equity"
    
    @staticmethod
    def classify_trade_type(
        strategy_id: str, 
        order_action: str
    ) -> TradeType:
        """
        Determine the trade type (long entry, long exit, etc.) based on strategy ID and action.
        
        Args:
            strategy_id: TradingView strategy_order_id (e.g., 'long', 'short', 'exit')
            order_action: TradingView strategy_order_action ('buy' or 'sell')
            
        Returns:
            TradeType: "long_entry", "long_exit", "short_entry", or "short_exit"
        """
        strategy_id_lower = strategy_id.lower()
        order_action_lower = order_action.lower()
        
        # Long entry: buy + long/entry or buy + !exit
        if order_action_lower == "buy":
            if "exit" in strategy_id_lower or "close" in strategy_id_lower:
                return "short_exit"  # Buying to exit a short position
            else:
                return "long_entry"  # Default buy action is to enter a long position
        
        # Sell action
        else:  # order_action_lower == "sell"
            if "exit" in strategy_id_lower or "close" in strategy_id_lower:
                return "long_exit"  # Selling to exit a long position
            else:
                return "short_entry"  # Default sell action is to enter a short position
    
    @classmethod
    def classify_trade(cls, alert_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a TradingView alert and classify the trade.
        
        Args:
            alert_data: Validated TradingView alert data
            
        Returns:
            Dict[str, Any]: Original alert data with additional classification info
        """
        symbol = alert_data.get("symbol", "")
        strategy_order_id = alert_data.get("strategy_order_id", "")
        strategy_order_action = alert_data.get("strategy_order_action", "")
        
        # Classify asset class and trade type
        asset_class = cls.classify_asset_class(symbol)
        trade_type = cls.classify_trade_type(strategy_order_id, strategy_order_action)
        
        # Add classifications to the alert data
        classified_data = alert_data.copy()
        classified_data["asset_class"] = asset_class
        classified_data["trade_type"] = trade_type
        
        logger.info(f"Classified trade: {symbol} as {asset_class}, {trade_type}")
        
        return classified_data 