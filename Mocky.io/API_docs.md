# Mocky API Documentation

## Mocky: [https://designer.mocky.io/](https://designer.mocky.io/)

---

## GET Method
### URL: [https://run.mocky.io/v3/af807fa9-43a6-419f-a51e-962fe409a7b8](https://run.mocky.io/v3/af807fa9-43a6-419f-a51e-962fe409a7b8)

### HTTP Headers:
```json
{
  "Host": "api.booknest.com",
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
  "Content-Type": "application/json",
  "Accept": "application/json",
  "User-Agent": "PostmanRuntime/7.29.0",
  "Cache-Control": "no-cache",
  "Connection": "keep-alive"
}
```

### JSON Response Body:
```json
{
  "status": "success",
  "data": {
    "books": [
      {
        "id": 1,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt, David Thomas",
        "published_year": 1999,
        "genre": "Technology",
        "price": 39.99,
        "available": true
      },
      {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "published_year": 2008,
        "genre": "Technology",
        "price": 49.99,
        "available": false
      }
    ]
  },
  "timestamp": "2025-02-10T12:00:00Z"
}
```

---

## POST Method (Create a New Book)
### URL: [https://run.mocky.io/v3/fdb59946-d736-422d-9afd-a914f7fd42d8](https://run.mocky.io/v3/fdb59946-d736-422d-9afd-a914f7fd42d8)

### Request Body:
```json
{
  "title": "Refactoring",
  "author": "Martin Fowler",
  "published_year": 1999,
  "genre": "Technology",
  "price": 45.99
}
```

### Response Body:
```json
{
  "status": "success",
  "message": "Book created successfully",
  "data": {
    "id": 3,
    "title": "Refactoring",
    "author": "Martin Fowler",
    "published_year": 1999,
    "genre": "Technology",
    "price": 45.99,
    "available": true
  }
}
```

---

## PUT Method (Update a Book)
### URL: [https://run.mocky.io/v3/15d96d11-5e31-4e87-a1cc-64f6771f6960](https://run.mocky.io/v3/15d96d11-5e31-4e87-a1cc-64f6771f6960)

### Request Body:
```json
{
  "price": 42.99,
  "available": false
}
```

### Response Body:
```json
{
  "status": "success",
  "message": "Book updated successfully",
  "data": {
    "id": 3,
    "title": "Refactoring",
    "author": "Martin Fowler",
    "published_year": 1999,
    "genre": "Technology",
    "price": 42.99,
    "available": false
  }
}
```

---

## DELETE Method (Delete a Book)

### Response Body:
```json
{
  "status": "success",
  "message": "Book deleted successfully"
}
```
`
