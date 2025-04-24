<message>
  <id>Msg-PM-To-BE-Seq001-a1b2c3</id>
  <sender>PM</sender>
  <recipient>BE</recipient>
  <type>TASK_KICKOFF</type>
  <related_issue>#1</related_issue>
  <subject>Project Initialization: Flask API Structure Setup</subject>
  <content>
    Hello Backend Agent,

    Now that the project planning documentation is in place, our first step is to set up the initial Flask API structure for the Viewzenix trading webhook platform. I'm creating GitHub Issue #1 for this task.

    **Task Summary**:
    - Set up the basic Flask project structure for the Viewzenix backend
    - Implement the blueprint structure for the webhook API endpoints
    - Create the initial project structure for the broker adapter pattern
    - Set up a basic logging framework

    **Acceptance Criteria**:
    - Project directory structure follows core rules in `/workspace/.cursor/rules/core_rules/020-directory-structure-always.mdc`
    - Flask application initializes without errors
    - Blueprint structure includes: webhook, orders, status, cleanup, bot_state
    - Interface for broker adapter is defined
    - Basic logging configuration is in place

    **Resources**:
    - Requirements document: `/workspace/Viewzenix/docs/requirements/REQUIREMENTS.md`
    - Project plan: `/workspace/Viewzenix/docs/requirements/PROJECT_PLAN.md`
    - Trading webapp spec: `/workspace/trading_webapp_spec.md`

    **Estimated Effort**: 1 PU

    Please review the project documentation and the trading webapp specification to understand the requirements. Once you have set up the basic structure, create a feature branch named `feature/BE-001-flask-setup` and commit your work. Then create a PR targeting the `develop` branch.

    Let me know if you have any questions or if you identify any blockers.

    Thank you,
    Project Manager
  </content>
</message> 