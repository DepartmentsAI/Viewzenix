# Viewzenix Frontend

This directory contains the frontend application for Viewzenix, built with React and TypeScript.

## Technology Stack

- **React**: UI library
- **TypeScript**: Type-safe JavaScript
- **React Router**: Client-side routing
- **CSS Modules/Styled Components**: Styling approach
- **Axios**: HTTP client for API requests
- **Jest/React Testing Library**: Testing framework

## Directory Structure

```
frontend/
├── components/       # Reusable UI components
├── hooks/            # Custom React hooks
├── pages/            # Page components corresponding to routes
├── services/         # API service calls
├── store/            # State management
├── styles/           # Global styles, themes, variables
├── types/            # TypeScript interfaces and types
├── utils/            # Utility functions
└── tests/            # Frontend-specific test utilities
```

## Getting Started

To run the frontend application locally:

```bash
# From the project root
npm run dev:frontend

# Or directly from the frontend directory
cd src/frontend
npm run dev
```

The application will be available at `http://localhost:3000`.

## Code Conventions

- Follow the project's TypeScript standards
- Use functional components with hooks
- Place styles in separate CSS module files
- Include unit tests for all components
- Follow accessibility best practices

## Testing

```bash
# Run unit tests
npm test

# Run with coverage
npm test -- --coverage
```

## Building for Production

```bash
npm run build:frontend
```

The production build will be created in the `build` directory.

## Design Documentation

UI design specifications are available in `/workspace/Viewzenix/docs/ui/DESIGN_SPECS.md`.

*Note: This README will be updated as the frontend implementation progresses.* 