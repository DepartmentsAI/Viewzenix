# Viewzenix

Viewzenix is an AI-driven software development project where specialized AI agents collaborate to build, test, and integrate a web application.

## Project Overview

This project demonstrates an AI-powered development pipeline that leverages:
- Specialized AI agents with distinct roles and responsibilities
- Standardized communication protocols
- Version control and workflow automation
- Quality assurance and testing methodologies

## Directory Structure

The project follows a standardized directory structure:

```
Viewzenix/
├── .github/              # GitHub workflows and templates
├── communication/        # Agent messaging area
├── config/               # Application configuration
├── docs/                 # Project documentation
├── infra/                # Infrastructure as code
├── libs/                 # Shared libraries
├── scripts/              # Utility scripts
├── src/                  # Source code
│   ├── frontend/         # Frontend code (FE Agent)
│   ├── backend/          # Backend code (BE Agent)
│   ├── integration/      # Integration code (INT Agent)
│   └── shared/           # Shared code
└── tests/                # Automated tests
```

## Getting Started

1. Review the documentation in `/docs/requirements/` to understand project goals
2. Check the current roadmap status in `/docs/requirements/ROADMAP.md`
3. Follow the development process outlined in `/docs/requirements/PROJECT_PLAN.md`

## Agent Roles

- **Project Manager (PM)**: Coordinates project activities and manages tasks
- **Frontend/UI (FE)**: Implements user interface and client-side functionality
- **Backend/Architecture (BE)**: Develops server-side logic and APIs
- **Integration (INT)**: Manages component integration and external services
- **QA & Testing (QA)**: Ensures quality through comprehensive testing

## Communication

All inter-agent communication follows the standardized protocol defined in Core Rules. Messages are exchanged through the inbox system in the `communication/` directory.

## License

[To be determined] 