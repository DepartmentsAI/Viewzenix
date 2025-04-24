# Viewzenix Shared Resources

This directory contains common code and resources shared between different parts of the Viewzenix application (frontend, backend, integration).

## Purpose

The shared directory provides:
- Common code that can be reused across the application
- Standardized interfaces and types
- Utility functions used by multiple layers
- Shared constants and configurations

## Directory Structure

```
shared/
├── constants/        # Shared constants and enums
├── errors/           # Error classes and error handling utilities
├── interfaces/       # Common TypeScript interfaces
├── types/            # Common TypeScript types
├── models/           # Shared data models
├── utils/            # Utility functions
└── validation/       # Data validation schemas and functions
```

## Usage Guidelines

### When to Add Code to Shared

Code should be added to the shared directory when:
- It's used by multiple parts of the application (frontend, backend, integration)
- It provides common functionality that should be consistent across the application
- It defines interfaces or types that cross application boundaries

### When Not to Add Code to Shared

Keep code out of shared when:
- It's specific to only one part of the application
- It introduces unnecessary dependencies
- It tightly couples different parts of the application

## Best Practices

- Keep shared code minimal and focused
- Avoid introducing dependencies in shared code whenever possible
- Document all shared interfaces, types, and utilities thoroughly
- Write comprehensive tests for shared code
- Get consensus from multiple agents before making significant changes

## Examples

### Shared Interfaces

```typescript
// interfaces/User.ts
export interface User {
  id: string;
  email: string;
  name: string;
  createdAt: Date;
}
```

### Shared Utilities

```typescript
// utils/formatting.ts
export function formatDate(date: Date): string {
  return date.toISOString().split('T')[0];
}
```

### Shared Constants

```typescript
// constants/apiStatus.ts
export enum ApiStatus {
  SUCCESS = 'success',
  ERROR = 'error',
  LOADING = 'loading',
}
```

## Testing

```bash
# Run tests for shared code
npm test -- --testPathPattern=shared
```

*Note: This README will be updated as the shared code implementation progresses.* 