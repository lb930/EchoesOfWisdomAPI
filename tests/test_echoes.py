from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_echo_by_name():
    """Test retrieving an echo by name."""
    response = client.get("/echoes/name/Zol")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Zol"
    assert data["type"] == "monster"
    assert data["image"].startswith("http")


def test_get_echo_by_name_case_insensitive():
    """Test case-insensitive echo retrieval by name."""
    response = client.get("/echoes/name/zol")
    assert response.status_code == 200
    assert response.json()["name"] == "Zol"


def test_get_echo_by_name_not_found():
    """Test handling of non-existent echo name."""
    response = client.get("/echoes/name/doesnotexist")
    assert response.status_code == 404


def test_get_all_echoes():
    """Test retrieving all echoes."""
    response = client.get("/echoes/all/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert all(e["image"].startswith("http") for e in data)


def test_get_all_echoes_pagination():
    """Test pagination for retrieving all echoes."""
    response = client.get("/echoes/all/?offset=0&limit=5")
    assert response.status_code == 200
    assert len(response.json()) == 5


def test_get_monsters():
    """Test retrieving monster echoes."""
    response = client.get("/echoes/monsters/")
    assert response.status_code == 200
    assert all(e["type"] == "monster" for e in response.json())


def test_get_objects():
    """Test retrieving object echoes."""
    response = client.get("/echoes/objects/")
    assert response.status_code == 200
    assert all(e["type"] == "object" for e in response.json())