# Viewzenix Project Plan

This document outlines the detailed plan for developing the Viewzenix application.

## Project Team

The Viewzenix project will be developed by a team of specialized AI agents:

- **Project Manager (PM)**: Overall project coordination, task management, and communication hub
- **Frontend/UI (FE)**: UI components and client-side application logic
- **Backend/Architecture (BE)**: Server-side logic, APIs, and application architecture
- **Integration (INT)**: Connecting components and external service integration
- **QA & Testing (QA)**: Quality assurance and comprehensive testing

## Project Scope

### Primary Deliverable: Trading Webhook Platform

The main deliverable of the Viewzenix project is a deterministic, broker-agnostic trading webhook platform that processes TradingView alerts and executes trades through various broker APIs. The platform will include:

1. **Flask Webhook API**: Receive and process TradingView alerts
2. **Trade Router**: Validate and normalize alert data, classify assets and trade types
3. **Order Engine**: Execute trades via broker-specific adapters
4. **Risk Management System**: Implement per-order and global stop-loss/take-profit
5. **Cleanup Service**: Manage orphaned orders when positions are closed
6. **Logging System**: Comprehensive transaction and activity logging
7. **React Dashboard**: Configure settings, monitor trades, and analyze performance
8. **Test Harness**: Offline testing capability that works when markets are closed

## Development Approach

The project will follow an iterative development approach with the following principles:

1. **Prompt Unit Management**: Work will be estimated and tracked using Prompt Units (PUs) as defined in 002-prompt-measurement-guidelines.mdc
2. **Incremental Delivery**: Features will be developed in manageable increments
3. **Continuous Integration**: Code will be regularly merged to the develop branch
4. **Quality Gates**: All code must pass automated tests before merging
5. **Broker Agnosticism**: Core logic must work identically across different brokers

## Sprint Structure

Each sprint will be 2 weeks long and follow this structure:

1. **Sprint Planning**: PM assigns tasks to agents based on roadmap priorities
2. **Development**: Agents work on assigned tasks, communicate blockers/progress
3. **Review**: Code review and quality assurance
4. **Retrospective**: Document learnings in knowledge base

## Task Assignment Process

1. PM breaks down features into assignable tasks
2. Tasks are prioritized based on dependencies and roadmap
3. Tasks are assigned to appropriate agents via GitHub Issues
4. Agents estimate effort in Prompt Units (PUs)
5. PM finalizes and communicates schedule

## Communication Structure

- GitHub Issues: Primary task tracking
- Agent messages: Direct inter-agent communication following 010-communication-protocol-always.mdc
- Decision Log: Record of significant decisions maintained by PM

## Risk Management

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Technical complexity exceeds agent capabilities | Medium | High | Break down tasks into smaller units, provide detailed specifications |
| Integration issues between components | High | Medium | Establish clear interfaces, regular integration testing |
| Resource constraints | Medium | Medium | Prioritize features, focus on core functionality first |
| Security vulnerabilities | Medium | High | Regular security reviews, follow security red lines |
| Broker API limitations | Medium | High | Develop adapter pattern with abstraction layer, thorough testing |
| Market closed testing challenges | High | Medium | Develop comprehensive test harnesses with mocked broker responses |
| Portfolio risk management failures | Low | Very High | Implement multiple layers of fail-safes, careful testing |

## Implementation Phases

### Phase 1: Core Architecture (Weeks 1-4)
- Set up project infrastructure and communication
- Design initial architecture and component interfaces
- Implement Flask webhook receiver and validation
- Create initial React dashboard shell

### Phase 2: Trading Foundation (Weeks 5-7)
- Implement trade classifier and router
- Develop AlpacaAdapter with basic order placement
- Create order engine with multiple order types
- Develop initial logging system

### Phase 3: Risk Management (Weeks 8-10)
- Implement per-order stop-loss/take-profit functionality
- Develop cleanup service for orphaned orders
- Create global portfolio monitoring
- Enhance dashboard with configuration panels

### Phase 4: Testing & Integration (Weeks 11-14)
- Develop comprehensive test harnesses
- Integrate all components
- Create detailed logging and analytics
- Implement remaining UI features

### Phase 5: Deployment & Launch (Weeks 15-16)
- Setup production environment
- Final testing and quality assurance
- Documentation and handoff preparation
- Launch and monitoring

## Success Criteria

The project will be considered successful when:

1. All features in the roadmap are implemented
2. The application passes all quality gates
3. The system meets performance and security requirements
4. Documentation is complete and accurate
5. The trading platform can:
   - Process TradingView webhooks reliably
   - Execute trades through Alpaca API deterministically
   - Apply proper risk management controls
   - Provide a usable dashboard for monitoring and configuration
   - Function correctly in both market open and closed states
   - Be tested without reliance on live broker connectivity

## Deployment Strategy

- Frontend: Static hosting on Fly.io
- Backend (Node.js): Containerized application on Fly.io
- Webhook API (Flask): Containerized application on Fly.io with private networking
- Database: Managed service or containerized
- Secrets: Managed through Fly.io secrets store
- CI/CD: GitHub Actions for automated testing and deployment

*Note: This plan will be revised and updated as the project progresses.* 