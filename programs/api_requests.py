import requests
def test_get_users():
    response=requests.get("https://www.linkedin.com/feed/")
    assert response.status_code==200
