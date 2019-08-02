from unittest.mock import patch

from spotify_api.oauth2 import SpotifyClientCredentials
from .mocks import MockResponse


class TestSpotifyClientCredentials:
    @patch('requests.post', autospec=True, spec_set=True)
    def test_get_access_token(self, mock_requests, token):
        mock_requests.return_value = MockResponse(200, token)
        client = SpotifyClientCredentials()
        assert client.get_access_token() == 'token'
        assert client.get_access_token() == 'token'
        mock_requests.assert_called_once()
