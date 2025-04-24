# Viewzenix Project Requirements

## Project Overview
Viewzenix is an AI-driven software development pipeline where specialized AI agents collaborate to build, test, and integrate a web application. The pipeline leverages automated communication, version control, and standardized workflows to streamline development.

## Project Goals
- Develop a functional web application through AI agent collaboration
- Establish robust and repeatable workflows for AI-driven development
- Measure and optimize agent performance using Prompt Units
- Ensure adherence to high standards of code quality, security, and performance
- Minimize human intervention required for routine development tasks

## Functional Requirements

### Trading Webhook Platform
1. **Webhook Receiver**
   - Accept and validate incoming webhooks from TradingView
   - Enforce fixed JSON schema validation
   - Process trade alerts based on a standard format

2. **Trade Classification & Routing**
   - Classify assets (crypto, equity, forex)
   - Support long/short entry and exit operations
   - Route orders to appropriate broker adapters

3. **Order Execution**
   - Support multiple order types (market, limit, stop, bracket)
   - Implement various sizing strategies (percentage, fixed contracts, notional)
   - Handle order tagging and tracking

4. **Risk Management**
   - Implement per-order stop-loss and take-profit functionality
   - Provide global portfolio stop-loss/take-profit monitoring
   - Enforce broker-specific trading restrictions

5. **Monitoring & Logging**
   - Comprehensive logging of all webhook interactions
   - Detailed activity tracking for auditing
   - Performance and status monitoring

6. **Administration Interface**
   - React dashboard with minimal-click interface
   - Configuration management for trading parameters
   - Order history and status visibility
   - Cleanup and maintenance tools

## Non-Functional Requirements
- **Performance**: The application must adhere to performance standards defined in 042-red-lines-performance.mdc
- **Security**: The application must follow security standards defined in 041-red-lines-security.mdc
- **Reliability**: The application must be resilient and handle errors gracefully
- **Scalability**: The application architecture must support horizontal scaling
- **Maintainability**: Code must follow the standards outlined in 030-code-standards-always.mdc
- **Testability**: The application must include comprehensive test harnesses that can run when markets are closed

## Technical Stack
- **Frontend**: React with TypeScript
- **Backend**: Node.js with TypeScript and Flask (for trading webhook API)
- **Database**: [To be determined]
- **Testing**: Jest, React Testing Library, Cypress, pytest
- **Broker Integration**: Alpaca API (initially), extensible to other brokers

## Development Process
- Follows the GitHub workflow defined in 011-github-workflow.mdc
- Uses standardized communication protocols defined in 010-communication-protocol-always.mdc
- Agent roles and responsibilities as defined in 004-scope-matrix.mdc

*This is an initial version. Requirements will be refined as the project progresses.* 