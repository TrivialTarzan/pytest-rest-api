# API Documentation

## POST - Add Contact

### Endpoint
```
POST https://thinking-tester-contact-list.herokuapp.com/contacts
```

### Headers
```
Authorization: Bearer {{token}}
```

### Body (JSON)
```json
{
    "firstName": "John",
    "lastName": "Doe",
    "birthdate": "1970-01-01",
    "email": "jdoe@fake.com",
    "phone": "8005555555",
    "street1": "1 Main St.",
    "street2": "Apartment A",
    "city": "Anytown",
    "stateProvince": "KS",
    "postalCode": "12345",
    "country": "USA"
}
```

### Example Request (cURL)
```sh
curl --location 'https://thinking-tester-contact-list.herokuapp.com/contacts' \
--header 'Authorization: Bearer {{token}}' \
--data-raw '{
    "firstName": "John",
    "lastName": "Doe",
    "birthdate": "1970-01-01",
    "email": "jdoe@fake.com",
    "phone": "8005555555",
    "street1": "1 Main St.",
    "street2": "Apartment A",
    "city": "Anytown",
    "stateProvince": "KS",
    "postalCode": "12345",
    "country": "USA"
}'
```

### Example Request (Python)
```python
import requests

url = "https://thinking-tester-contact-list.herokuapp.com/contacts"

payload = """
{
    "firstName": "John",
    "lastName": "Doe",
    "birthdate": "1970-01-01",
    "email": "jdoe@fake.com",
    "phone": "8005555555",
    "street1": "1 Main St.",
    "street2": "Apartment A",
    "city": "Anytown",
    "stateProvince": "KS",
    "postalCode": "12345",
    "country": "USA"
}
"""
headers = {
  'Authorization': 'Bearer {{token}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

### Example Response (201 Created)
```json
{
  "_id": "6085a221fcfc72405667c3d4",
  "firstName": "John",
  "lastName": "Doe",
  "birthdate": "1970-01-01",
  "email": "jdoe@fake.com",
  "phone": "8005555555",
  "street1": "1 Main St.",
  "street2": "Apartment A",
  "city": "Anytown",
  "stateProvince": "KS",
  "postalCode": "12345",
  "country": "USA",
  "owner": "6085a21efcfc72405667c3d4",
  "__v": 0
}
```

---

## GET - Get Contact List

### Endpoint
```
GET https://thinking-tester-contact-list.herokuapp.com/contacts
```

### Headers
```
Authorization: Bearer {{token}}
```

### Example Request (cURL)
```sh
curl --location 'https://thinking-tester-contact-list.herokuapp.com/contacts' \
--header 'Authorization: Bearer {{token}}'
```

### Example Request (Python)
```python
import requests

url = "https://thinking-tester-contact-list.herokuapp.com/contacts"

