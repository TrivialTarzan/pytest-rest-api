import yaml
import requests

BASE_URL = "https://run.mocky.io"

def test_get_books():
    response = requests.get(f"{BASE_URL}/v3/af807fa9-43a6-419f-a51e-962fe409a7b8")
    assert response.status_code == 200
    response_json = response.json()
    assert "status" in response_json
    assert "data" in response_json
    assert isinstance(response_json["data"]["books"], list)
    assert len(response_json["data"]["books"])

def test_create_book():
    new_book = {
        "title": "Refactoring",
        "author": "Martin Fowler",
        "published_year": "1999",
        "genre": "Technology",
        "price": "45.99"
    }
    response = requests.post(f"{BASE_URL}/v3/fdb59946-d736-422d-9afd-a914f7fd42d8", json=new_book)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["status"] == "success"
    assert response_json["message"] == "Book created successfully"
    assert "data" in response_json
    assert response_json["data"]["title"] == new_book["title"]
    assert response_json["data"]["genre"] == new_book["genre"]

def test_update_book():
    book_id = 3
    updated_data = {
        "price": 42.99,
        "available": False
    }
    response = requests.put(f"{BASE_URL}/v3/15d96d11-5e31-4e87-a1cc-64f6771f6960", json=updated_data)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["status"] == "success"
    assert response_json["message"] == "Book updated successfully"
    assert response_json["data"]["price"] == updated_data["price"]
    assert response_json["data"]["available"] == updated_data["available"]

