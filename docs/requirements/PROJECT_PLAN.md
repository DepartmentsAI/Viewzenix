# Viewzenix Project Plan

## 1. Project Overview

Viewzenix is a trading webhook platform that enables deterministic, broker-agnostic trade execution from TradingView alerts. The project will be developed in phases with clear milestones, leveraging a team of specialized AI agents working in coordination.

## 2. Team Structure & Responsibilities

| Agent Role | Primary Responsibilities | Key Deliverables |
|------------|--------------------------|------------------|
| **Project Manager (PM)** | Project planning, task management, stakeholder communication | Project plan, task breakdown, progress tracking, risk management |
| **Backend/Architecture (BE)** | API development, core business logic, database schema | Flask API, broker adapters, order engine, webhook handling |
| **Frontend/UI (FE)** | User interface, dashboard, data visualization | React dashboard, settings screens, UI components |
| **Integration (INT)** | External service integration, message flow | Broker API integration, TradingView connection |
| **QA & Testing (QA)** | Quality assurance, test automation | Test plans, automated tests, test harnesses |

## 3. Development Phases & Milestones

### Phase 1: Foundation (2 weeks)

**Milestone 1: Project Setup & Architecture**
- Setup development environment and repositories
- Define detailed architecture and component structure
- Create databases and data models
- Establish CI/CD pipelines

**Milestone 2: Core API Development**
- Implement webhook receiver with validation
- Develop trade classifier and order engine base
- Create basic logging system
- Build initial test framework

### Phase 2: Core Functionality (3 weeks)

**Milestone 3: Order Management System**
- Implement AlpacaAdapter
- Develop SL/TP order creation logic
- Build order cleanup service
- Create global SL/TP tracker

**Milestone 4: Frontend Dashboard (Basic)**
- Develop React application structure
- Create main dashboard layout and navigation
- Implement configuration screens
- Build order and position displays

### Phase 3: Integration & Enhancement (2 weeks)

**Milestone 5: Full Integration**
- Connect frontend to backend APIs
- Implement real-time updates where appropriate
- Complete broker integration
- Finalize error handling and recovery

**Milestone 6: Testing & Refinement**
- Complete comprehensive test suite
- Perform security review
- Optimize performance
- Document APIs and user flows

### Phase 4: Deployment & Final Delivery (1 week)

**Milestone 7: Deployment**
- Configure Fly.io deployment
- Set up monitoring and logging
- Complete security configuration
- Perform final system testing

**Milestone 8: Handoff**
- Finalize documentation
- Create user guides
- Collect feedback and implement final adjustments
- Project handoff

## 4. Task Dependencies

| Task ID | Description | Dependencies | Estimated Effort (PU) |
|---------|-------------|--------------|------------------------|
| BE-001 | Setup Flask project structure | - | 1 |
| BE-002 | Implement webhook receiver | BE-001 | 2 |
| BE-003 | Develop trade classifier | BE-001 | 2 |
| BE-004 | Build AlpacaAdapter | BE-001 | 3 |
| BE-005 | Implement order engine | BE-003, BE-004 | 3 |
| BE-006 | Create SL/TP functionality | BE-005 | 2 |
| BE-007 | Build cleanup service | BE-006 | 2 |
| BE-008 | Develop global SL/TP tracker | BE-006 | 2 |
| BE-009 | Implement API endpoints for UI | BE-005, BE-006, BE-007, BE-008 | 3 |
| FE-001 | Setup React project | - | 1 |
| FE-002 | Create dashboard layout | FE-001 | 2 |
| FE-003 | Build webhook configuration UI | FE-002 | 2 |
| FE-004 | Implement broker settings UI | FE-002 | 2 |
| FE-005 | Develop bot configuration UI | FE-002 | 2 |
| FE-006 | Create logs display | FE-002 | 2 |
| FE-007 | Build analytics dashboard | FE-002 | 3 |
| FE-008 | Integrate UI with backend APIs | FE-003, FE-004, FE-005, FE-006, FE-007, BE-009 | 3 |
| INT-001 | Implement TradingView schema validation | BE-002 | 2 |
| INT-002 | Build broker API integration | BE-004 | 3 |
| INT-003 | Create logging bus | BE-001 | 2 |
| QA-001 | Develop test harness | BE-002, BE-003 | 2 |
| QA-002 | Create webhook validation tests | INT-001 | 2 |
| QA-003 | Build order flow tests | BE-005, BE-006 | 3 |
| QA-004 | Implement cleanup service tests | BE-007 | 2 |
| QA-005 | Create global SL/TP tests | BE-008 | 2 |
| QA-006 | Develop UI integration tests | FE-008 | 3 |
| QA-007 | Perform security testing | All BE, INT | 3 |
| PM-001 | Create GitHub issues for all tasks | - | 1 |
| PM-002 | Monitor progress and resolve blockers | Ongoing | 1/week |
| PM-003 | Coordinate integration points | As needed | 1/week |
| PM-004 | Final review and documentation | All tasks | 2 |

## 5. Risk Management

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| Broker API changes | Medium | High | Create abstraction layer; monitor API announcements |
| WebSocket performance issues | Medium | Medium | Implement fallback polling; optimize data transfer |
| Complex UI interactions | Medium | Medium | Early prototyping; incremental implementation |
| Trade logic bugs | Low | High | Comprehensive test suite; manual testing plan |
| Security vulnerabilities | Low | High | Security review; secure coding practices |
| Integration complexity | Medium | Medium | Clear interface definitions; integration testing |

## 6. Communication Plan

- **Daily Coordination**: Agents communicate via standard message protocol
- **Issue Tracking**: All tasks managed via GitHub Issues
- **Blockers**: Immediately reported to PM using `BLOCKER_REPORT` message type
- **Handoffs**: Coordinated using the agent handoff protocol

## 7. Success Criteria

The project will be considered successful when:
- All functional requirements have been implemented and tested
- Non-functional requirements have been met and verified
- The system can successfully process TradingView alerts end-to-end
- Manual test sequence for crypto trading completes successfully
- All documentation has been completed and reviewed
- The system has been deployed to a secure production environment

## 8. Completion Checklist

- [ ] Provision Fly.io dev app (private)
- [ ] Implement Flask blueprints: `/webhook`, `/orders`, `/status`, `/cleanup`, `/bot_state`
- [ ] Build `AlpacaAdapter` covering all order types
- [ ] Complete React dashboard: advanced settings, logs, analytics
- [ ] Port all pytest scripts; broker calls mocked
- [ ] Confirm `logs.jsonl` & `activity.log` entries across flows
- [ ] Run manual crypto test sequence; deliver logs for sign-off
