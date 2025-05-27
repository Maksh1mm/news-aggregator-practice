from fastapi.testclient import TestClient
from backend.app import app
from backend.app import store, STUDENT_ID
from config import STUDENT_ID

client = TestClient(app)

def test_get_empty_sources():
    store[STUDENT_ID] = []
    res = client.get(f"/sources/{STUDENT_ID}")
    assert res.status_code == 200
    assert res.json() == {"sources": []}

def test_add_and_get_source():
    store[STUDENT_ID] = []
    res1 = client.post(f"/sources/{STUDENT_ID}", json={"url": "<https://example.com/rss>"})
    assert res1.status_code == 200
    assert "<https://example.com/rss>" in res1.json()["sources"]
    res2 = client.get(f"/sources/{STUDENT_ID}")
    assert "<https://example.com/rss>" in res2.json()["sources"]

