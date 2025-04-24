<message>
  <id>Msg-PM-To-BE-Seq001-a2b3c4</id>
  <sender>PM</sender>
  <recipient>BE</recipient>
  <type>TASK_ASSIGNMENT</type>
  <subject>Backend Agent Initial Tasks - Flask Webhook API Setup</subject>
  <content>
    Backend Agent,
    
    Your initial tasks focus on establishing the Flask webhook API foundation that will serve as the core entry point for TradingView alerts. Please prioritize the following:
    
    1. **Flask API Structure (5 PU)**
       - Set up Flask project structure in `src/backend/webhook_api/`
       - Implement initial blueprints for core endpoints: `/webhook`, `/status`, `/cleanup`, `/orders`, `/bot_state`
       - Create JSON schema validation for webhook payloads following TradingView format
    
    2. **Trade Router Component (7 PU)**
       - Develop asset classifier that identifies crypto/equity/forex from symbols
       - Implement trade type determination from strategy_order_id and strategy_order_action
       - Create order size calculator supporting percentage, fixed contracts, and notional sizing
    
    3. **Broker Adapter Framework (6 PU)**
       - Define base adapter interface for broker integration
       - Implement initial AlpacaAdapter with core trading methods
       - Create proper error handling and response normalization
    
    4. **Testing Harness Foundation (8 PU)**
       - Set up pytest structure for testing Flask endpoints
       - Implement mock broker responses for offline testing
       - Create initial tests for JSON schema validation and asset classification
    
    Please coordinate with the Integration Agent on the adapter interface design and with the QA Agent on testing harness development.
    
    Priority order: Task 1 → Task 2 → Task 3 → Task 4
    
    Documentation on APIs available in `/docs/api/API_SPECS.md` and architecture in `/docs/architecture/ARCHITECTURE.md`.
    
    Reply with your initial assessment and any clarification questions.
  </content>
</message> 