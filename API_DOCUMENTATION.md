# API Documentation

Base URL for local development:

http://127.0.0.1:8000

## Products

### List Products

GET /api/products/

Returns a list of all products. Supports optional search and filtering via query parameters.

### Query Parameters

| Parameter  | Type     | Description                                      |
|------------|----------|--------------------------------------------------|
| search     | string   | Search products by name or description           |
| category   | integer  | Filter products by category ID                   |
| tags       | integer  | Filter products by tag ID (can pass multiple)    |

### Example Requests

# Get all products
GET /api/products/

# Search by name or description
GET /api/products/?search=wireless

# Filter by category
GET /api/products/?category=1

# Filter by one or more tags
GET /api/products/?tags=2&tags=5

# Combine search and filters
GET /api/products/?search=wireless&category=1&tags=2

When multiple tags values are provided, products matching ANY of the selected tags are returned.

### Example Response

[
  {
    "id": 1,
    "name": "Wireless Headphones",
    "price": "99.99",
    "description": "Wireless noise cancelling headphones",
    "category": {
      "id": 1,
      "name": "Electronics"
    },
    "tags": [
      {
        "id": 2,
        "name": "wireless"
      },
      {
        "id": 5,
        "name": "sale"
      }
    ]
  }
]

## Categories

### List Categories

GET /api/categories/

Returns a list of all categories. Used to populate the category filter dropdown.

### Example Response

[
  {
    "id": 1,
    "name": "Electronics"
  },
  {
    "id": 2,
    "name": "Furniture"
  }
]

## Tags

### List Tags

GET /api/tags/

Returns a list of all tags. Used to populate the tag filter checkboxes.

### Example Response

[
  {
    "id": 1,
    "name": "wireless"
  },
  {
    "id": 2,
    "name": "portable"
  }
]

## Status Codes

| Code    | Meaning                        |
|---------|--------------------------------|
| 200 OK  | Request completed successfully |
| 404     | Endpoint not found             |