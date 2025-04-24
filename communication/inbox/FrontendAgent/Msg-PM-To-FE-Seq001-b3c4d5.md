<message>
  <id>Msg-PM-To-FE-Seq001-b3c4d5</id>
  <sender>PM</sender>
  <recipient>FE</recipient>
  <type>TASK_ASSIGNMENT</type>
  <subject>Frontend Agent Initial Tasks - Trading Dashboard Setup</subject>
  <content>
    Frontend Agent,
    
    Your initial focus will be on establishing the React dashboard foundation for the trading webhook platform. Please prioritize the following tasks:
    
    1. **Project Structure and Component Architecture (4 PU)**
       - Set up React frontend structure in `src/frontend/`
       - Configure build system and TypeScript integration
       - Create component hierarchy based on UI specifications
    
    2. **Dashboard Layout and Navigation (6 PU)**
       - Implement main dashboard shell with responsive layout
       - Create navigation system with tabs: Webhook Setup, Brokers, Bots, Logs, Analytics
       - Establish theme and styling system following design guidelines
    
    3. **Webhook Configuration UI (7 PU)**
       - Develop webhook setup screen with configuration form
       - Create visual TradingView alert generator with required JSON format
       - Implement copy/paste functionality for webhook URLs and payloads
    
    4. **Bot Configuration Panel (8 PU)**
       - Create UI for trading bot configuration (base_order_pct, order types, SL/TP settings)
       - Implement toggles for various trading parameters
       - Add global SL/TP configuration section with base equity input
    
    All UI components should follow the design specifications in `/docs/ui/DESIGN_SPECS.md` with a focus on minimal-click access and hover tooltips to maximize usability.
    
    Priority order: Task 1 → Task 2 → Task 3 → Task 4
    
    Please coordinate with the Backend Agent to ensure alignment on API interfaces that will be consumed by the frontend.
    
    Reply with your initial assessment and any clarification questions.
  </content>
</message> 