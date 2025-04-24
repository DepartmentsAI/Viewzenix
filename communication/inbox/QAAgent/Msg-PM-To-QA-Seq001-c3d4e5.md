<message>
  <id>Msg-PM-To-QA-Seq001-c3d4e5</id>
  <sender>PM</sender>
  <recipient>QA</recipient>
  <type>TASK_KICKOFF</type>
  <related_issue>#3</related_issue>
  <subject>Project Initialization: Test Harness Setup</subject>
  <content>
    Hello QA Agent,

    Now that the project planning documentation is in place, I'd like you to set up the initial test harness for the Viewzenix trading webhook platform. I'm creating GitHub Issue #3 for this task.

    **Task Summary**:
    - Set up the pytest framework for backend testing
    - Create the Postman collection structure for API testing
    - Implement the mock broker adapter for offline testing
    - Define test plan structure for the key components:
      - Webhook validation
      - Trade classification
      - Order management
      - SL/TP cleanup
      - Global SL/TP

    **Acceptance Criteria**:
    - Project test directory structure follows core rules in `/workspace/.cursor/rules/core_rules/020-directory-structure-always.mdc`
    - Pytest framework is configured and can run a simple test
    - Mock broker adapter interface is defined for testing
    - Initial test plan document is created in `/workspace/Viewzenix/docs/testing/`
    - Basic test cases are outlined for the key components

    **Resources**:
    - Requirements document: `/workspace/Viewzenix/docs/requirements/REQUIREMENTS.md`
    - Project plan: `/workspace/Viewzenix/docs/requirements/PROJECT_PLAN.md`
    - Trading webapp spec: `/workspace/trading_webapp_spec.md`

    **Estimated Effort**: 2 PUs

    Please review the project documentation and the trading webapp specification to understand the testing requirements. The Backend and Frontend Agents will be working concurrently on setting up their respective components, so your initial focus should be on establishing the test framework and mocks. 

    Once you have set up the basic test structure, create a feature branch named `feature/QA-001-test-harness` and commit your work. Then create a PR targeting the `develop` branch.

    Let me know if you have any questions or if you identify any blockers.

    Thank you,
    Project Manager
  </content>
</message> 