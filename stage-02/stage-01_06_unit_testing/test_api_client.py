from unittest.mock import Mock, patch

from api_client import get_user


@patch("api_client.requests.get")
def test_get_user(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "id": 1,
        "name": "Ghanshyam"
    }

    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    result = get_user(1)

    assert result["id"] == 1
    assert result["name"] == "Ghanshyam"

    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users/1"
    )