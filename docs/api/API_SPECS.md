# Viewzenix API Specifications

This document outlines the RESTful API endpoints for the Viewzenix application.

## API Base URL

- Development: `http://localhost:3001/api/v1`
- Production: [To be determined]

## Authentication

Most endpoints require authentication using JSON Web Tokens (JWT).

**Authentication Header Format:**
```
Authorization: Bearer <token>
```

**Token Acquisition:**
- Obtain via the `/auth/login` endpoint
- Refresh via the `/auth/refresh` endpoint

## Standard Response Format

All API responses follow this standard format:

```json
{
  "success": true|false,
  "data": { /* response data */ },
  "error": { 
    "code": "ERROR_CODE",
    "message": "Human-readable error message"
  },
  "meta": { 
    "pagination": { /* pagination info if applicable */ }
  }
}
```

## Error Codes

Common error codes that may be returned:

- `UNAUTHORIZED`: Authentication token missing or invalid
- `FORBIDDEN`: User lacks permission for the requested operation
- `NOT_FOUND`: Requested resource not found
- `VALIDATION_ERROR`: Request data failed validation
- `SERVER_ERROR`: Internal server error

## Endpoints

### Authentication

#### POST /auth/register
Creates a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "name": "John Doe"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "userId": "123e4567-e89b-12d3-a456-426614174000",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

#### POST /auth/login
Authenticates a user and returns a JWT.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "token": "eyJhbG...",
    "refreshToken": "eyJhbG...",
    "expiresIn": 3600
  }
}
```

#### POST /auth/refresh
Refreshes an expired JWT using a refresh token.

**Request Body:**
```json
{
  "refreshToken": "eyJhbG..."
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "token": "eyJhbG...",
    "refreshToken": "eyJhbG...",
    "expiresIn": 3600
  }
}
```

### Users

#### GET /users/profile
Retrieves the authenticated user's profile.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "userId": "123e4567-e89b-12d3-a456-426614174000",
    "email": "user@example.com",
    "name": "John Doe",
    "createdAt": "2023-04-01T12:00:00Z"
  }
}
```

#### PUT /users/profile
Updates the authenticated user's profile.

**Request Body:**
```json
{
  "name": "John Updated Doe",
  "email": "updated@example.com"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "userId": "123e4567-e89b-12d3-a456-426614174000",
    "email": "updated@example.com",
    "name": "John Updated Doe",
    "updatedAt": "2023-04-02T12:00:00Z"
  }
}
```

### [Other Resources]

Additional API endpoints will be defined as the project progresses.

## Pagination

For endpoints that return lists, pagination is supported using the following query parameters:

- `page`: Page number (default: 1)
- `limit`: Results per page (default: 20, max: 100)

**Example:**
```
GET /api/v1/resources?page=2&limit=10
```

**Paginated Response:**
```json
{
  "success": true,
  "data": [ /* array of items */ ],
  "meta": {
    "pagination": {
      "total": 45,
      "pages": 5,
      "page": 2,
      "limit": 10
    }
  }
}
```

## Rate Limiting

API endpoints are rate-limited to prevent abuse:

- 100 requests per minute per IP address
- 1000 requests per hour per user account

Exceeding these limits will result in a 429 Too Many Requests response.

## Versioning

The API version is included in the URL path (`/api/v1/`). Future breaking changes will use a new version number.

*Note: This API specification will be expanded as the project progresses.* 