"""
Webhook API Tests
---
Tests for the TradingView webhook API.
"""
import json
import pytest
from unittest.mock import patch, MagicMock

from ..app import app as flask_app


@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    flask_app.config.update({
        "TESTING": True,
    })
    
    yield flask_app


@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()


def test_index_route(client):
    """Test the index route returns correct status."""
    response = client.get("/")
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data["status"] == "running"
    assert "Viewzenix Webhook API" in data["name"]


@patch('webhook_api.adapters.alpaca_adapter.AlpacaAdapter')
def test_webhook_endpoint_validation(mock_adapter, client):
    """Test that the webhook endpoint validates incoming data."""
    # Invalid payload (missing required fields)
    invalid_payload = {
        "symbol": "BTCUSD",
        # Missing required fields
    }
    
    response = client.post("/webhook", json=invalid_payload)
    data = json.loads(response.data)
    
    assert response.status_code == 400
    assert data["success"] is False
    assert "VALIDATION_ERROR" in data["error"]["code"]


@patch('webhook_api.adapters.alpaca_adapter.AlpacaAdapter')
def test_status_endpoint(mock_adapter_class, client):
    """Test the status endpoint returns correct information."""
    # Mock the adapter's methods
    mock_adapter = MagicMock()
    mock_adapter.connect.return_value = True
    mock_adapter.get_account_info.return_value = {"equity": "10000.00"}
    mock_adapter.get_positions.return_value = [{"symbol": "BTCUSD"}]
    mock_adapter.get_orders.return_value = [{"id": "123"}]
    
    mock_adapter_class.return_value = mock_adapter
    
    response = client.get("/status")
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data["success"] is True
    assert data["data"]["status"] == "active"
    assert data["data"]["broker_connected"] is True
    assert data["data"]["positions_count"] == 1
    assert data["data"]["open_orders_count"] == 1 