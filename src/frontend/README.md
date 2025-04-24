# Viewzenix Frontend

This directory contains the frontend application for Viewzenix, built with React and Next.js.

## Technology Stack

- **Next.js**: React framework for production
- **React**: UI library
- **TypeScript**: Type-safe JavaScript
- **Styled Components**: CSS-in-JS styling
- **React Icons**: Icon library

## Directory Structure

```
frontend/
├── components/       # Reusable UI components
│   ├── layout/       # Layout components (Layout, Navbar, Sidebar)
│   └── ui/           # UI components (buttons, cards, etc.)
├── hooks/            # Custom React hooks
├── pages/            # Next.js pages (routes)
├── services/         # API service calls
├── styles/           # Global styles, themes
├── types/            # TypeScript interfaces and types
└── utils/            # Utility functions
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

## Features

The dashboard includes the following tabs:

1. **Webhook Setup**: Configure TradingView alerts with your Viewzenix webhook endpoint
2. **Brokers**: Configure broker connections and settings
3. **Bots**: Configure trading bots and automation settings
4. **Logs**: View system and trading activity logs
5. **Analytics**: View performance metrics and trading statistics

## Building for Production

```bash
npm run build
```

The production build will be created in the `.next` directory.

## Design Specifications

UI design specifications are available in `/workspace/Viewzenix/docs/ui/DESIGN_SPECS.md`.

*Note: This README will be updated as the frontend implementation progresses.* 