payload = {}
headers = {
  'Authorization': 'Bearer {{token}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

### Example Response (200 OK)
```json
[
  {
    "_id": "6085a221fcfc72405667c3d4",
    "firstName": "John",
    "lastName": "Doe",
    "birthdate": "1970-01-01",
    "email": "jdoe@fake.com",
    "phone": "8005555555",
    "street1": "1 Main St.",
    "street2": "Apartment A",
    "city": "Anytown",
    "stateProvince": "KS",
    "postalCode": "12345",
    "country": "USA",
    "owner": "6085a21efcfc72405667c3d4",
    "__v": 0
  },
  {
    "_id": "607b29861ba4d3a0b96733bc",
    "firstName": "Jan",
    "lastName": "Brady",
    "birthdate": "2001-11-11",
    "email": "fake2@gmail.com",
    "phone": "8008675309",
    "street1": "100 Elm St.",
    "city": "Springfield",
    "stateProvince": "NE",
    "postalCode": "23456",
    "country": "United States",
    "owner": "6085a21efcfc72405667c3d4",
    "__v": 0
  }
]
```

---

## DELETE - Delete Contact

### Endpoint
```
DELETE https://thinking-tester-contact-list.herokuapp.com/contacts/
```

### Headers
```
Authorization: Bearer {{token}}
```

### Example Request (cURL)
```sh
curl --location --request DELETE 'https://thinking-tester-contact-list.herokuapp.com/contacts/' \
--header 'Authorization: Bearer {{token}}'
```

### Example Request (Python)
```python
import requests

url = "https://thinking-tester-contact-list.herokuapp.com/contacts/"

payload = {}
headers = {
  'Authorization': 'Bearer {{token}}'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

### Example Response (200 OK)
```
Contact deleted
```

## POST - Add User
**Endpoint:** `https://thinking-tester-contact-list.herokuapp.com/users`

### Request Body (JSON)
```json
{
    "firstName": "Test",
    "lastName": "User",
    "email": "test@fake.com",
    "password": "myPassword"
}
```

### Example Request
```python
import requests

url = "https://thinking-tester-contact-list.herokuapp.com/users"

payload = """
{
    "firstName": "Test",
    "lastName": "User",
    "email": "test@fake.com",
    "password": "myPassword"
}
"""
headers = {
  'Authorization': 'Bearer {{token}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

### Example Response
```json
{
  "user": {
    "_id": "608b2db1add2691791c04c89",
    "firstName": "Test",
    "lastName": "User",
    "email": "test@fake.com",
    "__v": 1
  },
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## GET - Get User Profile
**Endpoint:** `https://thinking-tester-contact-list.herokuapp.com/users/me`

> **Note:** This operation is not available through the UI.

### Example Request
```python
import requests

url = "https://thinking-tester-contact-list.herokuapp.com/users/me"

payload = {}
headers = {
  'Authorization': 'Bearer {{token}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

### Example Response
```json
{
  "_id": "608b2db1add2691791c04c89",
  "firstName": "Test",
  "lastName": "User",
  "email": "test@fake.com",
  "__v": 1
}
```

---

## PATCH - Update User
**Endpoint:** `https://thinking-tester-contact-list.herokuapp.com/users/me`

> **Note:** This operation is not available through the UI.

### Request Body (JSON)
```json
{
    "firstName": "Updated",
    "lastName": "Username",
    "email": "test2@fake.com",
    "password": "myNewPassword"
}
```

### Example Request
```python
import requests

url = "https://thinking-tester-contact-list.herokuapp.com/users/me"

payload = """
{
    "firstName": "Updated",
    "lastName": "Username",
    "email": "test2@fake.com",
    "password": "myNewPassword"
}
"""
headers = {
  'Authorization': 'Bearer {{token}}'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
```

### Example Response
```json
{
  "_id": "608b2db1add2691791c04c89",
  "firstName": "Updated",
  "lastName": "Username",
  "email": "test2@fake.com",
  "__v": 1
}
```

---

## POST - Log Out User
**Endpoint:** `https://thinking-tester-contact-list.herokuapp.com/users/logout`

### Example Request
```python
import requests

url = "https://thinking-tester-contact-list.herokuapp.com/users/logout"

payload = {}
headers = {
  'Authorization': 'Bearer {{token}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

### Example Response
No response body.

---

## POST - Log In User
**Endpoint:** `https://thinking-tester-contact-list.herokuapp.com/users/login`

### Request Body (JSON)
```json
{
    "email": "test2@fake.com",
    "password": "myNewPassword"
}
```

### Example Request
```python
import requests

url = "https://thinking-tester-contact-list.herokuapp.com/users/login"

payload = """
{
    "email": "test2@fake.com",
    "password": "myNewPassword"
}
"""
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

### Example Response
```json
{
  "user": {
    "_id": "608b2db1add2691791c04c89",
    "firstName": "Updated",
    "lastName": "Username",
    "email": "test2@fake.com",
    "__v": 212
  },
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## DELETE - Delete User
**Endpoint:** `https://thinking-tester-contact-list.herokuapp.com/users/me`

> **Note:** This operation is not available through the UI.

### Example Request
```python
import requests

url = "https://thinking-tester-contact-list.herokuapp.com/users/me"

payload = {}
headers = {
  'Authorization': 'Bearer {{token}}'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

### Example Response
(200 OK)

No response body.

