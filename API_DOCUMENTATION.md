# API Documentation

Base URL for local development:

```text
http://127.0.0.1:8000
```

## Products

### List Products

```http
GET /api/products/
```

### Example Requests

```http
GET /api/products/?q=wireless
GET /api/products/?category=1
GET /api/products/?tags=2&tags=5
GET /api/products/?q=wireless&category=1&tags=2
```

When multiple `tags` values are provided, the product must contain every selected tag.

### Example Response

```json
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
        "name": "Wireless"
      },
      {
        "id": 5,
        "name": "Sale"
      }
    ]
  }
]
```

## Categories

### List Categories

```http
GET /api/categories/
```

### Example Response

```json
[
  {
    "id": 1,
    "name": "Electronics"
  },
  {
    "id": 2,
    "name": "Home"
  }
]
```

## Tags

### List Tags

```http
GET /api/tags/
```

### Example Response

```json
[
  {
    "id": 1,
    "name": "New"
  },
  {
    "id": 2,
    "name": "Wireless"
  }
]
```

## Status Codes

- `200 OK`: Request completed successfully.



