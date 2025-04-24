# Viewzenix Backend

This directory contains the backend application for Viewzenix, built with Node.js, Express, and TypeScript.

## Technology Stack

- **Node.js**: Runtime environment
- **TypeScript**: Type-safe JavaScript
- **Express**: Web framework
- **JWT**: Authentication mechanism
- **Middleware**: Request processing
- **Jest**: Testing framework

## Directory Structure

```
backend/
├── config/           # Configuration for environments
├── controllers/      # Route controllers
├── middlewares/      # Express middlewares
├── models/           # Data models and schemas
├── repositories/     # Data access layer
├── routes/           # API route definitions
├── services/         # Business logic
├── types/            # TypeScript interfaces and types
├── utils/            # Utility functions
└── tests/            # Backend-specific test utilities
```

## Getting Started

To run the backend application locally:

```bash
# From the project root
npm run dev:backend

# Or directly from the backend directory
cd src/backend
npm run dev
```

The API will be available at `http://localhost:3001`.

## API Documentation

API specifications are available in `/workspace/Viewzenix/docs/api/API_SPECS.md`.

## Code Conventions

- Follow the project's TypeScript standards
- Use dependency injection for services and repositories
- Write comprehensive unit tests
- Follow RESTful design principles
- Implement proper error handling

## Environment Variables

Create a `.env` file in the backend directory with the following variables:

```
NODE_ENV=development
PORT=3001
DB_CONNECTION_STRING=
JWT_SECRET=your_jwt_secret
JWT_EXPIRATION=3600
CORS_ORIGIN=http://localhost:3000
```

## Testing

```bash
# Run unit tests
npm test

# Run with coverage
npm test -- --coverage
```

## Database Migrations

[To be implemented based on selected database technology]

## Logging

Follows the standards defined in `/workspace/Viewzenix/docs/007-metrics-tracing.mdc`:
- Structured logging (JSON format)
- Appropriate log levels
- Error tracking
- Request tracing

*Note: This README will be updated as the backend implementation progresses.* 