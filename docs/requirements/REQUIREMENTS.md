# Viewzenix Requirements Document

## 1. Project Overview

Viewzenix is a trading webhook platform that enables deterministic, broker-agnostic trade execution from TradingView alerts through an API gateway. It provides a feature-rich dashboard with advanced features, robust testing capabilities, granular fail-safes, and an extensible design for future enhancements.

## 2. Core Objectives

| Goal | Description |
|------|-------------|
| **Deterministic, broker-agnostic trade execution** | Guarantees identical behavior across equities, crypto, and (future) forex brokers |
| **Feature-rich dashboard** | Provides minimal-click access, hover tool-tips, and advanced toggles to make a complex algo-trading stack approachable |
| **Robust test harnesses** | Allows core-logic regression testing without broker dependency |
| **Granular fail-safes** | Includes order-level & global SL/TP, broker restrictions, and portfolio circuit-breakers to protect capital |
| **Extensible design** | Supports "drop-in" addition of new brokers, asset classes, or AI modules |

## 3. Functional Requirements

### 3.1 Webhook Processing

- **FR-001**: System MUST accept and validate TradingView webhook alerts in a predefined JSON format
- **FR-002**: System MUST classify asset types (crypto, equity, forex) based on symbol
- **FR-003**: System MUST determine trade type (long entry, long exit, short entry, short exit) based on alert parameters
- **FR-004**: System MUST support multiple order sizing strategies:
  - Percentage of equity
  - Contracts from TradingView
  - Notional (dollar-based)
  - Fractional shares/coins

### 3.2 Order Management

- **FR-005**: System MUST support multiple order types:
  - Market (default)
  - Limit
  - Stop
  - Stop-limit
  - Trailing-stop
  - Bracket
- **FR-006**: System MUST support attaching Stop Loss (SL) and Take Profit (TP) orders to entries
- **FR-007**: System MUST support configurable pricing sources for SL/TP calculations
- **FR-008**: System MUST implement a cleanup service to remove orphaned SL/TP orders
- **FR-009**: System MUST implement global SL/TP monitoring as portfolio equity circuit breakers

### 3.3 Broker Integration

- **FR-010**: System MUST implement an AlpacaAdapter for order execution
- **FR-011**: System MUST enforce broker-specific restrictions (e.g., blocking crypto-shorts on Alpaca)
- **FR-012**: System MUST support future extension to additional brokers

### 3.4 User Interface

- **FR-013**: System MUST provide a React-based dashboard with tabs for:
  - Webhook Setup
  - Brokers
  - Bots
  - Logs
  - Analytics
- **FR-014**: UI MUST allow configuration of all trading parameters
- **FR-015**: UI MUST display current positions, orders, and account status

### 3.5 Logging and Monitoring

- **FR-016**: System MUST log all webhook alerts and broker responses in machine-readable format
- **FR-017**: System MUST maintain human-readable activity logs
- **FR-018**: System MUST provide status endpoints for system health monitoring

## 4. Non-Functional Requirements

### 4.1 Performance

- **NFR-001**: System MUST process webhook alerts within 500ms
- **NFR-002**: Global SL/TP tracker MUST poll account status every 10 seconds
- **NFR-003**: Cleanup service MUST run automatically every 30 seconds

### 4.2 Security

- **NFR-004**: System MUST be deployed on a secure hosting platform (Fly.io with private networking)
- **NFR-005**: API access MUST be limited to whitelisted IPs
- **NFR-006**: API secrets MUST be stored securely (not hard-coded)
- **NFR-007**: Future implementation MUST include JWT + RBAC (`admin`, `viewer`)

### 4.3 Reliability

- **NFR-008**: System MUST maintain 99.9% uptime during market hours
- **NFR-009**: All critical functions MUST have comprehensive test coverage
- **NFR-010**: CI/CD pipeline MUST include automated testing before deployment

### 4.4 Extensibility

- **NFR-011**: System MUST use modular architecture to support future extensions
- **NFR-012**: System MUST support multi-tenant workspaces in future versions
- **NFR-013**: System MUST support additional broker adaptors in future versions

## 5. TradingView Alert Schema

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

## 6. Future Enhancements

1. Multi-tenant workspaces & per-user API keys
2. AI Insight panel: latency & performance analytics
3. Live WebSocket broker feed in React
4. Pluggable broker adapters (IBKR, Binance)
5. Auto-generated TradingView alert builders with QR share

## 7. Technical Constraints

- Backend: Flask API
- Frontend: React (Next.js or CRA)
- Hosting: Fly.io with private networking
- Broker Integration: Starting with Alpaca API
- Testing: pytest + Postman
