import pytest

@pytest.mark.timeout(1.5)
def test_should_update_redis(redis_client, http_client):
    # Given
    redis_client.set('page_reviews', 4)

    # When
    response = http_client.get('/')

    # Then
    assert response.status_code == 200
    assert response.text == "This page has been reviewed 5 times."
    assert redis_client.get("page_reviews") == b"5"